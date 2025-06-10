#!/usr/bin/python3
"""a function to request data"""
import requests
import csv


def fetch_and_print_posts():
    """fetch_and_print_posts function"""

    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    if r.status_code != 200:
        return

    print(f"Status Code: {r.status_code}")
    data = r.json()

    for posts in data:
        print(posts["title"])


def fetch_and_save_posts():
    """fetch_and_save_posts function"""

    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    if r.status_code != 200:
        return

    data = r.json()
    headers = ['id', 'title', 'body']
    # data_header = data[0].values()

    with open('posts.csv', 'w') as f:
        writer = csv.DictWriter(f, extrasaction='ignore', fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
