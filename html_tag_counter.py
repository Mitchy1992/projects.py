import requests
from bs4 import BeautifulSoup
import pandas as pd

def web_scraper(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx)

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all HTML tags and count their occurrences
        tags = [tag.name for tag in soup.find_all()]
        tags_count = {tag: tags.count(tag) for tag in set(tags)}

        # Create a DataFrame from the dictionary
        df = pd.DataFrame(list(tags_count.items()), columns=['Tag', 'Count'])

        return df

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Example usage:
url = 'https://en.wikipedia.org/wiki/Oppenheimer_(film)'  # Replace with the desired URL
result = web_scraper(url)

if isinstance(result, pd.DataFrame):
    print(result)
else:
    print(result)
