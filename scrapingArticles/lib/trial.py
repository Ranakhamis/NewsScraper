import newspaper 
from newspaper import fulltext
import newspaper 
from newspaper import article
import nltk
# The punkt of nltk library is used to tokenize the sentences in order to be used for NLP. So we need to download punkt sentence tokenizer.
#nltk.download('punkt')

class scrap: 
    def __init__(self):
        cnn_paper = newspaper.build('http://cnn.com' ) 

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
        print(cnn_article.top_image)

        print("Article Title:") 
        print(cnn_article.title) #prints the title of the article
        print("\n") 
        print("Article Text:") 
        print(cnn_article.text) #prints the entire text of the article
        print("\n") 
        print("Article Summary:") 
        print(cnn_article.summary) #prints the summary of the article
        print("\n") 
        print("Article Keywords:")
        print(cnn_article.keywords) #prints the keywords of the article



        file1=open("NewsFile.txt", "w+")
        file1.write("Title:\n")
        file1.write(cnn_article.title)
        file1.write("\n\nArticle Text:\n")
        file1.write(cnn_article.text)
        file1.write("\n\nArticle Summary:\n")
        file1.write(cnn_article.summary)
        file1.write("\n\n\nArticle Keywords:\n")
        keywords='\n'.join(cnn_article.keywords)
        file1.write(keywords)
        file1.close()
    
    
