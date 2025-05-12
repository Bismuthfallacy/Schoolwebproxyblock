import requests
from bs4 import BeautifulSoup
from datetime import datetime

TARGET_URL = 'https://schoolwebproxy.com/1000-proxies-for-school-chromebook-2025/'  # Replace with the actual URL
OUTPUT_FILE = 'proxies.txt'

def fetch_links():
    response = requests.get(TARGET_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Adjust the logic here for your specific site
    links = [a['href'] for a in soup.find_all('a', href=True) if 'http' in a['href']]
    return set(links)

def load_existing():
    try:
        with open(OUTPUT_FILE, 'r') as f:
            return set(line.strip() for line in f if line.strip() and not line.startswith('#'))
    except FileNotFoundError:
        return set()

def save_links(links):
    timestamp = datetime.utcnow().isoformat() + 'Z'
    with open(OUTPUT_FILE, 'w') as f:
        f.write(f"# Last updated: {timestamp}\n")
        for link in sorted(links):
            f.write(link + '\n')

def main():
    new_links = fetch_links()
    existing_links = load_existing()
    combined = existing_links.union(new_links)

    if combined != existing_links:
        save_links(combined)
        print(f"Added {len(combined - existing_links)} new links.")
    else:
        print("No new links found.")

if __name__ == '__main__':
    main()
