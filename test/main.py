from flask import Flask, render_template, request
import openai
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)
openai.api_key = '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'
def scrape_articles(query):
    search_query = f"stratégies marketing {query}"
    url = f"https://www.bing.com/news/search?q={search_query}&format=rss"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    items = soup.find_all('item')
    articles = []
    for item in items:
        title = item.find('title').text
        link = item.find('link').text
        articles.append({'title': title, 'link': link})
    return articles

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/chat', methods=['POST'])
def chat():
    project_objective = request.form['project_objective']
    brand_name = request.form['brand_name']
    brand_sector = request.form['brand_sector']
    articles = scrape_articles(project_objective)
    prompt  = f"Provide me with a metaverse strategy for the following project:\n\n'{project_objective}'.\n\nThe brand is '{brand_name}' (secteur: '{brand_sector}')”.First, create 5 distinc plans, the 5 plan follow following the AARRR framework, on how you would approach this metaverse strategy. After that, Choose 3 relevant metaverse plateform for the bestmetaverse strategy.after create a table with all themetaverse  platform proposed plans and rate them all from 0-100 rating their engagement coherence, and practicality (based on your language model abilities) which you would prefer. "
    for article in articles:
        prompt += f"- {article['title']}\n  {article['link']}\n"
    prompt += f"\nThe brand is '{brand_name}' (secteur: '{brand_sector}')"
    

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt ,
        max_tokens=2400,
        n=1,
        stop=None,
        temperature=0.7
    )
    
    output = response.choices[0].text.strip()
    return render_template('index.html', output=output)
if __name__ == '__main__':
    app.run(debug=True)