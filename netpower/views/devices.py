#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from netpower.services.device_service import DeviceService
from netpower.services.power_service import PowerService

# 创建蓝图
device_bp = Blueprint('devices', __name__)

@device_bp.route('/')
def index():
    """主页视图"""
    # 加载设备并刷新状态
    devices = DeviceService.load_devices()
    devices = DeviceService.refresh_status(devices)
    return render_template('devices/index.html', devices=devices)

@device_bp.route('/wake_up/<int:device_id>')
def wake_up(device_id):
    """唤醒设备"""
    success, message = PowerService.wake_device(device_id)
    if success:
        flash(message, "success")
    else:
        flash(message, "error")
    return redirect(url_for('devices.index'))

@device_bp.route('/wake_all', methods=['POST'])
def wake_all():
    """批量唤醒设备"""
    selected_ids = request.form.getlist('selected_devices')
    if not selected_ids:
        flash("未选择任何设备", "error")
        return redirect(url_for('devices.index'))
    
    # 转换为整数列表
    device_ids = [int(id) for id in selected_ids if id.isdigit()]
    success, message = PowerService.wake_multiple_devices(device_ids)
    
    if success:
        flash(message, "success")
    else:
        flash(message, "error")
    
    return redirect(url_for('devices.index'))

@device_bp.route('/add_device', methods=['POST'])
def add_device():
    """添加设备"""
    name = request.form.get('name', '')
    mac = request.form.get('mac', '')
    ip = request.form.get('ip', '')
    
    success, message = DeviceService.add_device(name, mac, ip)
    if success:
        flash(message, "success")
    else:
        flash(message, "error")
    
    return redirect(url_for('devices.index'))

@device_bp.route('/edit_device/<int:device_id>')
def edit_device_page(device_id):
    """编辑设备页面"""
    devices = DeviceService.load_devices()
    if 0 <= device_id < len(devices):
        return render_template('devices/edit.html', device=devices[device_id], device_id=device_id)
    
    flash("设备不存在", "error")
    return redirect(url_for('devices.index'))

@device_bp.route('/update_device/<int:device_id>', methods=['POST'])
def update_device(device_id):
    """更新设备"""
    name = request.form.get('name', '')
    mac = request.form.get('mac', '')
    ip = request.form.get('ip', '')
    
    success, message = DeviceService.update_device(device_id, name, mac, ip)
    if success:
        flash(message, "success")
    else:
        flash(message, "error")
    
    return redirect(url_for('devices.index'))

@device_bp.route('/delete_device/<int:device_id>')
def delete_device(device_id):
    """删除设备"""
    success, message = DeviceService.delete_device(device_id)
    if success:
        flash(message, "success")
    else:
        flash(message, "error")
    
    return redirect(url_for('devices.index'))

@device_bp.route('/delete_selected', methods=['POST'])
def delete_selected():
    """批量删除设备"""
    selected_ids = request.form.getlist('selected_devices')
    if not selected_ids:
        flash("未选择任何设备", "error")
        return redirect(url_for('devices.index'))
    
    # 转换为整数列表
    device_ids = [int(id) for id in selected_ids if id.isdigit()]
    success, message = DeviceService.delete_multiple_devices(device_ids)
    
    if success:
        flash(message, "success")
    else:
        flash(message, "error")
    
    return redirect(url_for('devices.index'))

@device_bp.route('/refresh_status')
def refresh_status():
    """刷新设备状态"""
    devices = DeviceService.load_devices()
    DeviceService.refresh_status(devices)
    flash("设备状态已刷新", "success")
    return redirect(url_for('devices.index'))
