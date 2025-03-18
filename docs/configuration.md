# 配置指南

本文档详细介绍了Wake on LAN网络管理工具的配置选项。

## 基本配置

应用程序的主要配置在`netpower/config.py`文件中。您可以修改以下设置：

### 安全配置
- `SECRET_KEY`: 用于会话安全的密钥。在生产环境中，请设置为复杂的随机值。

### 设备状态检测
- `PING_TIMEOUT`: 检测设备在线状态的超时时间（秒）
- `PING_PORT`: 用于检测设备在线状态的TCP端口

## 环境变量

您可以使用以下环境变量覆盖默认配置：

- `SECRET_KEY`: 覆盖默认的密钥
- `DATA_FILE`: 设置设备数据文件的自定义路径

示例：
```bash
export SECRET_KEY="your-very-secure-key"
export DATA_FILE="/path/to/custom/devices.json"
```

## 开发/生产模式

默认情况下，应用程序以开发模式运行。在生产环境中，请执行以下操作：

1. 设置安全的`SECRET_KEY`
2. 关闭调试模式，修改`run.py`：
   ```python
   app.run(debug=False, host='0.0.0.0')
   ```

## 数据文件格式

设备数据存储在JSON文件中，格式如下：

```json
[
  {
    "name": "设备名称",
    "mac": "MAC地址",
    "ip": "IP地址",
    "status": false
  }
]
```

- `name`: 设备的显示名称
- `mac`: 设备的MAC地址，格式为xx:xx:xx:xx:xx:xx
- `ip`: 设备的IP地址
- `status`: 设备的当前状态（在线/离线）
