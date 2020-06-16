from bs4 import BeautifulSoup
import urllib


class TvShowsParser:
	def __init__(self, showInfo, withGevent):
		self.showInfo = showInfo
		if withGevent:
			self.getHtmlWithGevent()
		else:
			self.getHtmlWithoutGevent()

	def getHtmlWithoutGevent(self):
		req = urllib.request.Request(self.showInfo.url)
		with urllib.request.urlopen(req) as response:
			html = response.read()
		self.htmlParser = BeautifulSoup(html, 'html.parser')

	def getHtmlWithGevent(self):
		return

	def getRequiredShows(self):
		shows = self.getAllShows()
		if (shows is None or len(shows) == 0):
			print('No shows were found')
			return
		requiredShows = []
		for show in shows:
			if (show.startTime >= self.showInfo.startTime and
				show.startTime <= self.showInfo.endTime):
				requiredShows.append(show)
		if len(requiredShows) == 0:
			print(f'No shows between {self.showInfo.startTime} ' +
				'and {self.showInfo.endTime} were found')
		return requiredShows

	def getAllShows(self):
		raise NotImplementedError
