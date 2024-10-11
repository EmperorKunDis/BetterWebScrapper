import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import re

root_url = ""

def set_root_url():
    global root_url
    root_url = input("Enter the root URL (e.g., https://www.porthub.com/lovefull-books): ").strip()
    print(f"Root URL set to: {root_url}")

def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        text_content = soup.get_text(separator=" ", strip=True)
        links = []
        for a_tag in soup.find_all("a", href=True):
            link = urljoin(url, a_tag["href"])
            link_text = a_tag.text.strip()
            if link.startswith(root_url):
                links.append((link, link_text))
        return text_content, links
    except requests.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return None, None

def extract_sentences(text):
    sentence_pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s(?=[A-Z])'
    sentences = re.split(sentence_pattern, text)
    valid_sentences = [s.strip() for s in sentences if re.match(r'^[A-Z].*[.!?]$', s.strip())]
    return valid_sentences

def save_to_file(content, filename):
    file_path = os.path.join(os.getcwd(), filename)
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(content + "\n\n")

def read_url_list(filename):
    file_path = os.path.join(os.getcwd(), filename)
    urls = set()
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith("URL: "):
                    urls.add(line.strip()[5:])  # Remove "URL: " prefix
    print(f"Read {len(urls)} URLs from {filename}")
    return urls

def remove_duplicates_from_file(filename):
    file_path = os.path.join(os.getcwd(), filename)
    if os.path.exists(file_path):
        urls = read_url_list(filename)
        print(f"Total URLs read: {len(urls)}")
        root_urls = {url for url in urls if url.startswith(root_url)}
        print(f"URLs matching root URL: {len(root_urls)}")
        
        # Debug: Print some URLs
        print("Sample URLs:")
        for url in list(root_urls)[:5]:
            print(url)
        
        if root_urls:
            with open(file_path, "w", encoding="utf-8") as file:
                for url in sorted(root_urls):
                    file.write(f"URL: {url}\n")
            print(f"Kept {len(root_urls)} URLs that match the root URL.")
            print(f"Removed {len(urls) - len(root_urls)} URLs that don't match the root URL.")
        else:
            print("Warning: No URLs match the root URL. File not modified.")
    else:
        print(f"File {filename} not found.")

def scrape_urls_loop():
    existing_urls = read_url_list("URL_List.txt")
    while True:
        url = input("Enter a URL to scrape (or 'back' to return to main menu): ").strip()
        if url.lower() == 'back':
            break
        
        text, hyperlinks = scrape_website(url)

        if text and hyperlinks:
            sentences = extract_sentences(text)
            save_to_file(f"URL: {url}\n\nContent:\n" + "\n".join(sentences), "Content.txt")

            new_links = [(link, text) for link, text in hyperlinks if link not in existing_urls]
            if new_links:
                links_content = "\n".join([f'{link}' for link, _ in new_links])
                save_to_file(links_content, "URL_List.txt")
                existing_urls.update(link for link, _ in new_links)

            print(f"Data from {url} has been successfully saved.")
            print(f"Added {len(new_links)} new URLs matching the root URL.")
            print(f"Saved {len(sentences)} valid sentences to DesignPatterns.txt.")
        else:
            print(f"Failed to retrieve data from {url}.")

def main():
    set_root_url()
    
    while True:
        action = input("Choose an action:\n1. Start scraping websites\n2. Remove duplicates from URL list\n3. Exit\nYour choice: ")

        if action == "1":
            scrape_urls_loop()
        elif action == "2":
            print("Removing duplicates and non-root URLs from URL_List.txt...")
            remove_duplicates_from_file("URL_List.txt")
        elif action == "3":
            print("Program terminated.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
