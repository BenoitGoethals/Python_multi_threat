import psutil
import threading
import time
from datetime import datetime


class SystemMonitor:
    def __init__(self):
        self.monitoring = False
        self.stats = []

    def collect_stats(self):
        """Collect system statistics"""
        while self.monitoring:
            stats = {
                'timestamp': datetime.now().strftime('%H:%M:%S'),
                'cpu_percent': psutil.cpu_percent(interval=1),
                'memory_percent': psutil.virtual_memory().percent,
                'disk_usage': psutil.disk_usage('/').percent if hasattr(psutil, 'disk_usage') else 0,
                'process_count': len(psutil.pids())
            }
            self.stats.append(stats)
            time.sleep(1)

    def start_monitoring(self, duration=5):
        """Start monitoring for specified duration"""
        self.monitoring = True
        self.stats = []

        # Start monitoring thread
        monitor_thread = threading.Thread(target=self.collect_stats)
        monitor_thread.daemon = True
        monitor_thread.start()

        # Let it run for specified duration
        time.sleep(duration)
        self.monitoring = False

        # Wait for thread to finish
        monitor_thread.join()

        return self.stats

    def display_stats(self):
        """Display collected statistics"""
        if not self.stats:
            print("No statistics collected")
            return

        print("System Statistics:")
        print("Time     | CPU%  | Memory% | Processes")
        print("-" * 40)
        for stat in self.stats:
            print(
                f"{stat['timestamp']} | {stat['cpu_percent']:5.1f} | {stat['memory_percent']:7.1f} | {stat['process_count']:9d}")


# Use the system monitor
monitor = SystemMonitor()
print("Starting system monitoring for 5 seconds...")
monitor.start_monitoring(5)
monitor.display_stats()