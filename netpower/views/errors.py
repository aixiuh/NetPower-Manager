#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

# 创建蓝图
error_bp = Blueprint('errors', __name__)

@error_bp.app_errorhandler(404)
def page_not_found(e):
    """404错误处理"""
    return render_template('errors/404.html'), 404

@error_bp.app_errorhandler(500)
def internal_server_error(e):
    """500错误处理"""
    return render_template('errors/500.html'), 500
