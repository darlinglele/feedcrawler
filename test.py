from feedcrawler import FeedCrawler

if __name__ == '__main__':
	task = {'pool_size': 10, 'timeout':5, 'sources': [line.strip() for line in open('sites.txt')]}
	feedcrawler = FeedCrawler(task)
	print len(feedcrawler.crawl())