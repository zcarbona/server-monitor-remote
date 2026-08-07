# 🖥️ Server Health Check Report Generator

A lightweight Python script that collects key system health metrics and generates a formatted server status report.

This project is designed as a simple Linux server monitoring tool using Python and the `psutil` library. It gathers information about the operating system, hardware resources, storage, and network configuration, then exports everything into a readable text report.

---

## ✨ Features

- 📌 Collects system information
  - Hostname
  - Current user
  - Timestamp
  - Operating system
  - Kernel version

- ⚙️ Monitors CPU usage

- 🧠 Memory statistics
  - Total memory
  - Used memory
  - Free memory
  - Memory utilization percentage

- 💾 Disk usage
  - Used disk space
  - Free disk space
  - Disk utilization percentage

- 🌐 Network information
  - IP address
  - System uptime

- 📄 Automatically generates a report inside the `reports/` directory

---

## 📂 Project Structure

```
server-health-check/
│
├── reports/
│   └── server_report.txt
│
├── monitor.py
├── requirements.txt
└── README.md
```

---

## 🛠 Requirements

- Python 3.8+
- Linux (recommended)

Install dependencies:

```bash
pip install -r requirements.txt
```

or

```bash
pip install psutil
```

---

## ▶️ Usage

Run the script:

```bash
python monitor.py
```

After execution, the report will be generated at:

```
reports/server_report.txt
```

---

## 📄 Example Output

```
SERVER HEALTH CHECK

Hostname: archlinux
Current User: carbona
Timestamp: 2026-08-07 03:30:15
Operating System: Linux
Kernel Version: 6.16.0-arch1-1

CPU Usage: 12.4%

Total Memory: 15.32 GB
Used Memory: 6.41 GB
Free Memory: 8.91 GB
Used Memory Percentage: 41.84%

Used Disk Space: 58.12 GB
Free Disk Space: 173.44 GB
Used Disk Space Percentage: 25.09%

IP Address: 192.168.1.12
System Uptime: up 3 hours, 18 minutes
```

---

## 📚 Technologies Used

- Python
- psutil
- os
- platform
- socket
- subprocess
- datetime

---

## 🚀 Future Improvements

- Export reports as JSON and CSV
- Add email notifications
- Monitor multiple disks
- Display network interface statistics
- Monitor running services
- Log historical reports
- Add CPU temperature monitoring
- Build a web dashboard with Flask/FastAPI
- Schedule automatic execution with cron

---

## 🎯 Learning Objectives

This project demonstrates practical experience with:

- Python scripting
- Linux system administration
- System resource monitoring
- File handling
- Process automation
- Working with third-party Python libraries
- Report generation

---

## 📜 License

This project is licensed under the MIT License.

---

## 👤 Author

**Ali Mohamed Reda**

Computer Science Student • DevOps & Cybersecurity Enthusiast
