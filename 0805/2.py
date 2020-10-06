import requests as req
from bs4 import BeautifulSoup
import os

pokemon_url = 'https://pokemon.wingzero.tw'


def guard_folder(dir_name):
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)


def get_img(no, folder_name):
    url = f'{pokemon_url}/pokedex/generation/{no}/en'
    r = req.get(url)
    if r.status_code != 200:
        print(r.status_code)
    content = r.text

    soup = BeautifulSoup(content, 'lxml')
    num = soup.findAll(attrs={'class': 'pm_sn'})

    start, end = int(num[0].text), int(num[-1].text)

    for i in range(start, end+1, 1):
        url = f'{pokemon_url}/pokedex/intro/{i}/en'
        r = req.get(url)
        if r.status_code != 200:
            print(r.status_code)
        content = r.text

        soup = BeautifulSoup(content, 'lxml')
        name, ID = soup.find('h1').text.rsplit(' ', 1)
        name = name.replace(':', '')
        ID = ID.split('\n')[0]
        attrs = soup.find(attrs={'id': 'typeList'}).text.split()

        file_name = f'{ID}_{name}'
        for s in attrs:
            file_name += f'_{s}'
        path_name = os.path.join(
            folder_name, f'Generation_{no}/{file_name}.png')

        img_url = pokemon_url + \
            soup.find(attrs={'id': 'pokeImg'}).get('data-src')
        r_img = req.get(img_url, stream=True)
        if r_img.status_code == 200:
            with open(path_name, 'wb') as f:
                for chunk in r_img:
                    f.write(chunk)


def main(folder_name):
    for no in [1, 5, 7]:
        gen_no = f'Generation_{no}'
        guard_folder(os.path.join(folder_name, gen_no))
        get_img(no, folder_name)


if __name__ == '__main__':
    guard_folder('./img/Pokemons')
    main('./img/Pokemons')
