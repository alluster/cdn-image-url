import urllib.parse

def generate_urls(image_names, base_url="https://cdn.prod.website-files.com/66dab17d350a82afc58de8b3/"):
    
    urls = []
    for name in image_names:
        encoded_name = urllib.parse.quote(name)
        url = f"{base_url}{encoded_name}"
        urls.append(url)
    return urls

# Example usage:
image_names = [
    "1996 National Insurance Company of Etiopia kilpailu 1.palkinto 1-200 Ark.tsto CJN.jpg",
    "2024 Turun musiikkitalo 1-200 PES-arkkitehdit.jpg"
]

urls = generate_urls(image_names)

output = "\n".join(urls)
print(output)