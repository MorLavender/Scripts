import requests
import hashlib
import time

def fetch_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None

def monitor_website(url, interval=60):
    previous_hash = None
    while True:
        content = fetch_website_content(url)
        if content:
            current_hash = hashlib.md5(content.encode('utf-8')).hexdigest()
            if previous_hash is None:
                previous_hash = current_hash
                print(f"Monitoring {url} for changes every {interval} seconds...")
            elif current_hash != previous_hash:
                print(f"Change detected on {url}!")
                previous_hash = current_hash
            else:
                print(f"No changes detected on {url}.")
        time.sleep(interval)

if __name__ == "__main__":
    url = input("Enter the URL of the website to monitor: ")
    try:
        interval = int(input("Enter the monitoring interval in seconds (default is 60): ") or 60)
    except ValueError:
         interval = 60
         print("Invalid input for interval. Using default value of 60 seconds.")
    monitor_website(url, interval)
