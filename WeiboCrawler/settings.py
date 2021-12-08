# -*- coding: utf-8 -*-

# Scrapy settings for WeiboCrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'WeiboCrawler'

SPIDER_MODULES = ['WeiboCrawler.spiders']
NEWSPIDER_MODULE = 'WeiboCrawler.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
DOWNLOAD_TIMEOUT = 15
# # Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 100
# # The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 100
CONCURRENT_REQUESTS_PER_IP = 100

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
    'Connection': 'keep-alive',
    'Host': 'm.weibo.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'cookie':'SINAGLOBAL=8396480745870.702.1629344875926; UOR=,,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWPa.-0RzXGeWKl81m.yj8a5JpX5KMhUgL.FoqcS0qES0z7SKq2dJLoI7yzqPUuPfUad7tt; ALF=1670481023; SSOLoginState=1638945023; SCF=AsYu0FpoLKy28dB8QVglCVg3nqDJ3fgOngVhRvDIHijOGdmdWuxrtdlfmeJ6ajV-fDIsdtvSbp-YhTVX2PUSiFQ.; SUB=_2A25MtCFQDeRhGeBI7FQT9yzMzjqIHXVvwBWYrDV8PUNbmtB-LRL1kW9NRmAOvxXtz52eUlLfUG6CJ594Ub5YgL5z; XSRF-TOKEN=NTPFVr3hm1ziIC8gW6z3vArH; _s_tentry=weibo.com; Apache=3268797215588.175.1638960794186; ULV=1638960794215:4:2:1:3268797215588.175.1638960794186:1638346355970; WBPSESS=2EZTIvKcOVdUgDai4s3weNw02S4fHWjFYA46P7jXGxAkjrvvv92QqZuyz_mkbj5S0V-5C4DERelQ7Zo0DV7DwxjmhD3_doMnKFDYBWwQYrdgoZM8X0mzSys4aDNGQlcUbL1HQOcSDBrjFMvDypOWWg=='
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'WeiboCrawler.middlewares.IPProxyMiddleware': 100,
    'WeiboCrawler.middlewares.TooManyRequestsRetryMiddleware': 543,
}
RETRY_HTTP_CODES = [429, 418, 502]

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'WeiboCrawler.pipelines.WeibocrawlerPipeline': 300,
    # 'WeiboCrawler.pipelines.MongoPipeline': 400,
}
# MONGO_URI = 'localhost'
# MONGO_DB = 'weibo'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# # 图片存储目录
# IMAGES_STORE = 'images/'
# ITEM_PIPELINES = {
#    'WeiboCrawler.pipelines.ImagesnamePipeline': 300,
# }
