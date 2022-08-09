import requests
from bs4 import BeautifulSoup

SITE_URL = "http://www.mai-net.net"
BASE_URL = f"{SITE_URL}/bbs/sst/sst.php?act=dump&cate=tiraura&all=24734&n=1#kiji"

headlines = BeautifulSoup(requests.get(url=BASE_URL).text, "html.parser").find_all(name="a")
for headline in headlines:
    page_title = headline.text
    page_url = headline.get("href")
    page_html = BeautifulSoup(requests.get(url=f"{SITE_URL}{page_url}").text, "html.parser")

    body = page_html.find(name="div")
    body_text = str(body).replace("<br/>", "\n").replace('<div style="line-height:1.5">', "").replace("</div>", "")

    with open("youjo.txt", "a", encoding="utf-8") as file:
        file.write(f"{page_title}\n\n\n\n\n")
        file.write(f"{body_text}\n\n\n\n\n")

    if headline.text == "第一〇〇話":
        break
