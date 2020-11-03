from django.shortcuts import render
from trial import NewsDataScraper
from django.http.response import JsonResponse
from django.http import HttpResponse
from .models import scrapingArticles

# Create your views here.


def homepage(request):
    return render(request= request, 
                  template_name= "main/home.html" , #main?walla scrapinArticles 3ala esm l folder
                   context= {"sactapedData": scrapingArticles.object.all})



class ArticleAdmin(admin.ModelAdmin):


    actions = ['scrap_data']
	
    def scrap_data (self, request, queryset):
        # 1 - data of articles should be returned here
        queryset.update(status='p')
        scraper = NewsDataScraper();
        cnn_paper = scraper.scrap();
        # 2 - then we should do something like this inside loop ( depends on the data)
        for scraped_article in cnn_paper.articles:
            article = scrapingArticles()
            article.url = scraped_article.url
            article.title =  scraped_article.title
            article.text =  scraped_article.text
            article.summary = scraped_article.summary                  
            article.keywords = scraped_article.keywords
            article.save()

        # scraped_data.short_description = "Mark data as scraped"
        # yalla smy w dwry el maknaa ( run el project)
