from parsermanager import ParserManager
from config import USE_GEVENT
import time

def main():
	now = time.time()
	manager = ParserManager('pages.xml', True)
	manager.parse()
	print(time.time() - now)
	now = time.time()
	manager = ParserManager('pages.xml', False)
	manager.parse()
	print(time.time() - now)

main()
