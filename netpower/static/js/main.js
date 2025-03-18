/**
 * 主JavaScript文件
 */

// 确认删除操作
function confirmAction(message, callback) {
    if (confirm(message)) {
        callback();
    }
}

// 验证MAC地址格式
function isValidMac(mac) {
    return /^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$/.test(mac);
}

// 验证IP地址格式
function isValidIp(ip) {
    if (!/^(\d{1,3}\.){3}\d{1,3}$/.test(ip)) {
        return false;
    }
    
    const parts = ip.split('.');
    for (let part of parts) {
        const num = parseInt(part, 10);
        if (isNaN(num) || num < 0 || num > 255) {
            return false;
        }
    }
    return true;
}

// 设置闪现消息自动关闭
function setupFlashMessages(timeout = 5000) {
    setTimeout(function() {
        document.querySelectorAll('.flash-message').forEach(message => {
            message.style.display = 'none';
        });
    }, timeout);
}

// DOM加载完成后执行
document.addEventListener('DOMContentLoaded', function() {
    setupFlashMessages();
    setupFormValidation();
});

// 设置表单验证
function setupFormValidation() {
    document.querySelectorAll('form[data-validate="true"]').forEach(form => {
        form.addEventListener('submit', function(event) {
            const macInput = this.querySelector('input[name="mac"]');
            if (macInput && !isValidMac(macInput.value)) {
                alert('MAC地址格式无效。请使用格式：00:11:22:33:44:55');
                event.preventDefault();
                return;
            }
            
            const ipInput = this.querySelector('input[name="ip"]');
            if (ipInput && !isValidIp(ipInput.value)) {
                alert('IP地址格式无效或范围错误。请使用格式：192.168.1.100');
                event.preventDefault();
                return;
            }
        });
    });
}
