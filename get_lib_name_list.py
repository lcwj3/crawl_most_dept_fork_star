import requests
import json
LIBRARIES_IO_API_KEY = '59d8b38b16dda6e3a14018293f69e22e'
SORT_KEYS = {'most_dep': 'dependents_count', 'most_star': 'stars', 'most_fork': 'forks'}
wanted_language = ['rubygems', 'packagist']
wanted_number = 2000
def get_lib_list(size, language, type):
    ret = []
    for i in range(int(size / 100) + 1):
        try:
            batch_res = requests.get(
                f'https://libraries.io/api/search?sort={SORT_KEYS[type]}&api_key=59d8b38b16dda6e3a14018293f69e22e&platform={language}&page={str(i)}&per_page=100')
            batch_res.raise_for_status()
        except Exception as e:
            print(e)
        libs = json.loads(batch_res.content.decode())
        print(i, type)
        ret += list({x['name']: list(y['number'] for y in x['versions'])} for x in libs)
    return ret

def get_lib_lists(size, language, most_dep=False, most_star=False, most_fork=False):
    res = {}
    if most_dep:
        res['most_dep'] = get_lib_list(size, language, 'most_dep')
        with open('most_dep_' + str(size) + '_' + language + '.json', 'w') as f:
            json.dump(res['most_dep'], f)
    if most_star:
        res['most_star'] = get_lib_list(size, language, 'most_star')
        with open('most_star_' + str(size) + '_' + language + '.json', 'w') as f:
            json.dump(res['most_star'], f)
    if most_fork:
        res['most_fork'] = get_lib_list(size, language, 'most_fork')
        with open('most_fork_' + str(size) + '_' + language + '.json', 'w') as f:
            json.dump(res['most_fork'], f)
    return res

def get_most_downloaded_lib():
    # please check most_download.json, this contains top 1000 downloaded libs (until September 2019),
    # if you want latest download data, please use given url in readme.md to request again.
    pass


for lang in wanted_language:
    x = get_lib_lists(wanted_number, lang, most_dep=True, most_star=True, most_fork=True)
    # with open('most_dep_' + str(wanted_number) + '_' + lang + '.json', 'w') as f:
    #     json.dump(x['most_dep'], f)
    # with open('most_star_' + str(wanted_number) + '_' + lang + '.json', 'w') as f:
    #     json.dump(x['most_star'], f)
    # with open('most_fork_' + str(wanted_number) + '_' + lang + '.json', 'w') as f:
    #     json.dump(x['most_fork'], f)


