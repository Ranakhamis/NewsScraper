import newspaper 
from newspaper import fulltext
import newspaper 
from newspaper import article
import nltk
# The punkt of nltk library is used to tokenize the sentences in order to be used for NLP. So we need to download punkt sentence tokenizer.
#nltk.download('punkt')

cnn_paper = newspaper.build('http://bbc.com' ) 

class NewsDataScraper:
    # function to scrap data from modern newspapers
    def scrap(self):
        # get list of article URLs
        #for paper in cnn_paper:
        for article in cnn_paper.articles:
            print(article.url)
    
        #category
        for category in cnn_paper.category_urls():
            print(category)

        cnn_article = cnn_paper.articles[0]
        cnn_article.download()
        cnn_article.parse()
        cnn_article.nlp()
        ########################################################
        title = cnn_article.title
        text = cnn_article.text
        summary = cnn_article.summary
        keywords = cnn_article.keywords
       
        
        ##############################################################
        print("Article Title:", title , "\n") 
        print("Article Text:", text ,"\n" ) 
        print("Article Summary:", summary ,"\n") 
        print("Article Keywords:" , keywords ,"\n")

        ###################################################################
        file1=open("NewsFile.txt", "w+")
        file1.write("Title:\n", cnn_article.title )
        file1.write("\n\nArticle Text:\n",cnn_article.text )
        file1.write("\n\nArticle Summary:\n",cnn_article.summary)
        keywords='\n'.join(cnn_article.keywords)
        file1.write("\n\n\nArticle Keywords:\n", keywords) 
        file1.close()

        return cnn_paper

if __name__ == "__main__":
    pass