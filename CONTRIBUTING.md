# 贡献指南

感谢您考虑为Wake on LAN网络管理工具做出贡献！以下是一些有助于简化贡献过程的指南。

## 开发环境设置

1. 克隆仓库
   ```bash
   git clone https://github.com/yourusername/Wake-on-Lan-Webinterface.git
   cd Wake-on-Lan-Webinterface
   ```

2. 创建虚拟环境
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```

4. 运行应用
   ```bash
   python run.py
   ```

## 代码规范

- 遵循[PEP 8](https://www.python.org/dev/peps/pep-0008/)编码风格
- 使用有意义的变量名和函数名
- 为新功能添加适当的文档字符串
- 保持代码简洁明了

## 提交PR流程

1. 创建新分支进行开发
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. 进行更改并提交
   ```bash
   git add .
   git commit -m "添加了新功能：xxx"
   ```

3. 推送到您的fork并创建Pull Request
   ```bash
   git push origin feature/your-feature-name
   ```

4. 在GitHub上创建Pull Request，描述您的更改和改进

## 报告问题

如果您发现bug或有改进建议，请在GitHub issues中提出。请提供：

- 问题的详细描述
- 复现步骤
- 预期行为和实际行为
- 截图（如适用）
- 您的环境信息（操作系统、浏览器等）

感谢您的贡献！
