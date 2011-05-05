# RedditMyWallpaper
#  - Sets your desktop background as a random picture from a subreddit.

### Settings

subreddits = [
    'cityporn',
    'earthporn'
]

sort = 'hot'

limit = 10

### Dependencies

from wallpaperchanger import changeWallpaper as wp
from random import choice
from reddit import Reddit # Considering to remove this dependency, as I use very few features
from urllib import urlretrieve
from os     import getcwd

### Program

r = Reddit(user_agent="RedditMyWallpaper")
posts = r.get_subreddit("+".join(subreddits))
posts = getattr(posts, 'get_%s' % sort)(limit=limit)
url = choice(posts).url
print url
urlretrieve(url, 'img.jpg')

wp(getcwd() + '/img.jpg')
