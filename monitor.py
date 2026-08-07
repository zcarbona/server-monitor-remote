import os
import psutil
import platform
import subprocess
from socket import socket, gethostname, gethostbyname
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
try:
    ip_address = socket.gethostbyname(socket.gethostname())
except Exception:
    ip_address = "N/A"


system_uptime = subprocess.getoutput("uptime -p").strip()


#report generation
with open(report_path, "w") as f:
    f.write("=" * 50 + "\n")
    f.write("           SERVER HEALTH REPORT\n")
    f.write("=" * 50 + "\n\n")

    f.write("[ SYSTEM INFORMATION ]\n")
    f.write("-" * 50 + "\n")
    f.write(f"{'Hostname':<25}: {hostname}\n")
    f.write(f"{'Current User':<25}: {current_user}\n")
    f.write(f"{'Timestamp':<25}: {timestamp}\n")
    f.write(f"{'Operating System':<25}: {Operating_system}\n")
    f.write(f"{'Kernel Version':<25}: {kernel_version}\n\n")

    f.write("[ CPU & MEMORY ]\n")
    f.write("-" * 50 + "\n")
    f.write(f"{'CPU Load Average':<25}: {cpu_usage}\n")
    f.write(f"{'Total Memory':<25}: {total_memory:.2f} GB\n")
    f.write(f"{'Used Memory':<25}: {used_memory:.2f} GB\n")
    f.write(f"{'Free Memory':<25}: {free_memory:.2f} GB\n")
    f.write(f"{'Memory Usage':<25}: {used_memory_percentage:.2f}%\n\n")

    f.write("[ STORAGE ]\n")
    f.write("-" * 50 + "\n")
    f.write(f"{'Used Disk Space':<25}: {used_disk_space:.2f} GB\n")
    f.write(f"{'Free Disk Space':<25}: {free_disk_space:.2f} GB\n")
    f.write(f"{'Disk Usage':<25}: {Used_disk_space_percentage:.2f}%\n\n")

    f.write("[ NETWORK ]\n")
    f.write("-" * 50 + "\n")
    f.write(f"{'IP Address':<25}: {ip_address}\n")
    f.write(f"{'System Uptime':<25}: {system_uptime}\n\n")

    f.write("=" * 50 + "\n")
    f.write("End of Report\n")
    f.write("=" * 50 + "\n")