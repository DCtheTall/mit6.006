from urllib2 import urlopen
from urllib import urlencode
import json
from bs4 import BeautifulSoup

# Wikipedia scraper for getting documents to compare

def get_article_w_prompt(prompt):
  """
  Prompts user for search query then scrapes
  Wikipedia for an article with that query

  Returns the content of the article as a list of strings
  separated by line

  """
  query = raw_input(prompt)
  url = 'https://en.wikipedia.org' \
      '/w/api.php?action=query&list=search&format=json&%s' \
      % urlencode({'srsearch': query})
  json_res = urlopen(url).read()
  data = json.loads(json_res)
  results = data['query']['search']
  if not results:
    print 'Unable to find an article with that query. Please try again.\n'
    return get_article_w_prompt(prompt)
  title = '_'.join(results[0]['title'].split(' '))
  url = 'https://en.wikipedia.org/wiki/%s' % title
  html = urlopen(url).read()
  parsed_html = BeautifulSoup(html, 'html.parser')
  article = parsed_html.body.find('div', attrs={'id': 'bodyContent'}).text
  return article


def get_documents():
  first_doc = get_article_w_prompt(
      'What would you like to search for the first article? '
  )
  second_doc = get_article_w_prompt(
      'What would you like to search for the second article? '
  )
  return (first_doc.split('\n'), second_doc.split('\n'))
