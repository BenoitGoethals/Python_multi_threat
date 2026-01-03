import concurrent.futures
import time

import urllib.request

def task(n):
    print(f"Starting task...{n}")
    time.sleep(n)
    print(f"Task completed {n}")
    return n*n

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        reslt=executor.map(task,[1,2,3])
    for r in reslt:
        print(r)
    print("Done")



    URLS = ['http://www.foxnews.com/',
            'http://www.cnn.com/',
            'http://europe.wsj.com/',
            'http://www.bbc.co.uk/',
            'http://nonexistent-subdomain.python.org/']

    # Retrieve a single page and report the URL and contents
    def load_url(url, timeout):
        with urllib.request.urlopen(url, timeout=timeout) as conn:
            return conn.read()

    # We can use a with statement to ensure threads are cleaned up promptly
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its URL
        future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))

if __name__ == "__main__":
    main()