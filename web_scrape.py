
# source 1

# import library that allows us to pull data from websites
import requests

# requests data from url below
request = requests.get('https://www.adl.org/hate-symbols')
content = request.content

# imports library that allows for us to pick what parts of the content to pull
from bs4 import BeautifulSoup

# stores all of the site's content
soup = BeautifulSoup(content)

# filters soup to only display what is specified
specificData = soup.find_all('img')

print(specificData)


# source 2

# requests data from url below
request = requests.get('http://www.rsdb.org')
content = request.content

# imports library that allows for us to pick what parts of the content to pull
from bs4 import BeautifulSoup

# stores all of the site's content
soup = BeautifulSoup(content)

# filters soup to only display what is specified
specificData = soup.find_all('a')

# prints the html code including the specified tags
print(specificData)


# source 3

# requests data from url below
request = requests.get('https://archive.attn.com/stories/7307/common-expressions-words-that-are-sexist')
content = request.content

# imports library that allows for us to pick what parts of the content to pull
from bs4 import BeautifulSoup

# stores all of the site's content
soup = BeautifulSoup(content)

# filters soup to only display what is specified
specificData = soup.find_all('h2')

# prints the html code including the specified tags
pprint(specificData)
