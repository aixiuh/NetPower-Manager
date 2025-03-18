#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask

def create_app(config_name=None):
    """创建Flask应用实例"""
    app = Flask(__name__)
    
    # 加载配置
    from netpower.config import Config
    app.config.from_object(Config)
    
    # 设置日志
    configure_logging(app)
    
    # 确保数据目录存在
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # 确保日志目录存在
    log_dir = os.path.dirname(app.config['LOG_FILE'])
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # 注册蓝图
    from netpower.views.devices import device_bp
    from netpower.views.errors import error_bp
    
    app.register_blueprint(device_bp)
    app.register_blueprint(error_bp)
    
    # 设置错误处理
    from netpower.views.errors import page_not_found, internal_server_error
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)
    
    return app

def configure_logging(app):
    """配置应用日志"""
    handler = RotatingFileHandler(
        app.config['LOG_FILE'], 
        maxBytes=10485760,  # 10MB
        backupCount=5
    )
    handler.setFormatter(logging.Formatter(app.config['LOG_FORMAT']))
    handler.setLevel(app.config['LOG_LEVEL'])
    
    app.logger.addHandler(handler)
    app.logger.setLevel(app.config['LOG_LEVEL'])
    
    # 移除默认处理器，避免重复日志
    if app.debug:
        for handler in app.logger.handlers:
            app.logger.removeHandler(handler)
        app.logger.addHandler(handler)
