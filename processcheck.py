import psutil
import typing

def list_running_processes_with_cpu( plist: tuple[str] ):
    """Lists all running processes on the system, including CPU utilization."""
    for i in range(2):
        print(f"{i} ========")
        for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent']):

            if i == 0 or proc.info['name'] not in plist:   continue                         
            cpu_usage = proc.info['cpu_percent'] 
            print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}, User: {proc.info['username']}, CPU Usage: {cpu_usage}%")

if __name__ == "__main__":

    

    list_running_processes_with_cpu(("chrome.exe",))




