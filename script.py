import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://library.unm.edu/"
response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")

carousel_items = soup.select(".carousel-inner a")

results = []
seen_urls = set()

for a_tag in carousel_items:
    href = a_tag.get("href")
    img_tag = a_tag.find("img")
    
    if img_tag:
        src = img_tag.get("src")
        alt = img_tag.get("alt", "No description")
        full_img_url = urljoin(base_url, src)
        full_link_url = urljoin(base_url, href) if href else None

        if full_img_url in seen_urls:
            continue  # Skip duplicates

        seen_urls.add(full_img_url)
        results.append({
            "image_url": full_img_url,
            "alt_text": alt,
            "link": full_link_url
        })

# Print results
#for item in results:
#    print(f"Image: {item['image_url']}")
#    print(f"Alt Text: {item['alt_text']}")
#    print(f"Link: {item['link']}\n")

# Save the results to a JSON file
with open("carousel_data.json", "w") as json_file:
    json.dump(results, json_file, indent=4)
    
print("Data saved to carousel_data.json")
