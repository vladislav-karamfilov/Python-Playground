import sys
import json
import requests


def check_bookmark_url(url):
    status_code = 0

    try:
        response = requests.get(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'})

        status_code = response.status_code
    except:
        print('{} - {} (Fail)'.format(url, sys.exc_info()[1]))
        return

    result = 'Success' if status_code >= 200 and status_code < 300 else 'Fail'
    print('{} - {} ({})'.format(url, status_code, result))


def check_bookmarks(bookmarks):
    for bookmark in bookmarks:
        type = bookmark['type']

        if type == 'url':
            check_bookmark_url(bookmark['url'])
        elif type == 'folder':
            check_bookmarks(bookmark['children'])
        else:
            raise ValueError('Unknown bookmark type: {}'.format(type))


def main():
    if not sys.argv or len(sys.argv) < 2:
        print('Please specify Chrome bookmarks JSON file path.')
        return

    with open(sys.argv[1], encoding='utf-8') as bookmarks_file:
        bookmarks_json = json.load(bookmarks_file)

    bookmarks_bar_bookmarks = bookmarks_json['roots']['bookmark_bar']['children']
    check_bookmarks(bookmarks_bar_bookmarks)

    other_bookmarks = bookmarks_json['roots']['other']['children']
    check_bookmarks(other_bookmarks)


if __name__ == '__main__':
    main()
