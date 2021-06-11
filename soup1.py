from bs4 import BeautifulSoup

with open("https://site-avinash-nandakumar.mystrikingly.com/") as fp:
    soup = BeautifulSoup(fp, "html.parser")