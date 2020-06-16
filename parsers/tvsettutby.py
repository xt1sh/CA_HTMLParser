from tvshowsparser import TvShowsParser
from show import Show
from time import strptime
import datetime


class TvsetTutBy(TvShowsParser):
	def getAllShows(self):
		shows = []
		programs = self.htmlParser.findAll('li', {'class': 'programm-event'})
		now = datetime.datetime.now()
		for program in programs:
			time = program.find('div', {'class': 'event-time'}).find('a').text
			name = program.find('div', {'class': 'event-title'}).text
			hm = time.split(':')
			hour = int(hm[0])
			minute = int(hm[1])
			shows.append(Show(datetime.datetime(
				now.year, now.month, now.day, hour, minute),
				name))
		return shows
