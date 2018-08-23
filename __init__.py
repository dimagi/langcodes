from __future__ import absolute_import
from __future__ import unicode_literals
import json, os
import six
from io import open
from django.core.cache import cache

try:
    langs
except:
    with open(os.path.join(os.path.dirname(__file__), 'langs.json'), encoding='utf-8') as f:
        langs = json.load(f)

grandfathered = ('en', 'sw', 'es', 'af')

langs_by_code = {}
for lang in langs:
    if lang['two'] in grandfathered:
        langs_by_code[lang['two']] = lang
    else:
        langs_by_code[lang['three']] = lang


def get_name(lang):
    lang_info = langs_by_code.get(lang)
    if lang_info:
        return lang_info['names'][0]
    else:
        return None


def get_all_langs_for_select():
    langs_for_select = cache.get('__all_langs_for_select')
    if not langs_for_select:
        langs_for_select = []
        for key, val in six.iteritems(langs_by_code):
            label = key + " (" + val['names'][0] + ")"
            langs_for_select.append((key, label))
        cache.set('__all_langs_for_select', langs_for_select, 12 * 60 * 60)
    return langs_for_select

