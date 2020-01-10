import feedparser, random, json
from urllib import parse, request
from config import Config
from rss import get_rss_from_url
import logging


logging.basicConfig(filename=Config.LOG_FILE, level=Config.LOG_LEVEL, format='%(asctime)s:%(message)s')

item = get_rss_from_url()

if item:
    logging.info('fetch content with url: %s', item['link'])
    for chat_id in Config.RECIPIENTS:
        try:
            payload = {
                'chat_id': chat_id,
                'text': '<b>{}</b>\n\n{}\n{}'.format(item['title'], item['summary'], item['link']),
                'parse_mode': 'html'
            }

            tg_url = '{}/{}'.format(Config.TG_URL, 'sendMessage')
            
            tg = parse.urlencode(payload).encode('ascii')
            tg_resp = request.urlopen(url=tg_url, data=tg)
            resp = json.loads(tg_resp.read().decode('utf-8'))
            if not resp['ok']:
                logging.error(resp)
            else:
                logging.info('Sent success.')
        except (Exception) as e:
            logging.error(e)

else:
    logging.info('No rss feed available!')
