from datetime import date

import pytest

from pocket_recommendations import parse_pocket_recommended_at


@pytest.mark.parametrize('ago_text,expected', [
    ('1 minute ago', date(2020, 6, 3)),
    ('1 day ago', date(2020, 6, 2)),
    ('3 days ago', date(2020, 5, 31)),
    ('61 days ago', date(2020, 4, 3)),
])
def test_parse_pocket_recommended_at(ago_text, expected):
    today = date(2020, 6, 3)
    assert parse_pocket_recommended_at(ago_text, today) == expected
