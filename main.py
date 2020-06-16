from parsermanager import ParserManager
from config import USE_GEVENT
import time

def main():
	manager = ParserManager('pages.xml', USE_GEVENT)
	manager.parse()
main()
