#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wakeonlan import send_magic_packet
from netpower.services.device_service import DeviceService

class PowerService:
    """电源控制服务类，负责唤醒和关闭设备"""
    
    @staticmethod
    def wake_device(device_id):
        """唤醒单个设备"""
        devices = DeviceService.get_devices()
        if 0 <= device_id < len(devices):
            device = devices[device_id]
            try:
                send_magic_packet(device.mac)
                return True, f"唤醒信号已发送到 {device.name}"
            except Exception as e:
                return False, f"发送唤醒信号失败: {str(e)}"
        return False, "设备不存在"
