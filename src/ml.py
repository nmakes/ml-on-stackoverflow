import scraper
import config

meta = scraper.MetaData()

def get_all_featured_questions(meta):
	
	featuredPage = scraper.url_to_soup(config._featured, meta)
	fpSoup = featuredPage['soup']

	allLinks = fpSoup.find_all('a')


	
	# for url in questionUrls:
	# 	scraper.url_to_soup(url, meta)

get_all_featured_questions(meta)