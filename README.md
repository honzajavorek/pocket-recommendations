# pocket-recommendations

Unofficial library to get a feed of one's Pocket recommendations

## Usage

Get a public Pocket profile, like [this one](https://getpocket.com/@honzajavorek). Download its HTML using Python or anything else:

```bash
$ curl "https://getpocket.com/@honzajavorek" > getpocket-com-honzajavorek.html

```

In your Python program, have the HTML ready as a string:

```python
>>> from pathlib import Path
>>> html_text = Path('getpocket-com-honzajavorek.html').read_text()

```

Now you can use this library to parse the HTML:

```python
>>> import pocket_recommendations
>>> items = pocket_recommendations.parse(html_text)
>>> len(items)
50

```

Each item then looks like this:

```python
>>> from pprint import pprint
>>> pprint(items[0])
{'pocket_comment': 'Šablona na váš úspěšný HackerNews post',
 'pocket_recommended_at': None,
 'pocket_url': 'http://getpocket.com/redirect?&url=https%3A%2F%2Fsaagarjha.com%2Fblog%2F2020%2F05%2F10%2Fwhy-we-at-famous-company-switched-to-hyped-technology%2F&h=eff6d8cac22c9b475463d037037b0efdcf44b762c9b0b7913de2104cab5fa67d',
 'title': 'Why we at $FAMOUS_COMPANY Switched to $HYPED_TECHNOLOGY',
 'url': 'https://saagarjha.com/blog/2020/05/10/why-we-at-famous-company-switched-to-hyped-technology/'}

```

### Date of Recommendation

You can specify the date when the HTML has been downloaded to get the relative dates when the recommendations have been posted:

```python
>>> from datetime import date
>>> items = pocket_recommendations.parse(html_text, today=date(2020, 6, 3))
>>> pprint(items[0])
{'pocket_comment': 'Šablona na váš úspěšný HackerNews post',
 'pocket_recommended_at': date(2020, 6, 2),
 'pocket_url': 'http://getpocket.com/redirect?&url=https%3A%2F%2Fsaagarjha.com%2Fblog%2F2020%2F05%2F10%2Fwhy-we-at-famous-company-switched-to-hyped-technology%2F&h=eff6d8cac22c9b475463d037037b0efdcf44b762c9b0b7913de2104cab5fa67d',
 'title': 'Why we at $FAMOUS_COMPANY Switched to $HYPED_TECHNOLOGY',
 'url': 'https://saagarjha.com/blog/2020/05/10/why-we-at-famous-company-switched-to-hyped-technology/'}

```
