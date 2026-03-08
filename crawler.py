import requests
from bs4 import BeautifulSoup

def crawl_webpages(start_urls, max_pages=15):

    visited = set()
    documents = []
    titles = []
    urls = []

    headers = {"User-Agent": "Mozilla/5.0"}

    queue = list(start_urls)

    while queue and len(visited) < max_pages:

        url = queue.pop(0)

        if url in visited:
            continue

        try:
            response = requests.get(url, headers=headers, timeout=5)

            soup = BeautifulSoup(response.text, "html.parser")

            title = soup.title.string if soup.title else "No Title"

            text = soup.get_text(separator=" ", strip=True)

            documents.append(text)
            titles.append(title)
            urls.append(url)

            visited.add(url)

            # collect more links
            for link in soup.find_all("a", href=True):

                href = link["href"]

                if href.startswith("/wiki/"):

                    new_url = "https://en.wikipedia.org" + href

                    if new_url not in visited:
                        queue.append(new_url)

        except:
            continue

    return documents, titles, urls
