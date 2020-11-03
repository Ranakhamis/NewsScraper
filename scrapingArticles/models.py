from __future__ import unicode_literals
from django.db import models
from djongo import models

# Create your models here.

class scrapingArticles(models.Model): #collection name
   
    #Documents
    url = models.URLField()
    title=  models.TextField()
    text =  models.TextField()
    summary= models.TextField()                     
    keywords= models.TextField()
    def __str__(self):
		    return self.title


#models should orm db, so tables in db are defined as objects
#aro7 3al views a3mel import lel model ba3daha a3mel append lel data gowah
