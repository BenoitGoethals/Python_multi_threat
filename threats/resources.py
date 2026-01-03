import os
import requests
import multiprocessing

urls = {
    "hln": "https://hln.be",
    "fet": "https://www.routen.be/turfput-wandelroute",
}


def scrape_url(name, url):
    """
    Worker function to fetch a URL and save its content to an HTML file.
    """
    print(f"Process {os.getpid()} starting: Scraping {name}...")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        filename = f"{name}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"Process {os.getpid()} finished: Saved {filename}")
    except Exception as e:
        print(f"Process {os.getpid()} failed on {name}: {e}")


def main():
    processes = []

    # Create a process for each URL
    for name, url in urls.items():
        # Using multiprocessing.Process for explicit control
        process = multiprocessing.Process(target=scrape_url, args=(name, url))
        processes.append(process)
        process.start()
        print(f"Started process for {name}")

    # Wait for all processes to complete
    for process in processes:
        process.join()

    print("All scraping processes have finished.")


if __name__ == "__main__":
    main()