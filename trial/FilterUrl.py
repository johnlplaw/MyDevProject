import re

urls = [
'https://twitter.com/PACU_PMO/status/1744147923389260235',
'https://twitter.com/PACU_PMO/status/1744147923389260235/analytics',
'https://twitter.com/sravin10/status/1744748680799023253',
'https://twitter.com/sravin10/status/1744748680799023253/analytics',
'https://twitter.com/JPenerangan/status/1745029323743207602/photo/1'
]

for url in urls:
    x = re.search("/analytics", url)
    y = re.search('/photo/*', url)
    #print(x)
    #print(y)
    if x is None and y is None:
        print(url)