import json
import requests
from win32com.client import Dispatch
def genNews():
    api ="563b86e1120b463c9b33bb1f8ee9c6ec"
    news = "https://newsapi.org/v2/top-headlines?country=in&apiKey="
    # http://newsapi.org/v2/everything?q=bitcoin&from=2020-07-14&sortBy=publishedAt&apiKey=
    r = requests.get(f"{news}{api}")
    news = json.loads(r.text)
    print(news)
    i=10
    if news["totalResults"]<10:
        i=news["totalResults"]
    for s in range(i):
        n=news["articles"][s]["title"]
        print(news["articles"][s]["title"])
        yield f" News {s+1}:{n}"



def read(string):
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(string)
g=genNews()
for lat in g:
    read(lat)