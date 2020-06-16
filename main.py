from tvshowsparser import TvShowsParser
from parsermanager import ParserManager
from parsers.metauaparser import MetaUaParser
import datetime
from optparse import OptionParser
from config import USE_GEVENT

def main():
	if not USE_GEVENT:
		manager = ParserManager('pages.xml')
		manager.parse()

main()
