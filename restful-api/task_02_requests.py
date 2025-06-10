#!/usr/bin/python3
"""a function to request data"""
import requests
import json
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

    with open('posts.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(data[0].keys())
        for rows in data:
            writer.writerow(rows.values())
