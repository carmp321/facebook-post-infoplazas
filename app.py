from flask import Flask, render_template, request
import requests
from datetime import datetime
from collections import Counter

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = {}
    error = None

    if request.method == 'POST':
        token = request.form['token']
        page_id = request.form['page_id']

        url = f'https://graph.facebook.com/v18.0/{page_id}/posts'
        params = {
            'access_token': token,
            'fields': 'id,message,created_time',
            'limit': 100
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()

            if 'data' not in data:
                raise Exception(data.get('error', {}).get('message', 'Error desconocido'))

            conteo = Counter()
            for post in data['data']:
                fecha = datetime.fromisoformat(post['created_time'].replace('Z', '+00:00'))
                clave = fecha.strftime('%Y-%m')
                conteo[clave] += 1

            result = dict(sorted(conteo.items()))
        except Exception as e:
            error = str(e)

    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
