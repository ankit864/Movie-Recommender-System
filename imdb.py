import requests
from bs4 import BeautifulSoup
def main(max_pages = 1):
	page = 0
	count = 0	
	while page < max_pages:
		index = page * 50 + 1
		url = 'http://www.imdb.com/search/title?languages=en%7C1&num_votes=10000,&sort=user_rating,desc&start='+str(index)+'&title_type=feature'		
		print url
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text)
		for td in soup.findAll('td',{'class': 'image'},'a'):
			a = td.find('a')
			href = 'http://www.imdb.com' + a.get('href')
			get_single_item_data(href)
			count += 1
			#print count
		page+=1


def get_single_item_data(url):
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text)
	title_year = soup.find('div',{'class': 'title_wrapper'}).find('h1',{'itemprop': 'name','class': ''})
	try:
		title = title_year.contents[0].strip()
	
		year = title_year.find('span',{'id': 'titleYear'}).find('a').string
		imdbrating = soup.find('div',{'class': 'imdbRating'})
		rating_Value = imdbrating.find('div',{'class': 'ratingValue'}).find('strong').find('span',{'itemprop': 'ratingValue'}).string
		best_Rating = imdbrating.find('div',{'class': 'ratingValue'}).find('span',{'itemprop': 'bestRating'}).string
		no_of_reviews = imdbrating.find('a').find('span').string
		subtext = soup.find('div',{'class': 'subtext'})
		status = subtext.find('meta',{'itemprop': 'contentRating'})
		status_Rating = "NOT RATED"
		if not(status is None):
			status_Rating = status['content']
		duration = subtext.find('time',{'itemprop': 'duration'})
		if not(duration is None):
			duration = duration.string.strip()
		else:
			duration = ""
		genres = []
		for genre in subtext.findAll('a'):
			genersobject = genre.find('span',{'class': 'itemprop','itemprop': 'genre'})
			if not(genersobject is None):
				genres.append(genersobject.string)
		genre = ', '.join(genres)
		release_Date = subtext.find('a',{'title': 'See more release dates'}).contents[0].strip()
		image = soup.find('div',{'class': 'poster'}).find('a').find('img')
		image_Src = image['src']
		image_Alt = image['alt']
		image_Title = image['title']
		summary = soup.find('div',{'class': 'summary_text', 'itemprop': 'description'}).contents[0]
		if not(summary is None):
			summary = summary.strip()
		else:
			summary = "Not provided"	
		credit = []
		for credit_summary_item in soup.findAll('div',{'class': 'credit_summary_item'}):
			credit.append(credit_summary_item)
		directors = []
		for director in credit[0].findAll('span',{'itemprop': 'director'}):
			directors.append(director.find('a',{'itemprop': 'url'}).find('span',{'class': 'itemprop','itemprop': 'name'}).string)
		writers = []
		for writer in credit[1].findAll('span',{'itemprop': 'creator'}):
			writers.append(writer.find('a',{'itemprop': 'url'}).find('span',{'class': 'itemprop','itemprop': 'name'}).string)
		stars = []
		for star in credit[2].findAll('span',{'itemprop': 'actors'}):
			stars.append(star.find('a',{'itemprop': 'url'}).find('span',{'class': 'itemprop','itemprop': 'name'}).string)
		director = ', '.join(directors)
		writer = ', '.join(writers)
		star = ', '.join(stars)
		#print title + ',' + rating_Value
		with open('imdb.txt','a') as f:
			f.write(title + ',' + rating_Value + '\n')
		#print rating_Value
		#print writer
		#print star
		f.close()
	except:
		a=1 # just grabage value
		 
main()