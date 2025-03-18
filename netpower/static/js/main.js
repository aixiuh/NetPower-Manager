/**
 * 主JavaScript文件
 */

// 工具函数
const utils = {
    // 确认操作
    confirmAction(message, callback) {
        if (confirm(message)) callback();
    },
    
    // 验证MAC地址格式
    isValidMac(mac) {
        return /^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$/.test(mac);
    },
    
    // 验证IP地址格式
    isValidIp(ip) {
        if (!/^(\d{1,3}\.){3}\d{1,3}$/.test(ip)) return false;
        
        return ip.split('.')
            .map(part => parseInt(part, 10))
            .every(num => !isNaN(num) && num >= 0 && num <= 255);
    }
};

// 页面功能
const app = {
    // 设置闪现消息自动关闭
    setupFlashMessages(timeout = 5000) {
        setTimeout(() => {
            document.querySelectorAll('.flash-message').forEach(message => {
                message.style.display = 'none';
            });
        }, timeout);
    },
    
    // 设置表单验证
    setupFormValidation() {
        document.querySelectorAll('form[data-validate="true"]').forEach(form => {
            form.addEventListener('submit', function(event) {
                const macInput = this.querySelector('input[name="mac"]');
                if (macInput && !utils.isValidMac(macInput.value)) {
                    alert('MAC地址格式无效。请使用格式：00:11:22:33:44:55');
                    event.preventDefault();
                    return;
                }
                
                const ipInput = this.querySelector('input[name="ip"]');
                if (ipInput && !utils.isValidIp(ipInput.value)) {
                    alert('IP地址格式无效或范围错误。请使用格式：192.168.1.100');
                    event.preventDefault();
                    return;
                }
            });
        });
    },
    
    // 初始化页面
    init() {
        this.setupFlashMessages();
        this.setupFormValidation();
    }
};

// DOM加载完成后执行
document.addEventListener('DOMContentLoaded', () => app.init());
