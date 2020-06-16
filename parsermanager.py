from parsers.metauaparser import MetaUaParser
from parsers.tvsettutby import TvsetTutBy
from info import Info
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring
import datetime


class ParserManager:
	def __init__(self, xmlPath):
		self.rules = self.getRulesFromXml(xmlPath)

	def getRulesFromXml(self, xmlPath):
		rules = []
		root = ET.parse(xmlPath).getroot()
		now = datetime.datetime.now()
		for page in root:
			for el in page:
				if el.tag == 'url':
					url = el.text
				elif el.tag == 'startTime':
					time = el.text.split(':')
					startDate = datetime.datetime(
						now.year, now.month, now.day, int(time[0]), int(time[1]))
				elif el.tag == 'endTime':
					time = el.text.split(':')
					endDate = datetime.datetime(
						now.year, now.month, now.day, int(time[0]), int(time[1]))
			rules.append(Info(url, startDate, endDate))
		return rules

	def parse(self):
		shows = []
		for rule in self.rules:
			parser = self.getParser(rule)
			shows.append({rule.url: parser.getRequiredShows()})
		self.printShows(shows)

	def printShows(self, elements):
		shows = Element('shows')
		for el in elements:
			page = SubElement(shows, 'page')
			url = SubElement(page, 'url')
			url.text = el
			for show in el:
				show.name = show.name.replace('\n', '').replace('\r', '')
			
	def getParser(self, info):
		uri = info.url.split('/')[2]
		if uri == 'tv.meta.ua':
			return MetaUaParser(info, False)
		if uri == 'tvset.tut.by':
			return TvsetTutBy(info, False)
