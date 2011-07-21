# RedditMyWallpaper
#  - Sets your desktop background as a random picture from a subreddit.

### Settings
limit = 10

### Dependencies
from wallpaperchanger import changeWallpaper as wp
import json
import urllib
import random
from urllib import urlretrieve
from os import getcwd

### Program
url = "http://www.reddit.com/r/earthporn.json"
j = json.load(urllib.urlopen(url))['data']
print len(j['children'])
urls = []

for i in range(1, 25):
  urls.append(j['children'][i]['data']['url'])

print urlretrieve(random.choice(urls), 'img.jpg')

wp(getcwd() + '/img.jpg')
