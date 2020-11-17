# NewsScraper
A news scraper made using Django- MongoDB- newspaper in python

The goal of this coding challenge is to create a solution that crawls for articles from a news website, cleanses the response, stores it in a mongo database, then makes it available to search via an API.

## Specifications

- Write an application to crawl articles on a news website such as [theguardian.com](http://theguardian.com) or [bbc.com](http://bbc.com/) using a crawler framework such as [Scrapy](http://scrapy.org). You can use a crawl framework of your choice and build the application in Python.
- The application should cleanse the articles to obtain only information relevant to the news story, e.g. article text, author, headline, article url, etc. 

- Store the data in a hosted Mongo database, e.g. [MongoDB Atlas](https://www.mongodb.com/cloud/atlas), for subsequent search and retrieval. Ensure the URL of the article is included to enable comparison to the original.
- Write an API that provides access to the content in the mongo database.
- Bonus: The user should be able to search the articles' text by keyword.

