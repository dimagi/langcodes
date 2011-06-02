import json, os

try:
    langs
except:
    with open(os.path.join(os.path.dirname(__file__), 'langs.json')) as f:
        langs = json.load(f)

grandfathered = ('en', 'sw', 'es', 'af')

langs_by_code = {}
for lang in langs:
    if lang['two'] in grandfathered:
        langs_by_code[lang['two']] = lang
    langs_by_code[lang['three']] = lang


def get_name(lang):
    lang_info = langs_by_code.get(lang)
    if lang_info:
        return lang_info['names'][0]
    else:
        return None