import random
import re
import time
import requests
import util
from proxy import parse_proxy


def get_page_with_films(number_page):

    headers = {'cookie': f'navigator_settings=%5B%7B%22rating%22%3A%224%3A%22%7D%2C%22rating%22%5D; mda_exp_enabled=1; _ym_uid=1579529704866061345; mda=0; yandexuid=4775578911579527928; yuidss=4775578911579527928; i=9i3UxfDBmCNL75FEZx4U3m5mvyntQ3SOrXWOe2GcwT9RUFwvONHEehBobaOYt8qcqsCkDxk5AOlFzVem9dcmXnILw7w=; mustsee_sort_v5=01.10.200.21.31.41.121.131.51.61.71.81.91.101.111; lfiltr=all; gdpr=0; __gads=ID=6efe48584a968282:T=1585435663:S=ALNI_MYTKh2uwZR3uJ92wdW6gcL8-agexw; yandex_ugc_modal_dialog=apply; vote_data_cookie=88a70c35167db0a8a6bd50f25936be00; fuid01=5e2c9b512f50800a.XKmg3uxApTtabYZ4CzrUZBvyIO2xRfbMMk522nR7m2BuaU-1z3cKyL1cRG-p_cLskmJIPpgAe5zAsoEi-ZXST4HeSywzVP9WIfMirel3aRia4kHnnlzLJVywKy_C0qBV; mobile=no; mykp_button=group; my_perpages=%7B%2248%22%3A200%7D; _ym_wasSynced=%7B%22time%22%3A1591905320985%2C%22params%22%3A%7B%22eu%22%3A0%7D%2C%22bkParams%22%3A%7B%7D%7D; _ym_isad=2; yp=1584129332.oyu.4775578911579527928#1591991722.yu.4775578911579527928; ymex=1594497322.oyu.4775578911579527928; tc=370; spravka=dD0xNTkxOTA4MzkyO2k9MjE3LjE5OS4yMzguMTk5O3U9MTU5MTkwODM5MjQ5NTkzNzI3NTtoPTQ1OTY3ZjYyMzg4YmY0MDk3YTAzMDliZjY1NDk0NTA2; PHPSESSID=9ijqbp2d7f3mfa6saopthsdvk6; yandex_gid=142; _csrf_csrf_token=4TlC5nvmcQAyEZxY-ayQKo-xHUqPHQhZyZgfyGpWCow; desktop_session_key=ff6e098ea50e30c4ee1795fa019ade903a7e285b63c24495038be9d595f56babcb9d1254050ca7b7ff8af4cc28968763ec513157e274a0feeb2bb38758ca1ce4bbbbc7ef0ad8a2b9ccc34001bd3034a8f8882a8f7b4e265b36a7492fec374729; desktop_session_key.sig=drQ-k9x7DIdaxmdpPIn3cCT2iZw; user_country=ua; yandex_plus_metrika_cookie=true; _ym_visorc_22663942=b; _ym_visorc_52332406=b; _ym_visorc_56177992=b; _ym_visorc_26812653=b; ya_sess_id=noauth:1591961725; ys=c_chck.1202477847; mda2_beacon=1591961725740; sso_status=sso.passport.yandex.ru:synchronized; _ym_d=1591961828; cycada=Cts9rtXUNv1AiUXWU3VLdfz2/9NbechaydrerABCsV4=',
               'referer': f'https://www.kinopoisk.ru/top/navigator/m_act[rating]/4:/order/rating/page/{number_page - 1}/',
               'sec-fetch-dest': 'document',
               'sec-fetch-mode': 'navigate',
               'sec-fetch-site': 'cross-site',
               'sec-fetch-user': '?1',
               'upgrade-insecure-requests': '1',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',}
    html_code = requests.get(f'https://www.kinopoisk.ru/top/navigator/m_act[rating]/4%3A/order/rating/page/{number_page}/', headers=headers).text
    if html_code.find('captc') == -1:
        print('ok')
        with open('test.txt', 'a', encoding='utf-8') as f:
            f.write(html_code)
    else:
        print('пиздец')
    # return

    # with open('test.txt', 'r', encoding='utf-8') as f:
    #     html_code = f.read()
    counter = 0
    for code in re.finditer(r'<div id="tr_((?!filmName).)*', html_code, flags=re.DOTALL):
        # print(url)
        code = code.group()
        url = 'series/' if code.find('сериал') > -1 else '/film/'
        counter += 1
        if counter == 6:
            quit()
        print(url + re.search(r'tr_[^\"]*', code).group()[3:], counter)
        # if re.search(r'tr_[^\"]*', code).group()[3:] in ('280166', ):
        #     continue
        if util.check_film(re.search(r'tr_[^\"]*', code).group()[3:]) == 0:
            read_one_film(url + re.search(r'tr_[^\"]*', code).group()[3:] + '/')
            # time.sleep(1)
        # time.sleep(1)


def fixes():
    headers = {'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
               'cookie': 'mda_exp_enabled=1; _ym_uid=1579529704866061345; mda=0; yandexuid=4775578911579527928; yuidss=4775578911579527928; i=9i3UxfDBmCNL75FEZx4U3m5mvyntQ3SOrXWOe2GcwT9RUFwvONHEehBobaOYt8qcqsCkDxk5AOlFzVem9dcmXnILw7w=; mustsee_sort_v5=01.10.200.21.31.41.121.131.51.61.71.81.91.101.111; lfiltr=all; gdpr=0; __gads=ID=6efe48584a968282:T=1585435663:S=ALNI_MYTKh2uwZR3uJ92wdW6gcL8-agexw; yandex_ugc_modal_dialog=apply; vote_data_cookie=88a70c35167db0a8a6bd50f25936be00; fuid01=5e2c9b512f50800a.XKmg3uxApTtabYZ4CzrUZBvyIO2xRfbMMk522nR7m2BuaU-1z3cKyL1cRG-p_cLskmJIPpgAe5zAsoEi-ZXST4HeSywzVP9WIfMirel3aRia4kHnnlzLJVywKy_C0qBV; mobile=no; mykp_button=group; my_perpages=%7B%2248%22%3A200%7D; _ym_wasSynced=%7B%22time%22%3A1591905320985%2C%22params%22%3A%7B%22eu%22%3A0%7D%2C%22bkParams%22%3A%7B%7D%7D; _ym_isad=2; yp=1584129332.oyu.4775578911579527928#1591991722.yu.4775578911579527928; ymex=1594497322.oyu.4775578911579527928; tc=370; spravka=dD0xNTkxOTA4MzkyO2k9MjE3LjE5OS4yMzguMTk5O3U9MTU5MTkwODM5MjQ5NTkzNzI3NTtoPTQ1OTY3ZjYyMzg4YmY0MDk3YTAzMDliZjY1NDk0NTA2; user_country=ua; _ym_visorc_22663942=b; _ym_visorc_52332406=b; _ym_visorc_56177992=b; _ym_visorc_26812653=b; yandex_plus_metrika_cookie=true; _ym_visorc_237742=w; ya_sess_id=noauth:1591938160; mda2_beacon=1591938160511; sso_status=sso.passport.yandex.ru:synchronized; _ym_visorc_238726=w; PHPSESSID=9ijqbp2d7f3mfa6saopthsdvk6; yandex_gid=142; _csrf_csrf_token=4TlC5nvmcQAyEZxY-ayQKo-xHUqPHQhZyZgfyGpWCow; desktop_session_key=ff6e098ea50e30c4ee1795fa019ade903a7e285b63c24495038be9d595f56babcb9d1254050ca7b7ff8af4cc28968763ec513157e274a0feeb2bb38758ca1ce4bbbbc7ef0ad8a2b9ccc34001bd3034a8f8882a8f7b4e265b36a7492fec374729; desktop_session_key.sig=drQ-k9x7DIdaxmdpPIn3cCT2iZw; _ym_d=1591938830; cycada=iTORxNMLe5zAgFZtto7KpPz2/9NbechaydrerABCsV4=',
               'referer': 'https://www.google.com/',
               "sec-fetch-dest": "document",
               "sec-fetch-mode": "navigate",
               "sec-fetch-site": "same-origin",
               "sec-fetch-user": "?1",
               "upgrade-insecure-requests": "1",
               "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    for film_url in util.get_large_year():
        print('Начинаю загружать - ', 'https://www.kinopoisk.ru/' + film_url)
        html_code = requests.get('https://www.kinopoisk.ru/' + film_url, headers=headers).text
        print(get_year(html_code))
        util.update_years(film_url.split('/')[-1], get_year(html_code))
        # input()
        print('Закончил загружать - ', 'https://www.kinopoisk.ru/' + film_url)


def get_title(html_code):
    if html_code.find('"@context"') > -1:
        return re.search(r'name":"((?!\",\").)*', html_code).group()[7:]
    else:
        try:
            return re.search(r'"title" content="[^»]*', html_code).group()[18:]
        except AttributeError:
            print('Слетел IP')


def func_for_clear(data):
    """
        Функция для очистки строки от спец. символов и тегов.
    :param data:
    :return: чистая строка
    """
    return re.sub(r'<[^>]*>|&[^;]*;',  ' ', data)


def get_description(html_code):
    if html_code.find('"@context"') > -1:
        if description := re.search(r'description":"((?!\",\").)*', html_code):
            return re.search(r'description":"((?!\",\").)*', html_code).group()[14:]
    else:
        if description := re.search(r'itemprop="description">((?!<\/div>).)*', html_code):      # иногда описания может и не быть
            return func_for_clear(description.group()[23:])
    return ''


def get_genres(html_code):
    if html_code.find('"@context"') > -1:
        return eval(re.search(r'genre":[^]]*', html_code).group()[7:] + ']')
    else:
        html_code = html_code[html_code.find('itemprop="genre">') + 17:]
        html_code = html_code[:html_code.find('</span>')]
        list_of_genres = []
        for genre in re.finditer(r'>[^,]((?!<\/a>).)*', html_code):
            list_of_genres.append(genre.group()[1:])
        return list_of_genres


def get_year(html_code):
    if html_code.find('"@context"') > -1:
        return re.search(r'mC3xgnbJn9r8KpG71O4nw _2PpOsV4r_uZ1kfCMVw4YLb[^?]*', html_code).group()[-5:-1]
    else:
        return re.search(r'/lists/navigator/\d{4}', html_code, flags=re.DOTALL).group()[-4:]


def get_rating(html_code):
    if html_code.find('"@context"') > -1:
        return re.search(r'ratingValue":[^,]*', html_code).group()[13:]
    else:
        return re.search(r'rating:[^,]*', html_code).group()[7:]


def get_director(html_code):
    list_of_directors = []
    if html_code.find('"@context"') > -1:
        string = re.search(r'director":[^]]*', html_code).group()[10:] + ']'
        string = string.replace('null', 'None')
        for director in eval(string):
            if director.get('name'):
                list_of_directors.append(director.get('name'))
    else:
        if incorrect_directors := re.search('itemprop="director">((?!<\/tr).)*', html_code):
            incorrect_directors = incorrect_directors.group()[21:]
            for directors in re.findall(r'>[^,.][^<]*<', incorrect_directors):
                list_of_directors.append(directors[1:-1])

    return list_of_directors


def get_slug(html_code):
    if html_code.find('"@context"') > -1:
        if slug := re.search(r'_3ja1RtuInxvxsgjHtSWGjM _1nml1ld3eOhePX5JvGVDW7\">«[^»]*', html_code):
            return slug.group()[50:]
    else:
        if slug := re.search(r'слоган<\/td>((?!\/tr).)*', html_code):
            slug = slug.group()
            if slug.find('>-<') == -1:
                return slug[slug.find('&laquo;') + 7: slug.find('&raquo;')]
    return ''


def get_poster(html_code):
    if html_code.find('"@context"') > -1:
        poster = html_code[html_code.find('film-poster _1Vb4pWX9XKqLB1ARq_tTbD image-partial-component _744Do9HoKgS_juORQz12m _3ImO1wdHPSkNycqGSMjFWL'):]
        return 'https:' + re.search(r'src=\"[^\"]*', poster).group()[5:]
    else:
        return re.search(r'property=\"og:image\" content=\"[^\"]*', html_code).group()[29:]


def read_one_film(film_url):
    print('Начинаю загружать - ', film_url)
    headers = {'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
               'cookie': 'mda_exp_enabled=1; _ym_uid=1579529704866061345; mda=0; yandexuid=4775578911579527928; yuidss=4775578911579527928; i=9i3UxfDBmCNL75FEZx4U3m5mvyntQ3SOrXWOe2GcwT9RUFwvONHEehBobaOYt8qcqsCkDxk5AOlFzVem9dcmXnILw7w=; mustsee_sort_v5=01.10.200.21.31.41.121.131.51.61.71.81.91.101.111; lfiltr=all; gdpr=0; __gads=ID=6efe48584a968282:T=1585435663:S=ALNI_MYTKh2uwZR3uJ92wdW6gcL8-agexw; yandex_ugc_modal_dialog=apply; vote_data_cookie=88a70c35167db0a8a6bd50f25936be00; fuid01=5e2c9b512f50800a.XKmg3uxApTtabYZ4CzrUZBvyIO2xRfbMMk522nR7m2BuaU-1z3cKyL1cRG-p_cLskmJIPpgAe5zAsoEi-ZXST4HeSywzVP9WIfMirel3aRia4kHnnlzLJVywKy_C0qBV; mobile=no; mykp_button=group; my_perpages=%7B%2248%22%3A200%7D; _ym_wasSynced=%7B%22time%22%3A1591905320985%2C%22params%22%3A%7B%22eu%22%3A0%7D%2C%22bkParams%22%3A%7B%7D%7D; _ym_isad=2; yp=1584129332.oyu.4775578911579527928#1591991722.yu.4775578911579527928; ymex=1594497322.oyu.4775578911579527928; tc=370; spravka=dD0xNTkxOTA4MzkyO2k9MjE3LjE5OS4yMzguMTk5O3U9MTU5MTkwODM5MjQ5NTkzNzI3NTtoPTQ1OTY3ZjYyMzg4YmY0MDk3YTAzMDliZjY1NDk0NTA2; user_country=ua; _ym_visorc_22663942=b; _ym_visorc_52332406=b; _ym_visorc_56177992=b; _ym_visorc_26812653=b; yandex_plus_metrika_cookie=true; _ym_visorc_237742=w; ya_sess_id=noauth:1591938160; mda2_beacon=1591938160511; sso_status=sso.passport.yandex.ru:synchronized; _ym_visorc_238726=w; PHPSESSID=9ijqbp2d7f3mfa6saopthsdvk6; yandex_gid=142; _csrf_csrf_token=4TlC5nvmcQAyEZxY-ayQKo-xHUqPHQhZyZgfyGpWCow; desktop_session_key=ff6e098ea50e30c4ee1795fa019ade903a7e285b63c24495038be9d595f56babcb9d1254050ca7b7ff8af4cc28968763ec513157e274a0feeb2bb38758ca1ce4bbbbc7ef0ad8a2b9ccc34001bd3034a8f8882a8f7b4e265b36a7492fec374729; desktop_session_key.sig=drQ-k9x7DIdaxmdpPIn3cCT2iZw; _ym_d=1591938830; cycada=iTORxNMLe5zAgFZtto7KpPz2/9NbechaydrerABCsV4=',
               'referer': 'https://www.google.com/',
               "sec-fetch-dest": "document",
               "sec-fetch-mode": "navigate",
               "sec-fetch-site": "same-origin",
               "sec-fetch-user": "?1",
               "upgrade-insecure-requests": "1",
               "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    # film_url = 'series/1309325/'
    html_code = requests.get('https://www.kinopoisk.ru/' + film_url, headers=headers)
    html_code = html_code.text
    info_about_film = []

    info_about_film.append(get_title(html_code))                                                    # название

    info_about_film.append(get_description(html_code))                                              # описание

    info_about_film.append(get_genres(html_code))                                                   # жанры

    info_about_film.append(get_year(html_code))                                                     # год

    info_about_film.append(get_rating(html_code))                                                   # рейтинг

    info_about_film.append(get_director(html_code))                                                 # режисер

    info_about_film.append(get_slug(html_code))                                                     # слоган

    info_about_film.append(get_poster(html_code))                                                   # постер

    info_about_film.append(2 if html_code.find('"https://www.kinopoisk.ru/series') > -1 else 1)     # сериал или нет

    info_about_film.append(film_url[film_url.find('/') + 1:-1])

    util.insert_new_movie(info_about_film)

    print('Фильм - ', film_url, ' добавлен в БД')


def main():
    number_page = 103
    while number_page <= 103:
        print('Начинаю парсить страницу - ', number_page)
        get_page_with_films(number_page)
        print('Закончил парсить страницу - ', number_page)
        number_page += 1


if __name__ == '__main__':
    # pass
    # main()
    fixes()
    # get_page_with_films(1)
    # read_one_film('series/464963/')
    # read_one_film('series/77044/')
    # read_one_film('film/435/')
    # read_one_film('film/1003587/')
    # read_one_film('film/1048766/')
    # read_one_film('film/81542/')
    # read_one_film('film/1043713/')
    # read_one_film('/level/1/film/279548')