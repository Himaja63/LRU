import os
class LRU : 

    cache = {}
    freq = {} 
    cache_capacity = 0
    def __init__(self, MAX_CAPACITY) :

        self.cache_capacity = MAX_CAPACITY

    def put(self, uri, data) :
        if uri not in self.cache.keys() :
            if len (self.cache) == self.cache_capacity :
                x = sorted(self.freq.items(), key = lambda item : item[1])[0]
                key = x[0][:]
                del self.cache[key]
                del self.freq[key]
            self.cache[uri] = data
            self.freq[uri] = 0
    
    def get(self, uri) :
        try :
            self.freq[uri] += 1        
            return self.cache[uri]

        except :
            return None

    def get_cache(self) :        
        return self.cache

def main() :
    
    obj = LRU(5)

    assert (obj.get("1")) == None

    for file in os.listdir() :
        if file.startswith("file") :
            data = open(file, "r").read()
            obj.put(file, data)

    assert (obj.get("file1.txt")) == "This is First file."
    assert (obj.get("file2.txt")) == "This is Second file."
    assert (obj.get("file3.txt")) == "This is Third file."
    assert (obj.get("file4.txt")) == "This is Fourth file."
    assert (obj.get("file5.txt")) == "This is Fifth file."
    obj.put("1",2)
    assert(obj.get("file1.txt")) == None
    obj.put("2",3)
    obj.put("3",4)
    assert(obj.get("1")) == None
    assert(obj.get("2")) == None


