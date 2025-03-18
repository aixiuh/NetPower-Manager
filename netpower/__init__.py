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
    
    # 确保数据和日志目录存在
    for directory in [os.path.dirname(app.config['DATA_FILE']), 
                     os.path.dirname(app.config['LOG_FILE'])]:
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    # 设置日志
    handler = RotatingFileHandler(
        app.config['LOG_FILE'], 
        maxBytes=10485760,
        backupCount=5
    )
    handler.setFormatter(logging.Formatter(app.config['LOG_FORMAT']))
    handler.setLevel(app.config['LOG_LEVEL'])
    
    app.logger.addHandler(handler)
    app.logger.setLevel(app.config['LOG_LEVEL'])
    
    # 注册蓝图
    from netpower.views.devices import device_bp
    from netpower.views.errors import error_bp, page_not_found, internal_server_error
    
    app.register_blueprint(device_bp)
    app.register_blueprint(error_bp)
    
    # 设置错误处理
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)
    
    return app
