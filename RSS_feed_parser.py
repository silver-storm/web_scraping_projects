def parse_RSS(feed='https://timesofindia.indiatimes.com/rssfeedstopstories.cms'):

  import requests
  import bs4

  Soup = bs4.BeautifulSoup(requests.get(feed).text)
  print(Soup.select('copyright')[0].get_text()+'\n\n')

  for title,description,link,date in zip(Soup.select('title'),Soup.select('description'),Soup.select('guid'),Soup.select('pubdate')):
    print(date.get_text())
    print(title.get_text())
    print(description.get_text())
    print("Link to the article : ", link.get_text())
    print(''.join(['*']*400) + '\n')

if __name__ == "__main__":
  parse_RSS()