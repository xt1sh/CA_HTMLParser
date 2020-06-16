from tvshowsparser import TvShowsParser
from parsermanager import ParserManager
from parsers.metauaparser import MetaUaParser
import datetime
from optparse import OptionParser


def main():
	manager = ParserManager('pages.xml')
	manager.parse()

main()
