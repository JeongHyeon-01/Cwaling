import requests
from bs4 import BeautifulSoup
import pandas as pd

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
req = requests.get('https://www.melon.com/chart/week/index.htm', headers = header)

# HTML Parsing
html = req.text
soup = BeautifulSoup(html, 'html.parser')

# 응답 상태 코드(response status code) 출력: 200출력
req.status_code
req.headers
# {'Content-Encoding': 'gzip', 'Date': 'Fri, 21 Jan 2022 03:29:10 GMT', 'Content-Length': '36508', 'Accept-Ranges': 'bytes', 'ETag': '"0:8e9c"', 'Content-Type': 'text/html;charset=utf-8', 'Cache-Control': 'no-cache', 'Connection': 'Keep-Alive'}
req.encoding
# UTF-8


# select이용

rank = soup.select('tr.lst50 > td > div.wrap.t_center > span.rank')
music = soup.select('div.wrap > div.wrap_song_info > div.ellipsis.rank01 > span > a')
musiction = soup.select('div.wrap > div.wrap_song_info > div.ellipsis.rank02 > span > a')


results= []

for i in range(50):
    results.append([rank[i].text,music[i].text,musiction[i].text])


df = pd.DataFrame(results)
df.columns = ["순위","노래제목","가수"]
df.to_excel('./melon.xlsx')
