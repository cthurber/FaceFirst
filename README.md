# FaceFirst
### What
FaceFirst is a simple Python commandline program that allows the user to retrieve the names and user ids of the first 100 Facebook users.

### Why
I found [this post](https://www.quora.com/The-first-user-id-on-Facebook-is-4-Mark-Zuckerberg-Who-were-1–3) on Quora about Facebook's first few users, and I got curious. I had also been looking into a library a friend of my found called [Splinter](http://splinter.readthedocs.org), a webpage API for Python (highly recommend it by the way!). I decided this would be a perfect time to try it out, so I created this simple program that interates through each user ID and records all valid names and ids it finds in a CSV file.

### How
FaceFirst uses the [Splinter API](http://splinter.readthedocs.org) to interact and capture webpages, and the [BeautifulSoup API](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) to parse them. The rest is simple ifs and prints, and of course a nice, concise CSV spreadsheet. I made sure to implement a randomly generated delay to avoid DOSing Facebook's servers.
#### What you need:
- Python 3.x
- [Splinter API](http://splinter.readthedocs.org) ```pip install splinter```
- [BeautifulSoup API](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) ```pip install beautifulsoup4```
