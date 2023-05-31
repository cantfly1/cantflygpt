from flask import Flask, request, jsonify
from youtubesearchpython import VideosSearch
from goose3 import Goose
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
from flask import render_template

# Endpoint for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint for the user interface
@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json
    prompt = data['prompt']

    # Example code for scraping YouTube video links
    if is_youtube_query(prompt):
        video_links = scrape_youtube_links(prompt)
        articles = []
    else:
        video_links = []
        articles = scrape_articles(prompt)

    # Return the results in JSON format
    return jsonify({'video_links': video_links, 'articles': articles})

# Endpoint for the API
@app.route('/api/scrape', methods=['POST'])
def api_scrape():
    data = request.json
    prompt = data['prompt']

    # Example code for scraping YouTube video links
    if is_youtube_query(prompt):
        video_links = scrape_youtube_links(prompt)
        articles = []
    else:
        video_links = []
        articles = scrape_articles(prompt)

    # Return the results in JSON format
    return jsonify({'video_links': video_links, 'articles': articles})

def is_youtube_query(query):
    # Simple check to determine if the query is more likely a YouTube video query
    return 'youtube'in query.lower()

def scrape_youtube_links(query):
    videos_search = VideosSearch(query, limit=5)
    results = videos_search.result()['result']
    video_links = [f"https://www.youtube.com/watch?v={result['id']}" for result in results]
    return video_links

def scrape_articles(query):
    url = f"https://www.bing.com/news/search?q={query}&format=rss"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    items = soup.find_all('item')
    articles = []
    for item in items:
        title = item.find('title').text
        link = item.find('link').text
        articles.append({'title': title, 'link': link})
    return articles

if __name__ == '__main__':
    app.run()
