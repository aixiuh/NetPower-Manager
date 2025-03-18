#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

class Config:
    """应用配置"""
    # 基本配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'wake-on-lan-secret-key'
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    PARENT_DIR = os.path.dirname(BASE_DIR)
    
    # 数据文件路径
    DATA_FILE = os.path.join(PARENT_DIR, 'data', 'devices.json')
    
    # 扫描设置
    PING_TIMEOUT = 1  # 设备在线检测超时时间(秒)
    PING_PORT = 80    # 检测设备在线状态使用的端口
    
    # 日志配置
    LOG_LEVEL = logging.DEBUG
    LOG_FILE = os.path.join(PARENT_DIR, 'logs', 'app.log')
    LOG_FORMAT = '%(asctime)s [%(levelname)s] in %(module)s: %(message)s'
