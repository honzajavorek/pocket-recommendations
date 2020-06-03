from urllib.parse import urlparse, parse_qs

from lxml import html


__version__ = '0.1.0'


def parse(html_text):
    html_tree = html.fromstring(html_text)
    return [parse_post(post_el)
            for post_el in html_tree.cssselect('.sprofile-post')]


def parse_post(post_el):
    title_el = post_el.cssselect('.sprofile-article-title')[0]
    title = title_el.text_content()

    link_el = post_el.cssselect('.sprofile-article-link')[0]
    pocket_url = link_el.get('href')

    return dict(title=title,
                url=parse_url(pocket_url),
                pocket_comment=parse_comment(post_el),
                pocket_url=pocket_url,
                pocket_recommended_at=None)


def parse_url(pocket_url):
    parts = urlparse(pocket_url)
    url_param = parse_qs(parts.query).get('url')
    if url_param:
        return url_param[0]
    return None


def parse_comment(post_el):
    try:
        comment_el = post_el.cssselect('.sprofile-attribution-comment')[0]
        return comment_el.text_content()
    except IndexError:
        return None
