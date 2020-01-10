import feedparser, random, json
import logging, argparse
from config import Config
from urllib import request, parse
from urllib.request import Request


logging.basicConfig(filename=Config.LOG_FILE, level=Config.LOG_LEVEL, format='%(asctime)s:%(message)s')

'''
Add new rss url to file
'''
def add_rss(rss_link: str) -> None:
    rss = get_rss()
    with open(Config.RSS_FILE, 'a') as f:
        if rss and rss_link in rss:
            logging.warning('Rss link already exists')
            print('Rss link already exists')
        else:
            f.write('{}\n'.format(rss_link))
            logging.info('Rss link added')
            print('Rss link added')

'''
This function will read all rss url from file and convert to a list
'''
def get_rss():
    rss_links = []
    with open(Config.RSS_FILE) as rss:
        lines = rss.readlines()
        if lines:
            for line in lines:
                rss_links.append(line.strip())

    return rss_links

'''
Function to read content from rss url.
This will pop randomized content from the list.
'''
def get_rss_from_url():
    feed_url = get_rss()
    random.shuffle(feed_url)
    rss_link = feed_url.pop()
    logging.info('fetch from %s', rss_link)
    rss = feedparser.parse(rss_link)
    random.shuffle(rss['items'])
    item = {}
    if rss['items']:
        item = rss['items'].pop()

    return item

if __name__ == '__main__':
    # Adding new rss url
    parser = argparse.ArgumentParser(description='Add new rss url')
    parser.add_argument('url', type=str, help='Enter rss url')
    args = parser.parse_args()

    try:
        req = Request(url=args.url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'
        })
        request.urlopen(req)
        add_rss(args.url)
    except ValueError as e:
        logging.error(e)
        print(e)