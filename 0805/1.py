import re
import os
import requests as req
import pandas as pd

def guard_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)

def get_top100_csv(category):
    print(
        f'https://www.rottentomatoes.com/top/bestofrt/top_100_{category}_movies/')
    with req.get(f'https://www.rottentomatoes.com/top/bestofrt/top_100_{category}_movies/') as r:
        if r.status_code != 200:
            print(r.status_code)
            exit(-1)
        content = r.text

    hearder_pattern = r'<table class=\"table\">\s+?<thead>\s+?<tr>\s+?(<.+?>\s+?<.+?>\s.+?<.+?>\s+?<.+)'

    hearder = re.search(hearder_pattern, content).group(1)

    col_pattern = r'<th.*?>(\w.+?)<'
    col_names = re.findall(col_pattern, hearder)

    df = pd.DataFrame(columns=col_names)

    content_patterns = [r'<td class=\"bold\">(\d+)\D', r'<span class=\"tMeterScore\">\S+;(\d+\S)',
                        r'<a.+?class=\"unstyled articleLink\">\s+(\S.+?)</a>', r'<td class=\"right hidden-xs\">(\d+)</td>']

    for c, p in zip(col_names, content_patterns):
        ls = re.findall(p, content)
        df[c] = ls

    df.to_csv(f'./src/top100/terry/{category}.csv', index=False)


def main():

    with req.get('https://www.rottentomatoes.com/top/') as r:
        if r.status_code != 200:
            print(r.status_code)
            exit(-1)
        content = r.text

    pattern = r'<a.+?class=\"articleLink unstyled\"><div>Top 100 (\S.+?) Movies</div>'
    categories = [c.replace('&', '').replace(' ', '_').lower()
                  for c in re.findall(pattern, content)]

    for c in categories:
        print('----------')
        print(c)
        get_top100_csv(c)


if __name__ == "__main__":
    guard_folder('./src/top100')
    guard_folder('./src/top100/terry')
    main()
