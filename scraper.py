from bs4 import BeautifulSoup
import requests
import string
import random
import os
import sys


threads = []


class chan_4():
    def __init__(self, url):
        self.url = url

    def scrape_it(self):
        os.chdir(sys.argv[2])

        r = requests.get(self.url)
        if r.status_code != 200:
            return

        soup = BeautifulSoup(r.content, "lxml")
        thr = soup.find_all("span", class_="summary desktop")

        for thread in thr:
            links = thread.find_all("a")
            for link in links:
                threads.append("https://boards.4channel.org/c/" + link["href"])

        self.scrape()

    def scrape(self):
        i = 0

        for x in threads:
            r = requests.get(threads[i]).text
            soup = BeautifulSoup(r, "lxml")
            img = soup.find_all("a", class_="fileThumb")

            for image in img:
                link = image["href"]
                name = "".join(random.choice(string.ascii_lowercase)
                               for _ in range(15)) + ".png"
                with open(name, "wb") as f:
                    im = requests.get("https:" + link)
                    f.write(im.content)
                    print(f"Downloading file: {name}")

            i += 1


class waifu():

    def scrape_it(self):

        sfw = ["waifu", "neko", "shinobu", "megumin", "bully", "cuddle", "cry", "hug", "awoo", "kiss", "lick", "pat", "smug", "bonk", "yeet", "blush",
               "smile", "wave", "highfive", "handhold", "nom", "bite", "glomp", "slap", "kill", "kick", "happy", "wink", "poke", "dance", "cringe"]

        while True:
            random_sfw = random.choice(sfw)
            r = requests.get(f"https://api.waifu.pics/sfw/{random_sfw}").text
            json_data_sfw = r.json()

            url_sfw = json_data_sfw["url"]

            name = "".join(random.choice(string.ascii_lowercase)
                           for _ in range(15)) + ".png"
            with open(name, "wb") as f:
                im = requests.get(url_sfw).text
                f.write(im.content)
                print(f"Downloading file: {name}")


def main():
    if sys.argv[4] == "4chan":
        i = 0
        for _ in range(11):
            chan_4(f"https://boards.4channel.org/c/{i}").scrape_it()
            i += 1
    elif sys.argv[4] == "waifu":
        waifu().scrape_it()
