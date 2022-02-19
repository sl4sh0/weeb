import argparse
from scraper import *


def start():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-dir", help="Name of directory or folder where to save images.", required=True)
    parser.add_argument(
        "-name", help="Name of site u want to scrape from. 4chan or waifu", required=True)
    main()


start()
