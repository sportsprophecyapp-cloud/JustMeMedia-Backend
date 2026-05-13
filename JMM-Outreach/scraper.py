import requests
from bs4 import BeautifulSoup
import re

def scrape_website(url):
    """
    Fetches the homepage of a website and extracts key information.
    Returns a summary of services and business description.
    """
    if not url.startswith('http'):
        url = 'https://' + url
        
    try:
        print(f"Scraping {url}...")
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.extract()

        # Get text
        text = soup.get_text()

        # Break into lines and remove leading and trailing whitespace
        lines = (line.strip() for line in text.splitlines())
        # Break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # Drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        # Basic heuristic: look for "Services", "About", or the first few paragraphs
        # We'll just take the first 1000 characters and let Ollama handle the summary if needed,
        # but the task asks for a summary here.
        
        # Let's try to be a bit smarter and find headings
        services = []
        for h in soup.find_all(['h1', 'h2', 'h3']):
            h_text = h.get_text().strip()
            if len(h_text) > 3:
                services.append(h_text)
        
        summary = f"Services/Headlines: {', '.join(services[:10])}\n\n"
        summary += "Content Snippet:\n" + text[:1500] # Take a decent chunk
        
        # Truncate to word limit (approximate)
        words = summary.split()
        if len(words) > 200:
            summary = ' '.join(words[:200]) + "..."
            
        return summary

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return "Could not fetch website content."

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python scraper.py <url>")
    else:
        print(scrape_website(sys.argv[1]))
