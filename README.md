# advurl_shortner - Advanced URL Shortner for Python

[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square)](LICENSE.md)

Python Library to help you short urls with advanced options. Multiple domains, URL TTL, split tests, visit statistics etc.
An extended native Python wrapper for [AdvUrlShortner API](https://github.com/advUrlShortner/API/) with minimal requirements. Supports all methods and types of responses.

## Features

- Easy to use
- Multiple domains
- Link TTL (Time-To-Live) in seconds
- Redirect to second URL after primary URL expires (TTL)
- Randomized and weighted randomnized redirect to different URLs (split tests etc.)
- Password-protected statistics of visits to a shortened URL
- Password protected shortened URL parameters (TTL, second URL, etc.)

## Usage

To use shorten_url, you first need to import the package:

```python
import advurl_shortner
```


### Shorten URL:

```python

advurl_shortner.short("https://google.com/")
# Returns the shortened URLs in JSON
# Example: {"urls": ["https://liii.pw/N", "https://illi.ink/N", "https://illi.cfd/N"]}XX

advurl_shortner.short("https://google.com/", password="1234x")
# Returns shortened URLs, sets a password to access visiting statistics and shortened URL parameters.

advurl_shortner.short("https://google.com/", ttl=86400)
# Returns the shortened URLs., after 24 hours (86400 seconds) will return "The Link You Followed Has Expired"

advurl_shortner.short("https://google.com/", ttl=86400, second_url="https://bing.com/")
# Returns the shortened URLs., after 24 hours (86400 seconds)  shortned link will redirect to second_url

advurl_shortner.short("https://google.com/",second_url="https://bing.com/")
# Returns shortened URLs. The shortened link is randomly redirected to one of the provided URLs.

advurl_shortner.short("https://google.com/",second_url="https://bing.com/", weights=[0.3, 0.7])
# Returns shortened URLs.
# The shortened link is randomly (weighted by weight parameter) redirected to one of the provided URLs.
# approximately 30% to "https://google.com/ and 70% to "https://bing.com/"



```
### Getting shortned URL parameters and visit statistics:

```python
advurl_shortner.stat("https://illi.cfd/H","aaa")
# Returns the parameters and visit statistics of the shortened URL stored with password "1234x".
# Example:
#{
#	"url": "http://google.com/?z=1",
#	"second_url": "http://yahoo.com/",
#	"ttl": null,
#	"date_created": "1703411470",
#	"weights": null,
#	"visits": 4,
#	"primary_url_expired": false
#}
```

### TODO:
- More than 2 URLs
- Advanced visit statistics
