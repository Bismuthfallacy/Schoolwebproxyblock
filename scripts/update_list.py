import requests
import re

# URL of the proxy list page
url = "https://schoolwebproxy.com/1000-proxies-for-school-chromebook-2025/"

# Fetch the page content
response = requests.get(url)
text = response.text

# Extract all URLs starting with https://, excluding stuff in tags or with line breaks
proxy_links = re.findall(r'https://[^\s"<>\n]+', text)

# Remove duplicates and sort
proxy_links = sorted(set(proxy_links))

# Write to the file at the root of the repo
with open("proxies.txt", "w") as f:
    for link in proxy_links:
        f.write(link + "\n")
