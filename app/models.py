class Source_data:
    
    def __init___ (self, id, name,url):

        self.id = id
        self.name = name
        self.url = url

class Articles_data:

    def __init__(self, id, name, author, url, urlToImage, publishedAt):

        self.id = id
        self.name = name
        self.author = author
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
