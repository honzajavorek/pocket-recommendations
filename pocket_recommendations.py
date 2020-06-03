import re
import html
from datetime import timedelta
from urllib.parse import urlparse, parse_qs

from lxml.html import fromstring as parse_html


def parse(html_text, today=None):
    html_tree = parse_html(html_text)
    return [parse_post(post_el, today=today)
            for post_el in html_tree.cssselect('.sprofile-post')]


def parse_post(post_el, today=None):
    title = post_el.cssselect('.sprofile-article-title')[0].text_content()
    title_unescaped = html.unescape(title)

    pocket_url = post_el.cssselect('.sprofile-article-link')[0].get('href')
    pocket_url_https = re.sub(r'^http://', 'https://', pocket_url)

    if today:
        ago_text = post_el.cssselect('.sprofile-post-time')[0].text_content()
        pocket_recommended_at = parse_pocket_recommended_at(ago_text, today)
    else:
        pocket_recommended_at = None

    return dict(title=title_unescaped,
                url=parse_url(pocket_url),
                pocket_comment=parse_pocket_comment(post_el),
                pocket_url=pocket_url_https,
                pocket_recommended_at=pocket_recommended_at)


def parse_url(pocket_url):
    parts = urlparse(pocket_url)
    url_param = parse_qs(parts.query).get('url')
    if url_param:
        return url_param[0]
    return None


def parse_pocket_comment(post_el):
    try:
        comment_el = post_el.cssselect('.sprofile-attribution-comment')[0]
        return comment_el.text_content()
    except IndexError:
        return None


def parse_pocket_recommended_at(ago_text, today):
    if 'day' in ago_text:
        days_ago = int(re.search(r'\d+', ago_text).group(0))
        return today - timedelta(days=days_ago)
    return today  # minutes, hours? (Pocket doesn't use weeks, months)
