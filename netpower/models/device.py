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
        """验证MAC地址格式
        
        支持多种格式的MAC地址:
        - 带冒号分隔: AA:BB:CC:DD:EE:FF
        - 带连字符分隔: AA-BB-CC-DD-EE-FF
        - 带点分隔: AABB.CCDD.EEFF
        - 无分隔符: AABBCCDDEEFF
        
        返回:
            bool: MAC地址格式是否有效
        """
        # 去除前后空白字符
        mac = mac.strip() if mac else ""
        
        # 各种MAC地址格式的正则表达式
        patterns = [
            r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$',           # AA:BB:CC:DD:EE:FF 或 AA-BB-CC-DD-EE-FF
            r'^([0-9A-Fa-f]{4}\.){2}([0-9A-Fa-f]{4})$',             # AABB.CCDD.EEFF
            r'^([0-9A-Fa-f]{12})$'                                  # AABBCCDDEEFF
        ]
        
        # 检查是否符合任一格式
        for pattern in patterns:
            if re.match(pattern, mac):
                return True
                
        return False
    
    @staticmethod
    def is_valid_ip(ip):
        """验证IP地址格式"""
        if not re.match(r'^(\d{1,3}\.){3}\d{1,3}$', ip):
            return False
        return all(0 <= int(num) <= 255 for num in ip.split('.'))
