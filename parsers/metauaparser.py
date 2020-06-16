from tvshowsparser import TvShowsParser
from show import Show
import urllib.request
from time import strptime
import datetime


class MetaUaParser(TvShowsParser):
	def getAllShows(self):
		shows = []
		main = self.htmlParser.find(id = 'main')
		children = main.findChildren('table')
		now = datetime.datetime.now()
		for child in children:
			tr = child.findChildren('tr', recursive = False)[1]
			td = tr.findChildren('td', recursive = False)
			for i in range(len(td)):
				div = td[i].findChildren('div', recursive = False)
				for j in range(len(div)):
					info = div[j].findChildren('div', recursive = False)
					hm = info[0].text.split(':')
					name = info[1].text
					hour = int(hm[0])
					minute = int(hm[1])
					shows.append(Show(datetime.datetime(
						now.year, now.month, now.day, hour, minute),
						name))
		return shows
