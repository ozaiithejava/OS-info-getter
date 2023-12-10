import platform
import os
import socket

def get_system_info():
    system_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Python Version": platform.python_version(),
        "IP Address": get_ip_address(),
        "Current Directory": os.getcwd(),
        "CPU Cores": os.cpu_count(),
        "Memory Info": get_memory_info(),
    }

    return system_info

def get_ip_address():
    try:
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        return ip_address
    except socket.error as e:
        return str(e)

def get_memory_info():
    try:
        mem_info = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
        return f"{mem_info / (1024. ** 3):.2f} GB"
    except AttributeError:
        return "Memory info not available"

if __name__ == "__main__":
    system_info = get_system_info()

    for key, value in system_info.items():
        print(f"{key}: {value}")
