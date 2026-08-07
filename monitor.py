import os
import psutil
import platform
import subprocess
from socket import socket
from datetime import datetime


#safty check for reports directory
os.makedirs("reports", exist_ok=True)
report_path = "reports/server_report.txt"



#system information
hostname = platform.node()
current_user = os.getlogin()
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
Operating_system = platform.system()
kernel_version = platform.release()

#hardware information
cpu_usage = psutil.cpu_percent(interval=1)
total_memory = psutil.virtual_memory().total / (1024. ** 3)
used_memory = psutil.virtual_memory().used / (1024. ** 3)
free_memory = psutil.virtual_memory().free / (1024. ** 3)
used_memory_percentage = (used_memory / total_memory) * 100

file_system = os.statvfs('/')
used_disk_space = (file_system.f_blocks - file_system.f_bfree) * file_system.f_frsize / (1024. ** 3)
free_disk_space = file_system.f_bfree * file_system.f_frsize / (1024. ** 3)
Used_disk_space_percentage = (used_disk_space / (used_disk_space + free_disk_space)) * 100


#network information
ip_address = ip_address = socket.gethostbyname(socket.gethostname())
system_uptime = subprocess.getoutput("uptime -p").strip()


#report generation
with open(report_path, "w") as f:
    f.write("SERVER HEALTH CHECK\n")
    f.write(f"Hostname: {hostname}\n")
    f.write(f"Current User: {current_user}\n")
    f.write(f"Timestamp: {timestamp}\n")
    f.write(f"Operating System: {Operating_system}\n")
    f.write(f"Kernel Version: {kernel_version}\n")
    f.write(f"CPU Usage: {cpu_usage}\n")
    f.write(f"Total Memory: {total_memory:.2f} GB\n")
    f.write(f"Used Memory: {used_memory:.2f} GB\n")
    f.write(f"Free Memory: {free_memory:.2f} GB\n")
    f.write(f"Used Memory Percentage: {used_memory_percentage:.2f}%\n")
    f.write(f"Used Disk Space: {used_disk_space:.2f} GB\n")
    f.write(f"Free Disk Space: {free_disk_space:.2f} GB\n")
    f.write(f"Used Disk Space Percentage: {Used_disk_space_percentage:.2f}%\n")
    f.write(f"IP Address: {ip_address}\n")
    f.write(f"System Uptime: {system_uptime}\n")