from flask import Flask
from flask_github import GitHub

app = Flask(__name__)
app.config['GITHUB_CLIENT_ID'] = 'repo-token'
app.config['GITHUB_CLIENT_SECRET'] = 'leaflet-secret'
app.cconfig['AUTH0_PYTHON_CLIENT_ID'] =  'AUTH0_PYTHON_CLIENT_ID'

# For GitHub Enterprise
# app.config['GITHUB_BASE_URL'] = 'https://HOSTNAME/api/v3/'
# app.config['GITHUB_AUTH_URL'] = 'https://HOSTNAME/login/oauth/'

github = GitHub(app)

app = Flask(__name__)

@app.route('/')
def index():
    start_coords = (46.9540700, 142.7360300)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/')
def hello_world():
    return 'Polígonos App'
