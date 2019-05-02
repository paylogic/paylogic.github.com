#!/usr/bin/env python3
import csv
import unicodedata
import re
from os import path
from collections import OrderedDict

talks = []
with open('talks.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    talks = [r for r in reader]


def strip_accents(str):
    return ''.join((c for c in unicodedata.normalize('NFD', str)
                    if unicodedata.category(c) != 'Mn'))


def to_slug(str):
    return re.sub('[±\.:,\'\\(\)!\?@#$]', '',
                  strip_accents(str)
                  .lower()
                  .replace(' & ', ' and ')
                  .replace(' ', '-'))


def write_rst(path, meta, body):
    with open(path, 'w') as f:
        for key, value in meta.items():
            f.write(f":{key}: {value}\n")
        f.write('\n')
        f.write(body)
        f.write('\n')


for talk in talks:
    if talk['Accept?'] != 'y':
        continue

    speaker = talk['Your name']
    speaker_slug = to_slug(speaker)
    bio = talk['Short bio']
    title = talk['Title of your talk']
    title_slug = to_slug(title)
    summary = talk.get('Summary of your talk')

    talk_meta = OrderedDict([
        ('slug', title_slug),
        ('speaker', speaker_slug),
        ('year', 2019),
        ('title', title),
    ])

    talk_path = path.join('content/talks', f"{title_slug}.rst")
    write_rst(talk_path, talk_meta, summary)
    print(f"Written {talk_path}")

    speaker_meta = OrderedDict([
        ('slug', speaker_slug),
        ('name', speaker),
        ('image', f"{speaker_slug}.jpg"),
    ])

    speaker_path = path.join('content/speakers', f"{speaker_slug}.rst")
    write_rst(speaker_path, speaker_meta, bio)
    print(f"Written {speaker_path}")
