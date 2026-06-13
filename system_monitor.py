#!/usr/bin/env python3

import os
import sys
import time
from datetime import datetime

import psutil

ANSI_RESET = "\033[0m"
ANSI_CYAN = "\033[1;36m"
ANSI_GREEN = "\033[1;32m"
ANSI_YELLOW = "\033[1;33m"
ANSI_GRAY = "\033[1;90m"
BAR_WIDTH = 30
REFRESH_INTERVAL = 2
TOP_PROCESS_COUNT = 5


def get_cpu_usage() -> float:
    return psutil.cpu_percent(interval=0.5)


def get_memory_usage() -> dict:
    mem = psutil.virtual_memory()
    return {
        "total": mem.total / (1024 ** 3),
        "used": mem.used / (1024 ** 3),
        "percent": mem.percent,
    }


def get_disk_usage(path: str = "/") -> dict:
    disk = psutil.disk_usage(path)
    return {
        "total": disk.total / (1024 ** 3),
        "used": disk.used / (1024 ** 3),
        "percent": disk.percent,
    }


def get_top_processes(n: int = TOP_PROCESS_COUNT) -> list:
    processes = []
    for proc in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
        try:
            info = proc.info
            if info["cpu_percent"] is not None:
                processes.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    processes.sort(key=lambda x: x["cpu_percent"] or 0, reverse=True)
    return processes[:n]


def format_size(gb: float) -> str:
    return f"{gb:.2f} GB"


def progress_bar(percent: float, width: int = BAR_WIDTH) -> str:
    filled = int(width * percent / 100)
    bar = "\u2588" * filled + "\u2591" * (width - filled)
    return f"[{bar}] {percent:.1f}%"


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def render_frame() -> None:
    cpu = get_cpu_usage()
    mem = get_memory_usage()
    disk = get_disk_usage()
    procs = get_top_processes()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = [
        f"{ANSI_CYAN}\u2554{'=' * 60}\u2557{ANSI_RESET}",
        f"{ANSI_CYAN}\u2551{'SYSTEM MONITOR':^60}\u2551{ANSI_RESET}",
        f"{ANSI_CYAN}\u255a{'=' * 60}\u255d{ANSI_RESET}",
        f"{ANSI_YELLOW}  Time: {now}{ANSI_RESET}",
        "",
        f"{ANSI_GREEN}  CPU Usage:{ANSI_RESET} {progress_bar(cpu)}",
        "",
        f"{ANSI_GREEN}  Memory Usage:{ANSI_RESET} {progress_bar(mem['percent'])}",
        f"    Used: {format_size(mem['used'])} / {format_size(mem['total'])}",
        "",
        f"{ANSI_GREEN}  Disk Usage (/):{ANSI_RESET} {progress_bar(disk['percent'])}",
        f"    Used: {format_size(disk['used'])} / {format_size(disk['total'])}",
        "",
        f"{ANSI_CYAN}  {'-' * 58}{ANSI_RESET}",
        f"{ANSI_CYAN}  Top {TOP_PROCESS_COUNT} Processes by CPU Usage:{ANSI_RESET}",
        f"{ANSI_CYAN}  {'-' * 58}{ANSI_RESET}",
        f"  {'PID':<10} {'Name':<30} {'CPU%':<10} {'RAM%':<10}",
        f"  {'-' * 10} {'-' * 30} {'-' * 10} {'-' * 10}",
    ]

    for p in procs:
        name = (p["name"] or "")[:30]
        cpu_val = p["cpu_percent"] or 0
        ram_val = p["memory_percent"] or 0
        lines.append(f"  {p['pid']:<10} {name:<30} {cpu_val:<10.1f} {ram_val:<10.1f}")

    lines.append("")
    lines.append(f"{ANSI_GRAY}  Press Ctrl+C to exit{ANSI_RESET}")

    clear_screen()
    print("\n".join(lines))


def main() -> None:
    try:
        while True:
            render_frame()
            time.sleep(REFRESH_INTERVAL)
    except KeyboardInterrupt:
        print(f"\n{ANSI_YELLOW}\n  Monitor stopped. Goodbye!{ANSI_RESET}\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
