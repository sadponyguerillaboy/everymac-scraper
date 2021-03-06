# everymac-scraper

Python script that creates a comprehensive `json` database of all items listed on everymac. Please review everymac's [Terms of Use](https://everymac.com/articles/admin/termsofuse.html). It prohibits the scraping of content. By using this software, the user takes full responsibility for their actions. Please refer to the included license. This software was developed purely as a proof of concept for educational purposes regarding web security. Usage of this software should be conducted in an ethical, respectful, non-commecial and legal manner.

Note that the US Court of Appeals denied LinkedIn’s request to prevent HiQ, an analytics company, from scraping its data in late 2019, effectively legalizing the scraping of publically accessible content. [Reference for Ruling](https://parsers.me/us-court-fully-legalized-website-scraping-and-technically-prohibited-it/), [Legal Docs](https://cases.justia.com/federal/appellate-courts/ca9/17-16783/17-16783-2019-09-09.pdf?ts=1568048483)

Use your best judgement.

__Requirements:__
```
bs4
fake-useragent
pandas
lxml
requests
urllib3
```

__Usage:__
```
python scraper.py
```

__Notes:__

The only item that is not currently added to the database is the eMate 300. Its specs page is differently formated from everything else on the site and incompatible with the scrapers algorithm.
