import subprocess
import sys

def open_firewall_port(port, protocol="TCP", rule_name="PythonAppPort"):
    """
    在Windows防火墙中开放指定端口
    参数：
        port: 要开放的端口号 (int)
        protocol: 协议类型 (TCP/UDP)
        rule_name: 防火墙规则名称
    """
    try:
        # 验证管理员权限
        if not is_admin():
            print("错误：需要以管理员身份运行此脚本！")
            sys.exit(1)

        # 验证端口有效性
        if not 1 <= port <= 65535:
            raise ValueError("端口号必须在1-65535之间")

        # 构建命令
        command = f'netsh advfirewall firewall add rule name="{rule_name}" dir=in action=allow protocol={protocol} localport={port}'

        # 执行命令
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"成功开放 {protocol} 端口 {port}")
            print(f"可能需要重启相关应用程序或服务")
        else:
            print(f"操作失败：{result.stderr}")

    except Exception as e:
        print(f"发生错误：{str(e)}")

def is_admin():
    """检查是否以管理员权限运行"""
    try:
        return subprocess.check_output("net session", shell=True, stderr=subprocess.DEVNULL)
    except Exception:
        return False

if __name__ == "__main__":
    try:
        port = int(input("请输入要开放的端口号 (1-65535): "))
        protocol = input("选择协议类型 (TCP/UDP，默认TCP): ").upper() or "TCP"
        
        if protocol not in ["TCP", "UDP"]:
            raise ValueError("协议类型必须是TCP或UDP")

        open_firewall_port(port, protocol)
        
    except ValueError as ve:
        print(f"输入错误: {str(ve)}")
    except KeyboardInterrupt:
        print("\n操作已取消")