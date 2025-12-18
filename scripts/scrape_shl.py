import pandas as pd
import requests
from bs4 import BeautifulSoup

print("Reading Excel dataset...")

# 1. Read your provided dataset
df = pd.read_excel("Gen_AI Dataset.xlsx")

# 2. Get unique assessment URLs
urls = df["Assessment_url"].dropna().unique()

print("Found", len(urls), "unique assessment URLs")

rows = []

# 3. Visit each assessment page
for url in urls:
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, "html.parser")

        # 4. Extract name and description
        name_tag = soup.find("h1")
        desc_tag = soup.find("meta", attrs={"name": "description"})

        name = name_tag.text.strip() if name_tag else ""
        description = desc_tag["content"].strip() if desc_tag else ""

        rows.append({
            "name": name,
            "url": url,
            "description": description
        })

        print("Fetched:", name)

    except Exception as e:
        print("Failed:", url)

# 5. Save to CSV
catalog = pd.DataFrame(rows)
catalog.to_csv("shl_catalog.csv", index=False)

print("DONE ✅ Saved", len(catalog), "assessments to shl_catalog.csv")
