import requests
from bs4 import BeautifulSoup

def get_serp_data(keyword_clusters):
    results = []
    for label, keywords in keyword_clusters.items():
        for kw in keywords:
            url = f"https://www.google.com/search?q={kw}"
            headers = {"User-Agent": "Mozilla/5.0"}
            res = requests.get(url, headers=headers)
            soup = BeautifulSoup(res.text, "html.parser")
            for g in soup.select("div.g")[:3]:
                title = g.select_one("h3")
                link = g.select_one("a")["href"] if g.select_one("a") else ""
                if title and link:
                    results.append({
                        "cluster": label,
                        "keyword": kw,
                        "title": title.text,
                        "link": link
                    })
    return results
