# everymac-scraper

Python script that creates a comprehensive `json` database of all items listed on everymac. Please review everymac's [Terms of Use](https://everymac.com/articles/admin/termsofuse.html). It prohibits the scraping of content. By using this software, the user takes full responsibility for their actions. Please refer to the license. This software was developed purely as a proof of concept for educational purposes regarding web security. Usage of this software should be conducted in an ethical, respectful, non-commecial and legal manner.

Note that the US Court of Appeals denied LinkedIn’s request to prevent HiQ, an analytics company, from scraping its data in late 2019, effectively legalizing the scraping of uncopyrighted content. [Reference for Ruling](https://parsers.me/us-court-fully-legalized-website-scraping-and-technically-prohibited-it/). In order for a copyright to be valid, the individual(s) or corporation(s) claiming to possess the copyright must have been the first individuals to produce the item of copyright in tangible form. As much of the information hosted on everymac was produced elsewhere in some tangible form, copyrights could be debateable. 

Use your best judgement.

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
