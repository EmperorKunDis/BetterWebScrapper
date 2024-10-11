# Web Scraper with Root URL Filtering

## Overview

This is a Python-based web scraper that allows you to extract and save content and URLs from a specified website. The scraper is designed to filter URLs based on a root URL, ensuring that only links from the same domain are collected. It also offers functionality to remove duplicate entries from the collected URL list.

### Key Features

- **Root URL Filtering**: Scrapes only links that start with the specified root URL.
- **URL Collection**: Saves the collected URLs to `URL_List.txt`.
- **Content Saving**: Saves scraped content to `Content.txt`.
- **Duplicate Removal**: Removes duplicate URLs from `URL_List.txt` with a single command.
- **User Input**: Simple interface to choose between scraping, removing duplicates, or exiting.

## How It Works

1. **Set Root URL**: The scraper prompts the user to enter the root URL (e.g., `https://www.porthub.com/lovefull-books`). This ensures that only URLs matching this root will be collected during scraping.
2. **Scraping**: Once a full URL is provided, the program scrapes the content and saves relevant URLs to a list.
3. **Duplicate Removal**: The program includes a feature to remove duplicates from `URL_List.txt`.
4. **Repeatable**: The program can be run multiple times, allowing you to scrape different pages and manage the URL list easily.

## How to Use

1. **Run the Script**: 
   - Run the script using your preferred Python environment.

2. **Set Root URL**:
   - When prompted, enter the root URL of the site you want to scrape (e.g., `https://www.porthub.com/lovefull-books`).

3. **Scraping**:
   - Choose option `1` to scrape a webpage. Enter the full URL of the page you want to scrape.
   - The script will save:
     - **Content** to `Content.txt`.
     - **Matching URLs** to `URL_List.txt`.

4. **Remove Duplicates**:
   - Choose option `2` to remove duplicate URLs from `URL_List.txt`.

5. **Exit**:
   - Choose option `3` to exit the program.

### Example Usage:

```bash
Enter root URL: https://www.porthub.com/lovefull-books
1. Scrape website
2. Remove duplicates from URL_List.txt
3. Exit

Choose an option: 1
Enter URL to scrape: https://www.porthub.com/lovefull-books
Scraping content...
Saving URLs to URL_List.txt...
