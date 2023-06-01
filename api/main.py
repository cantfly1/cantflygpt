
from flask import Flask, request, jsonify,render_template
import openai

app = Flask(__name__)
openai.api_key = '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'
#add index.hmlt
async def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

@app.route('/generate', methods=['POST'])
def generate_prompt():
    data = request.get_json()
    brand_sector = data['brandSector']
    brand_name = data['brandName']
    project_objective = data['projectObjective']

    prompt = f"Provide me with a metaverse strategy for the following project: Brand Sector: {brand_sector}\nBrand Name: {brand_name}\nProject Objective: {project_objective}First, create 5 distinc plans, the 5 plan follow following the AARRR framework, on how you would approach this metaverse strategy. After that, Choose 3 relevant metaverse plateform for the bestmetaverse strategy.after create a table with all themetaverse platform proposed plans and rate them all from 0-100 rating their engagement coherence, and practicality (based on your language model abilities) which you would prefer. "

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=200,
    )

    return jsonify({'response': response.choices[0].text.strip()})

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=8080)
