import requests
import re

# URL of the proxy list page
url = "https://schoolwebproxy.com/1000-proxies-for-school-chromebook-2025/"

# Domains to exclude from the results
excluded_domains = [
    "graph.org",
    "schoolwebproxy.com",
    "binance.com",
    "example.com",
    "googletagmanager.com",
    "pinterest.com",
    "schema.org",
    "clarity.ms",
    "api.w.org",
    "cdn.onesignal.com",
    "ogp.me",
    "googlesyndication.com"
]

# Fetch the page content
response = requests.get(url)
text = response.text

# Extract all URLs starting with https://
proxy_links = re.findall(r'https://[^\s"<>\n]+', text)

# Filter out links that contain any excluded domain
filtered_links = [
    link for link in proxy_links
    if not any(domain in link for domain in excluded_domains)
]

# Deduplicate and sort
filtered_links = sorted(set(filtered_links))

# Write to the file at the root of the repo
with open("proxies.txt", "w") as f:
    for link in filtered_links:
        f.write(link + "\n")
