# Libraries
import urllib as ul
import datetime
from bs4 import BeautifulSoup

# Dependencies
import config

class MetaData:
	
	# Class to handle metadata

	def __init__(self, userName='unknown user'):
		self.userName = userName
		self.startTime = None
		self.endTime = None
		self.executionTime = None
		self.pagesLoaded = []
		self.pagesLoadedCount = 0
		self.successfulTermination = False


	# Reinitialize the MetaData object (to be done after every call)
	def reinit(self):
		self = MetaData(self.userName)


	# Start Analysis
	def start_analysis(self):
		
		# automatically called when the first webpage load occurs
		# can be called manually before any website is scraped

		self.startTime = datetime.datetime.now
		self.endTime = None


	def end_analysis(self):
		
		# automatically called when publishMetaData is called after analysis has started
		# can be called manually after all the work is done

		self.endTime = datetime.datetime.now
		self.executionTime = self.endTime - self.startTime
		self.successfulTermination = True


	def write_to_file(self, metaFileName=config.metaFileName):

		# writes metadata to file
		
		with open(metaFileName, 'a') as metaFile:
			metaFile.writeline('\n')
			metaFile.write("Analysis started by " + str(self.userName) + '\n')
			metaFile.write("# startTime: " + str(self.startTime) + '\n')
			metaFile.write("# endTime: " + str(self.startTime) + '\n')
			metaFile.write("# startTime: " + str(self.startTime) + '\n')
			metaFile.write("# executionTime: " + str(self.executionTime) + '\n')
			metaFile.write("# pagesLoadedCount: " + str(self.pagesLoaded) + '\n')
			metaFile.write("# pagesLoaded:\n")

			for page in self.pagesLoaded:
				metaFile.write('    - ' + str(page) + '\n')

			metaFile.write("# successfulTermination " + str(self.successfulTermination) + ' (Early Publish)\n')


	def publishMetaData(self):

		if startTime == None:
			print "ERROR [MetaData.publishMetaData] : No Analysis has been done. Cannot write to the meta file."
			return

		else:
			self.end_analysis()
			self.write_to_file()
			self.reinit()


# Load a url and convert it to BeautifulSoup object
def url_to_soup(url, meta):
	
	if meta.startTime==None:
		meta.start_analysis()

	page = {}

	page['addinfourl'] = ul.urlopen(url)
	meta.pagesLoaded.append(url)
	meta.pagesLoadedCount += 1

	page['soup'] = BeautifulSoup(page['addinfourl'], 'lxml')

	return page