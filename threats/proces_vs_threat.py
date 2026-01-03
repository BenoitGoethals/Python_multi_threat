import multiprocessing
import threading
import time
import os

def cpu_intensive_task(n):
    """A CPU-intensive task for demonstration"""
    result = 0
    for i in range(n):
        result += i * i
    return result

def io_intensive_task(duration):
    """An I/O-intensive task (simulated with sleep)"""
    time.sleep(duration)
    return f"Task completed after {duration} seconds"

# Function to run with multiprocessing
def process_worker(task_id, n):
    start_time = time.time()
    result = cpu_intensive_task(n)
    end_time = time.time()
    print(f"Process {task_id} (PID: {os.getpid()}) completed in {end_time - start_time:.2f} seconds")
    return result

# Function to run with threading
def thread_worker(task_id, duration):
    start_time = time.time()
    result = io_intensive_task(duration)
    end_time = time.time()
    print(f"Thread {task_id} completed in {end_time - start_time:.2f} seconds")
    return result

# Demonstrate threading for I/O-bound tasks
print("=== Threading Example (I/O-bound) ===")
start_time = time.time()

threads = []
for i in range(3):
    thread = threading.Thread(target=thread_worker, args=(i, 1))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Total time with threading: {time.time() - start_time:.2f} seconds")