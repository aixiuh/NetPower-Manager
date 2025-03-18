#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wakeonlan import send_magic_packet
from netpower.services.device_service import DeviceService

class PowerService:
    """电源控制服务类，负责唤醒和关闭设备"""
    
    @staticmethod
    def wake_device(device_id):
        """唤醒单个设备"""
        devices = DeviceService.load_devices()
        if 0 <= device_id < len(devices):
            device = devices[device_id]
            try:
                send_magic_packet(device.mac)
                return True, f"唤醒信号已发送到 {device.name}"
            except Exception as e:
                return False, f"发送唤醒信号失败: {str(e)}"
        return False, "设备不存在"
    
    @staticmethod
    def wake_multiple_devices(device_ids):
        """批量唤醒设备"""
        if not device_ids:
            return False, "未选择任何设备"
        
        devices = DeviceService.load_devices()
        success_count = 0
        
        for device_id in device_ids:
            if 0 <= device_id < len(devices):
                try:
                    send_magic_packet(devices[device_id].mac)
                    success_count += 1
                except:
                    pass
        
        if success_count > 0:
            return True, f"已向选中的 {success_count} 个设备发送唤醒信号"
        return False, "发送唤醒信号失败"
