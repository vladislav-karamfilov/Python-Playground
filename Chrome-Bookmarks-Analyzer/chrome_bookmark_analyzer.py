from pprint import pprint
from urllib.parse import urlparse
import json
import sys


def add_to_url_folder_mappings(url, folder, url_folder_mappings, ignore_protocol_and_fragment):
    if ignore_protocol_and_fragment:
        parsed_url = urlparse(url)
        actual_url = parsed_url.netloc + parsed_url.path + '?' + parsed_url.query
    else:
        actual_url = url

    if actual_url in url_folder_mappings:
        if folder in url_folder_mappings[actual_url]:
            url_folder_mappings[actual_url][folder] += 1
        else:
            url_folder_mappings[actual_url][folder] = 1
    else:
        url_folder_mappings[actual_url] = {folder: 1}


def populate_url_folder_mappings(bookmarks_json, folder, url_folder_mappings):
    if bookmarks_json['type'] == 'url':
        add_to_url_folder_mappings(
            bookmarks_json['url'], folder, url_folder_mappings, True)
        # add_to_url_folder_mappings(
        #     bookmarks_json['name'], folder, url_folder_mappings, True)
        return

    if bookmarks_json['type'] != 'folder':
        print('Unknown type: {}'.format(bookmarks_json['type']))
        return

    for child in bookmarks_json['children']:
        populate_url_folder_mappings(
            child, bookmarks_json['name'], url_folder_mappings)


def main():
    if not sys.argv or len(sys.argv) < 2:
        print('Please specify Chrome bookmarks JSON file path.')
        return

    with open(sys.argv[1], encoding='utf-8') as bookmarks_file:
        bookmarks_json = json.load(bookmarks_file)

    url_folder_mappings = {}

    populate_url_folder_mappings(
        bookmarks_json['roots']['bookmark_bar'], 'bookmark_bar', url_folder_mappings)
    populate_url_folder_mappings(
        bookmarks_json['roots']['other'], 'other', url_folder_mappings)

    print('Bookmarks count: {}'.format(len(url_folder_mappings)))
    pprint(url_folder_mappings)


if __name__ == '__main__':
    main()
