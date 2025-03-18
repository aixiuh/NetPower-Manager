#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import socket

class Device:
    """设备模型类"""
    
    def __init__(self, name, mac, ip, status=False):
        self.name = name
        self.mac = mac
        self.ip = ip
        self.status = status
    
    @classmethod
    def from_dict(cls, data):
        """从字典创建设备实例"""
        return cls(
            name=data.get('name', ''),
            mac=data.get('mac', ''),
            ip=data.get('ip', ''),
            status=data.get('status', False)
        )
    
    def to_dict(self):
        """将设备转换为字典"""
        return {
            'name': self.name,
            'mac': self.mac,
            'ip': self.ip,
            'status': self.status
        }
    
    def check_status(self, timeout=1, port=80):
        """检查设备在线状态"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((self.ip, port))
            sock.close()
            self.status = (result == 0)
            return self.status
        except:
            self.status = False
            return False
    
    @staticmethod
    def is_valid_mac(mac):
        """验证MAC地址格式"""
        return bool(re.match(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', mac))
    
    @staticmethod
    def is_valid_ip(ip):
        """验证IP地址格式"""
        if not re.match(r'^(\d{1,3}\.){3}\d{1,3}$', ip):
            return False
        return all(0 <= int(num) <= 255 for num in ip.split('.'))
