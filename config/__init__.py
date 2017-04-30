import yaml

with open('config/application.yaml', 'r') as f:
    app_config = yaml.load(f)

config_db = app_config['database']
