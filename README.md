The Python SEC RSS Feed Parser Repository
------
Version 1.0

Using Python, read the SEC RSS Feed: https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=&company=&dateb=&owner=include&start=0&count=100&output=html to parse the entries in the feed into JSON.


Setup
------

To run this have the python dependencies installed:

feedparser

json

Usage
------

feedparser-examples$ ./read_feed.py

The rss_configs/sec_rss_config.json file maintains the count=100 but this is easy to override


Additional / License
------

This is free to use MIT LICENSE and all that fun.

Enjoy.






