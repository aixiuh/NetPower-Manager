#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from flask import current_app
from netpower.models.device import Device

class DeviceService:
    """设备服务类，负责设备的增删改查等操作"""
    
    _devices_cache = None  # 缓存设备列表
    
    @classmethod
    def get_devices(cls, refresh=False):
        """获取设备列表，支持缓存"""
        if cls._devices_cache is None or refresh:
            cls._devices_cache = cls.load_devices()
        return cls._devices_cache
    
    @staticmethod
    def load_devices():
        """从JSON文件加载设备数据"""
        data_file = current_app.config['DATA_FILE']
        devices = []
        
        try:
            if os.path.exists(data_file):
                with open(data_file, 'r', encoding='utf-8') as f:
                    data_list = json.load(f)
                    devices = [Device.from_dict(item) for item in data_list]
        except Exception as e:
            current_app.logger.error(f"加载设备数据失败: {str(e)}")
        
        return devices
    
    @classmethod
    def save_devices(cls, devices=None):
        """保存设备数据到JSON文件"""
        if devices is None:
            devices = cls._devices_cache or []
        else:
            cls._devices_cache = devices  # 更新缓存
            
        data_file = current_app.config['DATA_FILE']
        os.makedirs(os.path.dirname(data_file), exist_ok=True)
        
        try:
            device_dicts = [device.to_dict() for device in devices]
            with open(data_file, 'w', encoding='utf-8') as f:
                json.dump(device_dicts, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            current_app.logger.error(f"保存设备数据失败: {str(e)}")
            return False
    
    @classmethod
    def add_device(cls, name, mac, ip):
        """添加新设备"""
        # 验证输入
        if not name or not Device.is_valid_mac(mac) or not Device.is_valid_ip(ip):
            return False, "输入数据无效"
        
        # 创建设备并保存
        devices = cls.get_devices()
        new_device = Device(name=name, mac=mac, ip=ip)
        devices.append(new_device)
        
        if cls.save_devices(devices):
            return True, f"设备 {name} 添加成功"
        return False, "保存设备数据失败"
    
    @classmethod
    def update_device(cls, device_id, name, mac, ip):
        """更新设备信息"""
        # 验证输入
        if not name or not Device.is_valid_mac(mac) or not Device.is_valid_ip(ip):
            return False, "输入数据无效"
        
        # 获取设备并更新
        devices = cls.get_devices()
        if 0 <= device_id < len(devices):
            devices[device_id].name = name
            devices[device_id].mac = mac
            devices[device_id].ip = ip
            
            if cls.save_devices(devices):
                return True, f"设备 {name} 更新成功"
        
        return False, "设备不存在或保存失败"
    
    @classmethod
    def delete_device(cls, device_id):
        """删除设备"""
        devices = cls.get_devices()
        if 0 <= device_id < len(devices):
            deleted_name = devices[device_id].name
            del devices[device_id]
            
            if cls.save_devices(devices):
                return True, f"设备 {deleted_name} 已删除"
        
        return False, "设备不存在或删除失败"
    
    @classmethod
    def delete_multiple_devices(cls, device_ids):
        """批量删除设备"""
        if not device_ids:
            return False, "未选择任何设备"
        
        # 按ID从大到小排序，防止删除时索引变化
        device_ids = sorted([int(id) for id in device_ids if str(id).isdigit()], reverse=True)
        devices = cls.get_devices()
        deleted_count = 0
        
        for device_id in device_ids:
            if 0 <= device_id < len(devices):
                del devices[device_id]
                deleted_count += 1
        
        if deleted_count > 0 and cls.save_devices(devices):
            return True, f"已删除 {deleted_count} 个设备"
        
        return False, "删除设备失败"
    
    @classmethod
    def refresh_status(cls):
        """刷新所有设备状态"""
        devices = cls.get_devices(refresh=True)
        timeout = current_app.config.get('PING_TIMEOUT', 1)
        port = current_app.config.get('PING_PORT', 80)
        
        for device in devices:
            device.check_status(timeout, port)
        
        cls.save_devices(devices)  # 保存状态更新
        return devices
