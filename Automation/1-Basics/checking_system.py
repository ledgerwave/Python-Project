"""
Checking system info
"""

import shutil
import psutil


def check_disk_usage(disk):
    """
    Checks disk usage
    """
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_cpu_usage():
    """
    Checks cpu usage
    """
    usage = psutil.cpu_percent(1)
    return usage < 75


def main():
    """
    Main function
    """
    if not check_disk_usage("/") or not check_cpu_usage():
        print("Low memory and cpu usage!")
    else:
        print("Everything is OK!")


if __name__ == "__main__":
    main()
