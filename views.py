from collections import defaultdict
from django.http import HttpResponse
import json
from langcodes import langs as all_langs

code_key = defaultdict(lambda: "three")
for two in ('en', 'sw', 'es', 'af'):
    code_key[two] = "two"

def format_lang(lang, name=None):
    name = name or lang["names"][0]
    code = lang[code_key[lang['two']]]
    return {"name": name, "code": code}

def search(request):
    q = request.GET.get('term') or "English"
    q = q.lower()
    langs = []

    for lang in all_langs:
        if lang['two'].startswith(q) or lang['three'].startswith(q):
            langs.append(format_lang(lang))
        else:
            for name in lang['names']:
                if name.lower().startswith(q):
                    langs.append(format_lang(lang))
                    break
    
    return HttpResponse(json.dumps(langs))