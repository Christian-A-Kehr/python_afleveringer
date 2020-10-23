import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

def works():
    print("works")

# exc 1.1: init(self, url_list)
class BookHandler:
     
    def __init__(self, url_list):
        """Class may need a name"""
        self.url_list = url_list
        
# exc 1.2: download(url,filename) raises NotFoundException when url returns 404
    def download(self, url,filename):
        """ Takes an url input and an output file and write the content of the input file into a list, 
    the console or to the output file.
     
    Parameters:
    url: The URL where the fill can be found
    filenmae: The name of the file where the url content will be placed  
    """
        r = requests.get(url)
        if(r.status_code == 404):
            raise Exception("Unable to establish conection")
        with open(filename, 'w+') as subject:
            subject.write(r.text)

    # exc 1.3: multi_download() uses threads to download multiple urls as text and stores filenames as a property
    def multiple_download(self):
        """ """
        self.files = []
        executor = ThreadPoolExecutor(len(self.url_list))
        for idx, url in enumerate(self.url_list):
            filename = 'Subject'+str(idx)+'.txt'
            self.files.append(filename)
            executor.submit(self.download(url, filename))
    
    # exc 1.4. iter() returns an iterator
    def __iter__(self):
        self.current_index = 0
        return self

    # exc 1.5. next() returns the next filename (and stops when there are no more)
    def __next__(self):
        if self.current_index > len(self.files) - 1:
            raise StopIteration  # signals "the end"
        result = self.files[self.current_index]
        self.current_index += 1
        return result

    # exc 1.6. urllist_generator() returns a generator to loop through the urls
    def urllist_generator(self):
        for url in self.url_list:
            yield url

    # exc 1.7. avg_vowels(text) - a rough estimate on readability returns average number of vowels in the words of the text
    def avg_vowels(self, text):
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        with open(text, 'rt') as fd:
            data = fd.read()
            words = data.split()
            count = 0
            for word in words:
                lower = word.lower()
                for i in range(0, len(lower)):
                    if lower[i] in vowels:
                        count += 1
            return {text: count / len(words)}

    # 8. hardest_read() returns the filename of the text with the highest vowel score (use all the cpu cores on the computer for this work.
    def hardest_read(self):
        executor = ProcessPoolExecutor(multiprocessing.cpu_count())
        with ProcessPoolExecutor(multiprocessing.cpu_count()) as ex:
            res = ex.map(self.avg_vowels, self.files)
        result = {k: v for d in res for k, v in d.items()}
        result_sorted = {k: v for k, v in sorted(
            result.items(), key=lambda item: item[1], reverse=True)}
        return next(iter(result_sorted.items()))