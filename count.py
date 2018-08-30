#!/usr/bin/env python3

from collections import Counter
from datetime import datetime

import requests

API_URL = 'https://getpocket.com/v3/get'
STATE_MAP = {
    '0': 'Unread',
    '1': 'Archived',
}


def print_status_stats(articles):
    counter = Counter(STATE_MAP.get(article['status'], 'Other') for article in articles)
    print(f'Total of {len(articles):,} articles')
    for state, count in counter.items():
        print(f'{count:,} {state}')
    word_count = sum(int(article['word_count'])
                     for article in articles if article['status'] == '0')
    if counter['Unread'] > 0:
        print(f'Total of {word_count:,} unread words '
              f'(average of {round(word_count / counter["Unread"]):,} per article)')


def print_reading_hist(articles):
    hist = Counter(datetime.fromtimestamp(int(article['time_updated'])).date()
                   for article in articles if article['status'] == '1')
    for date, count in sorted(hist.items())[-25:]:
        print(f'{date.strftime("%d/%m/%Y")}: {"*" * count} ({count})')


def main(consumer_key: str, access_token: str):
    assert consumer_key is not None, 'Missing consumer key'
    assert access_token is not None, 'Missing access token'

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'X-Accept': 'application/json',
    }
    body = {
        'consumer_key': consumer_key,
        'access_token': access_token,
        'state': 'all',
    }
    resp = requests.post(API_URL, headers=headers, json=body).json()
    articles = list(resp['list'].values())
    print('=' * 75)
    print_reading_hist(articles)
    print('=' * 75)
    print_status_stats(articles)
    print('=' * 75)


if __name__ == '__main__':
    import os
    main(os.getenv('CONSUMER_KEY'), os.getenv('ACCESS_TOKEN'))
