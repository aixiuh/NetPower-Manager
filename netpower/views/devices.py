#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, redirect, url_for, flash
from netpower.services.device_service import DeviceService
from netpower.services.power_service import PowerService
from functools import wraps

device_bp = Blueprint('devices', __name__)

def handle_errors(f):
    """错误处理装饰器"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            flash(f"操作失败: {str(e)}", "error")
            return redirect(url_for('devices.index'))
    return decorated_function

@device_bp.route('/')
def index():
    """主页视图"""
    devices = DeviceService.get_devices()
    return render_template('devices/index.html', devices=devices)

@device_bp.route('/wake_up/<int:device_id>')
@handle_errors
def wake_up(device_id):
    """唤醒设备"""
    success, message = PowerService.wake_device(device_id)
    flash(message, "success" if success else "error")
    return redirect(url_for('devices.index'))

@device_bp.route('/add_device', methods=['POST'])
@handle_errors
def add_device():
    """添加设备"""
    name = request.form.get('name', '')
    mac = request.form.get('mac', '')
    ip = request.form.get('ip', '')
    
    success, message = DeviceService.add_device(name, mac, ip)
    flash(message, "success" if success else "error")
    return redirect(url_for('devices.index'))

@device_bp.route('/edit_device/<int:device_id>')
@handle_errors
def edit_device_page(device_id):
    """编辑设备页面"""
    devices = DeviceService.get_devices()
    if 0 <= device_id < len(devices):
        return render_template('devices/edit.html', device=devices[device_id], device_id=device_id)
    
    flash("设备不存在", "error")
    return redirect(url_for('devices.index'))

@device_bp.route('/update_device/<int:device_id>', methods=['POST'])
@handle_errors
def update_device(device_id):
    """更新设备"""
    name = request.form.get('name', '')
    mac = request.form.get('mac', '')
    ip = request.form.get('ip', '')
    
    success, message = DeviceService.update_device(device_id, name, mac, ip)
    flash(message, "success" if success else "error")
    return redirect(url_for('devices.index'))

@device_bp.route('/delete_device/<int:device_id>')
@handle_errors
def delete_device(device_id):
    """删除设备"""
    success, message = DeviceService.delete_device(device_id)
    flash(message, "success" if success else "error")
    return redirect(url_for('devices.index'))

@device_bp.route('/refresh_status')
@handle_errors
def refresh_status():
    """刷新设备状态"""
    DeviceService.refresh_status()
    flash("设备状态已刷新", "success")
    return redirect(url_for('devices.index'))
