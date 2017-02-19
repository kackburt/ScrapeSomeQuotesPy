from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
import random

def get_soup(site_url):
    site_html = urlopen(site_url).read()
    site_soup = BeautifulSoup(site_html)
    return site_soup

def main():

    print()
    print("PRINTING RANDOM QUOTES")
    print()

    url = "http://quotes.yourdictionary.com/theme/marriage/"
    quote_soup = get_soup(url)
    quotes = quote_soup.findAll("p", attrs={"class": "quoteContent"})

    for quote in quotes:
        print(quote.string)

    #for i in range(5):
        #print(quotes)
        #i = i + 1

    print()
    print("Parsing done. Goodbye!")


if __name__ == '__main__':
    main()
