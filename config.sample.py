import logging


class Config(object):

    LOG_LEVEL = logging.DEBUG

    LOG_FILE = 'rss.log'

    RSS_FILE = 'rss.txt'

    RECIPIENTS = []

    TG_URL = 'https://api.telegram.org/bot<token>'