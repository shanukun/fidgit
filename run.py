import yaml

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

from routes.handler import app

app.repo = config['repo']['path']
