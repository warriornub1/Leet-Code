class Codec:
    
    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self.base = "http://tinyurl.com/"
    
    def encode(self, longUrl):
        
        if longUrl not in self.encodeMap:
            shortUrl = self.base + str(len(longUrl))
            self.encodeMap[longUrl] = self.base + str(len(longUrl) + 1)
            self.decodeMap[shortUrl] = longUrl
        return self.encodeMap[longUrl]
        

    def decode(self, shortUrl):
        return self.decodeMap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.encode("www.youtube.com/happy"))
print(codec.decode("http://tinyurl.com/21"))