import json, os

try:
    langs
except:
    with open(os.path.join(os.path.dirname(__file__), 'langs.json')) as f:
        langs = json.load(f)