from urllib.request import urlopen
from urllib.parse import quote_plus


//Enter the url that you wanna scrape
url = quote_plus('https://github.com/')


//you can also get the api by logging --> https://crawlbase.com/ 
handler= urlopen('https://api.crawlbase.com/?token=Your_Api_Here&url=' +url)

print(handler.read().decode('utf-8'))
