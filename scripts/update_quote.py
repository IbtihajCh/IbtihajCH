import requests
import re

def fetch_quote():
    """Fetch a random programming/inspirational quote from ZenQuotes API."""
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=10)
        response.raise_for_status()
        data = response.json()[0]
        quote = data["q"]
        author = data["a"]
        return quote, author
    except Exception as e:
        print(f"Failed to fetch quote: {e}")
        # Fallback quote if API is down
        return "Talk is cheap. Show me the code.", "Linus Torvalds"


def update_readme(quote, author):
    """Replace content between QUOTE_START and QUOTE_END markers in README.md."""
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    new_block = (
        f"<!-- QUOTE_START -->\n"
        f'> *"{quote}"*\n'
        f"> — {author}\n"
        f"<!-- QUOTE_END -->"
    )

    updated = re.sub(
        r"<!-- QUOTE_START -->.*?<!-- QUOTE_END -->",
        new_block,
        content,
        flags=re.DOTALL
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"✅ Quote updated: \"{quote}\" — {author}")


if __name__ == "__main__":
    quote, author = fetch_quote()
    update_readme(quote, author)
