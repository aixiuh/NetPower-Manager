# Wake on LAN 网络管理工具

这是一个基于Flask构建的简洁而功能强大的Web应用程序，允许您管理局域网中设备的电源状态。您可以轻松地远程唤醒（Wake-on-LAN）网络设备，并监控它们的在线状态。

## 当前功能

- **设备管理：** 添加、编辑、删除和查看局域网中的设备
- **远程唤醒：** 使用Wake-on-LAN协议唤醒局域网内的设备
- **状态监控：** 检查设备的在线/离线状态
- **批量操作：** 同时唤醒或删除多个设备

## 规划中的功能

- **远程关机：** 通过SSH远程关闭设备
- **设备分组：** 对设备进行分类管理
- **定时任务：** 设置定时唤醒和关机任务
- **用户认证：** 增加登录系统，保护管理界面安全
- **设备监控：** 更详细的设备状态监控

## 开始使用

按照以下步骤设置和运行Wake on LAN工具：

1. **克隆仓库：**
   ```bash
   git clone https://github.com/yourusername/Wake-on-Lan-Webinterface.git
   cd Wake-on-Lan-Webinterface
   ```

2. **安装依赖项：**
   ```bash
   pip install -r requirements.txt
   ```

3. **运行应用程序：**
   ```bash
   python run.py
   ```

4. **访问应用：**
   在浏览器中打开 `http://localhost:5000` 即可使用

## 使用方法

1. **添加设备：**
   - 在界面顶部的"添加设备"部分输入设备信息
   - 填写设备名称、MAC地址、IP地址，然后点击"添加设备"

2. **唤醒设备：**
   - 在设备列表中找到要唤醒的设备
   - 点击"唤醒"按钮发送Wake-on-LAN魔术包
   - 也可以选择多个设备，然后使用"唤醒选中"进行批量唤醒

3. **编辑/删除设备：**
   - 使用设备列表中的"编辑"按钮修改设备信息
   - 使用"删除"按钮从列表中移除设备
   - 也可以选择多个设备，然后使用"删除选中"进行批量删除

4. **查看设备状态：**
   - 设备列表显示每个设备的当前在线/离线状态
   - 使用"刷新状态"按钮更新所有设备状态

## 配置
应用程序将设备信息存储在`data/devices.json`文件中。该文件会自动创建和管理。

## 项目结构
```
netpower-manager/
├── app/
│   ├── controllers/
│   │   └── device_controller.py
│   ├── models/
│   │   └── device.py
│   ├── services/
│   │   ├── power_service.py
│   │   └── status_service.py
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── edit_device.html
│   └── __init__.py
├── config/
│   ├── devices.json
│   └── config.py
├── run.py
└── README.md
```

## 贡献
欢迎贡献该项目。无论是修复bug、改进文档，还是添加新功能，您的贡献都将受到欢迎。

## 许可证
该项目根据MIT许可证授权。


