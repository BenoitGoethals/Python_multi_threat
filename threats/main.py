# This is a sample Python script.
import threading
import time


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def worker_function(name, delay):
    """A simple worker function that simulates some work"""
    print(f"Thread {name} starting...")
    time.sleep(delay)
    print(f"Thread {name} finished after {delay} seconds")

def print_hi(name):
    import psutil
    import os
    import time

    # Get current process information
    current_process = psutil.Process()

    print(f"Process ID (PID): {current_process.pid}")
    print(f"Process Name: {current_process.name()}")
    print(f"Parent Process ID: {current_process.ppid()}")
    print(f"Memory Info: {current_process.memory_info()}")
    print(f"CPU Usage: {current_process.cpu_percent()}%")

    # Get all running processes
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        try:
            processes.append(proc.info)
        except psutil.NoSuchProcess:
            pass

    # Sort by memory usage and show top 5
    top_processes = sorted(processes, key=lambda x: x['memory_percent'], reverse=True)[:5]

    print("Top 5 processes by memory usage:")
    for proc in top_processes:
        print(f"PID: {proc['pid']:<6} Name: {proc['name']:<20} Memory: {proc['memory_percent']:.1f}%")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    main_thread = threading.current_thread()
    print(f"Main thread name: {main_thread.name}")
    print(f"Main thread ID: {main_thread.ident}")
    print(f"Active thread count: {threading.active_count()}")
    # Create some threads
    threads = []
    for i in range(3):
        thread = threading.Thread(
            target=worker_function,
            args=(f"Worker-{i}", i + 1),
            name=f"WorkerThread-{i}"
        )
        threads.append(thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All threads completed!")
