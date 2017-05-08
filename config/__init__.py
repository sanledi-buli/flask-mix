import yaml

with open('config/application.yaml', 'r') as f:
    config = yaml.load(f)

config_db = config['database']
config_app = config['application']
