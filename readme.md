#### Feed Your Application
Fetch rss content from multiple rss urls and send to telegram by bot or to any application you want. You can add as many as rss urls to the application.

#### Installation
<pre>
- pip3 install -r package.txt or pip3 install feedparser==5.2.1
</pre>

#### Basic Configuration
Copy `config.sample.py` to `config.py`. Inside `config.py` enter your necessary information

#### Add new RSS Link
<pre>
python rss.py your-feed-url

python rss.py -h
usage: rss.py [-h] url
</pre>

#### Get news from rss
<pre>
python send.py
</pre>

#### RSS
- rss.py: A group of methods and script to add new rss url
- rss.txt: File to store rss url
- rss.log: Log file

You can customize the way you send rss content to telegram or to any application. You can read rss contents by importing `get_rss_from_url()` function from `rss.py`