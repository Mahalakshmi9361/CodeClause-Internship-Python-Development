import pyshorteners

def shorten_url(long_url):
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_url)
    return short_url

def expand_url(short_url):
    shortener = pyshorteners.Shortener()
    expanded_url = shortener.tinyurl.expand(short_url)
    return expanded_url

if __name__ == "__main__":
    long_url = input("Enter the URL to shorten: ")
    short_url = shorten_url(long_url)
    print("Shortened URL:", short_url)
 
    expanded_url = expand_url(short_url)
    print("Expanded URL:", expanded_url)
