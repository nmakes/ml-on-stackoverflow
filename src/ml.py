import scrapper
import config

meta = scrapper.MetaData()

def get_all_featured_questions(meta):
	
	featuredPage = scrapper.url_to_soup(config._featured, meta)
	fpSoup = featuredPage['soup']

	allLinks = fpSoup.find_all('a')

	
	
	# for url in questionUrls:
	# 	scrapper.url_to_soup(url, meta)

get_all_featured_questions(meta)