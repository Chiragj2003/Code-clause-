# pyshorteners is a Python lib to help you short and expand urls using the most famous URL Shorteners availables
import pyshorteners

url = input("enter the url: ")

def shortenurl(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))
    
shortenurl(url)