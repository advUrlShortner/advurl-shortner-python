# advurl_shortner

Python Library to help you short urls with advanced options. Multiple domains, URL TTL, visit statistics etc.

## Features
- Easy to use
- Multiple domains
- Link TTL (Time-To-Live) in seconds
- Redirect to second URL after primary URL expires (TTL)
- Randomized and weighted randomnized redirect to different URLs
- Password-protected statistics of visits to a shortened URL
- Password protected shortened URL parameters (TTL, second URL, etc.)

## Installation

In order install this package, simply run:

```bash
pip install advurl_shortner
```

## Usage

To use shorten_url, you first need to import the package:

```python
import advurl_shortner
```


### Shorten URL:
```python

advurl_shortner.short("https://google.com/")
# Returns the shortened URLs

advurl_shortner.short("https://google.com/", pass="1234x")
# Returns shortened URLs, sets a password to access statistics and shortened URL parameters.

advurl_shortner.short("https://google.com/", ttl=86400)
# Returns the shortened URLs., after 24 hours (86400 seconds) will return "The Link You Followed Has Expired"

advurl_shortner.short("https://google.com/",second_url="https://bing.com/")
# Returns shortened URLs. The shortened link is randomly redirected to one of the provided URLs.

advurl_shortner.short("https://google.com/",second_url="https://bing.com/", "weights"=[0.3, 0.7])
# Returns shortened URLs. The shortened link is randomly (weighted by weight parameter) redirected to one of the provided URLs.

advurl_shortner.short("https://google.com/", ttl=86400, second_url="https://bing.com/")
# Returns the shortened URLs., after 24 hours (86400 seconds)  shortned link will redirect to second_url


```
### Getting shortned URL parameters and visit statistics:
```python
advurl_shortner.stat("https://liil.bid/kdRz",pass="1234x")
# Returns the parameters and visit statistics of the shortened URL
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
