import Crawler
import Tests
import Scraper
import json


def main():
    # test scraping 1 discussion from early onset json
    fpath = r'C:\Users\wslam\Everything\machine-learning\dementia-bot\src\data\crawler_output\ad_connect\crawled_ad_connect_early_onset.json'
    out_path = r'C:\Users\wslam\Everything\machine-learning\dementia-bot\src\data\scraped\ad_connect\scraped_ad_connect_early_onset.jsonl'
    discussions = Scraper.scrape_ad_connect(fpath)
    Scraper.save_scraped_ad_connect(discussions=discussions, save_destination=out_path)


if __name__ == "__main__":
    main()
