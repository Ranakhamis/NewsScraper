from django.contrib import admin
from .models import scrapingArticles
# Register your models here.


class Scrap_Admin(admin.ModelAdmin):
    fields = ["article_url" , 
              "article_title", 
              "article_text",
              "article_summary" ,
              "article_keywords",]


admin.site.register(scrapingArticles) #Scrap_Admin)

