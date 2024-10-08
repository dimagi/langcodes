from collections import defaultdict

from django.http import JsonResponse

from langcodes import grandfathered
from langcodes import langs as all_langs

code_key = defaultdict(lambda: "three")
for two in grandfathered:
    code_key[two] = "two"

def format_lang(lang, name=None, suffix=None):
    name = name or lang["names"][0]
    code = lang[code_key[lang['two']]] + ('-' + suffix if suffix else "")
    return {"name": name, "code": code}

def split_query(q):
    if '-' in q:
        q = q.split('-')
        q, suffix = '-'.join(q[:-1]), q[-1]
    else:
        suffix = None
    return q, suffix

def search(request):
    q = request.GET.get('term')
    langs = []
    if q:
        q = q.lower()
        q, suffix = split_query(q)

        for lang in all_langs:
            lang_code_and_name = lang['names'] + [lang['two'], lang['three']]
            if any([code_and_name.lower().startswith(q)
                    for code_and_name in lang_code_and_name]):
                langs.append(format_lang(lang, suffix=suffix))
    else:
        for lang in all_langs:
            langs.append(format_lang(lang))
    
    return JsonResponse(langs, safe=False)

def validate(request):
    q = request.GET.get('term') or ''
    key = None
    match = None
    suggestions = []
    q, suffix = split_query(q)
    
    if len(q) == 2:
        key = 'two'
    elif len(q) == 3:
        key = 'three'

    if key:
        q_lower = q.lower()
        match = [lang for lang in all_langs if lang[key] == q_lower]
        match = format_lang(match[0]) if match else None
        if match and match['code'] != q:
            suggestions.append(match)
            match = None
            
    if not match:
        q_lower = q.lower()
        sugs = [
            lang for lang in all_langs
            if lang["three"].startswith(q_lower) or [
                name for name in lang['names'] if name.lower().startswith(q_lower)
            ]
        ]
        suggestions.extend([format_lang(lang) for lang in sugs])

    def filter_suggestions(old_suggestions):
        sug_codes = set()
        suggestions = []
        for sug in old_suggestions:
            if sug['code'] not in sug_codes:
                suggestions.append(sug)
                sug_codes.add(sug['code'])
        return suggestions
    suggestions = filter_suggestions(suggestions)
    return JsonResponse({
        "match":  match,
        "suggestions": suggestions,
    })
