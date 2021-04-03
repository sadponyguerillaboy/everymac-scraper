# everymac-scraper

Python script that creates a comprehensive `json` database of all items listed on everymac. Please review everymac's [Terms of Use](https://everymac.com/articles/admin/termsofuse.html). It prohibits the scraping of content. By using this software, the user takes full responsability for their actions. Please refer to the license. This software was developed purely as a proof of concept for educational purposes. Usage of this software should be conducted in an ethical, respectful, non-commecial manner and legal manner.

__Requirements:__
```
bs4
pandas
requests
urllib3
```

__Usage:__
```
python scraper.py
```

__Notes:__

The only item that is not currently added to the database is the eMate 300. Its specs page is differently formated from everything else on the site and incompatible with the scrapers algorithm.
