import threading
import time


def worker(event):
    print(event)
    event.wait()
    for _ in range(5):
        print("Working...")
        time.sleep(1)
    print("Done")


def main():
    event = threading.Event()
    thread = threading.Thread(target=worker, args=(event,))
    thread.start()
    time.sleep(2)
    event.set()
    thread.join()
    print("Main thread exiting...")
if __name__ == "__main__":
    main()