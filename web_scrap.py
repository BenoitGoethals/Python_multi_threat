import os
import requests
from multiprocessing import Pool

urls = {
    "hln": "https://hln.be",
    "fet": "https://www.routen.be/turfput-wandelroute",
}


def scrape_url(name_url_tuple):
    """
    Worker function to fetch a URL and save its content to an HTML file.
    """
    name, url = name_url_tuple
    print(f"Scraping {name}: {url}...")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check for HTTP errors

        filename = f"{name}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)

        return f"Successfully saved {name} to {filename}"
    except Exception as e:
        return f"Failed to scrape {name}: {e}"


def main():
    # Ensure we have a list of tuples for the Pool to map over
    url_items = list(urls.items())

    # Use a Pool of processes. By default, it uses the number of CPU cores.
    with Pool(processes=len(url_items)) as pool:
        results = pool.map(scrape_url, url_items)

    for result in results:
        print(result)


if __name__ == "__main__":
    # Create an output directory if you want to keep things tidy
    # os.makedirs("scraped_pages", exist_ok=True)
    main()