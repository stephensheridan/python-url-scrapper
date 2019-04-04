# python-url-scrapper

# Summary
Python script that uses curl and grep along with regex to scrape URLS from the Alexa top 1 million or Cisco top 1 million.

# Description
This script iterates through the Alexa top 1 million or similar CSV file and scrapes URL's by parsing anchor href tags from the first the first level of each entry in the Alexa top 1 million. The script relies on curl, grep and regex in order to pull content and parse out the href tags.

# Example curl command piped to grep along with regex 
curl -L --max-time 10 www.yahoo.com | grep -oE 'href=\"(\S*)'

The script uses a Python set to store URL's retrieved from the curl command. This ensures that only unique URL's are stored. Approximately 13,066 URL's are returned from the first 150 entries in the Alexa top 1 million.

# Usage
python url_scrapper <input_file> <output_file> <num_pages_to_scrape>

# Input file
The input file must have the following format:

1,google.com
2,facebook.com
3,youtube.com
4,baidu.com
5,yahoo.com
6,amazon.com
7,wikipedia.org
8,qq.com
9,twitter.com
10,google.co.in
...

# Output file
The output file generated will have the following format:

0,https://xhamster.com/channels/private-society
1,https://www.microsoft.com/en-us/store/locations/find-a-store?icid=en-us_UF_FAS
2,http://food.china.com.cn/2019-04/04/content_74645676.htm
3,https://www.snapdeal.com/products/jewellery-fashion?q=hpsaScore_tf1%3A1%7C&sort=plrty
4,http://french.alibaba.com
5,https://educacao.uol.com.br/biografias/
6,https://www.snapdeal.com/products/mobiles-wearables-smartwatches
7,http://community.ebay.com/t5/Groups/ct-p/Groups
8,https://autofinance.chase.com/auto-finance/home?offercode=WDXDPXXX03&referrer_id=ZJPM000021546
9,https://abs.twimg.com/a/1554171232/icons/favicon.svg
10,https://aws.amazon.com/ru/?nc1=f_ls
...

# Referencing this work and dataset
Please use the following format when using and referencing this work.

Sheridan, S. (2019). Universal Resource Locators scrapped from Alexa Top 1 million websites. https://github.com/stephensheridan/python-url-scrapper

