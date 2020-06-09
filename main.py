import re
import requests


def get_page_with_films(number_page):
    headers = {'cookie': 'navigator_settings=%5B%7B%22rating%22%3A%224%3A%22%7D%2C%22rating%22%5D; mda_exp_enabled=1; _ym_uid=1579529704866061345; mda=0; yandexuid=4775578911579527928; yuidss=4775578911579527928; yandex_login=nick.kurkurin; i=9i3UxfDBmCNL75FEZx4U3m5mvyntQ3SOrXWOe2GcwT9RUFwvONHEehBobaOYt8qcqsCkDxk5AOlFzVem9dcmXnILw7w=; mustsee_sort_v5=01.10.200.21.31.41.121.131.51.61.71.81.91.101.111; lfiltr=all; gdpr=0; __gads=ID=6efe48584a968282:T=1585435663:S=ALNI_MYTKh2uwZR3uJ92wdW6gcL8-agexw; yandex_ugc_modal_dialog=apply; vote_data_cookie=88a70c35167db0a8a6bd50f25936be00; fuid01=5e2c9b512f50800a.XKmg3uxApTtabYZ4CzrUZBvyIO2xRfbMMk522nR7m2BuaU-1z3cKyL1cRG-p_cLskmJIPpgAe5zAsoEi-ZXST4HeSywzVP9WIfMirel3aRia4kHnnlzLJVywKy_C0qBV; PHPSESSID=dk540f4hmu80mg3kc92agkgg91; yandex_gid=142; tc=370; uid=18669245; _csrf_csrf_token=33HPuPKQk48L5tEp4wkHRn8raahH2u039ukReeM22Ow; mobile=no; desktop_session_key=6a2c2ac7756fa9d4fd17f6f21a00f7319b15797226077f8fdf2f9c58db9fad7859fd329375e7967ec99a4b75c63a4858fa3bda88a5e5c43d9653cf126cf9d19bab169e4ef1c1332198ea1595c07d965c32cb3faf072893366bdeef4afac2adc8; desktop_session_key.sig=fR3aoymlc781RG3dpJw0hGN8sDU; _ym_wasSynced=%7B%22time%22%3A1591711356960%2C%22params%22%3A%7B%22eu%22%3A0%7D%2C%22bkParams%22%3A%7B%7D%7D; _ym_isad=2; yp=1584129332.oyu.4775578911579527928#1591797760.yu.4775578911579527928; ymex=1594303360.oyu.4775578911579527928; user-geo-region-id=142; user-geo-country-id=62; user_country=ua; _ym_visorc_22663942=b; _ym_visorc_52332406=b; _ym_visorc_56177992=b; _ym_visorc_26812653=b; ya_sess_id=3:1591722387.5.0.1579529751482:5O7H2Q:2.1|230517873.0.2|30:190171.230791.tJ1qMMOgQcJCYtveYf7HwNx3ZaE; ys=udn.cDpuaWNrLmt1cmt1cmlu#c_chck.2170997977; mda2_beacon=1591722387940; sso_status=sso.passport.yandex.ru:synchronized; _ym_visorc_238735=w; _ym_visorc_237742=w; _ym_visorc_238724=w; yandex_plus_metrika_cookie=true; _ym_visorc_10630330=b; spravka=dD0xNTkxNzIzNDUwO2k9MjE3LjE5OS4yMzkuMTEwO3U9MTU5MTcyMzQ1MDcwNjQwMjQ5NjtoPTVjZWI2ZjQ5YWMzZGRmZDJiN2RmOTAzYWNlNDJiMjdk; my_perpages=%5B%5D; cycada=i+LY98SA4Su4axF/7c/ydPz2/9NbechaydrerABCsV4=; _ym_d=1591723539',
               'referer': 'https://www.kinopoisk.ru/top/',
               'purpose': 'prefetch',
               'sec-fetch-dest': 'empty',
               'sec-fetch-mode': 'no-cors',
               'sec-fetch-site': 'same-origin',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',}
    html_code = requests.get(f'https://www.kinopoisk.ru/top/navigator/m_act[rating]/4%3A/order/rating/page/{number_page}/#results', headers=headers).text
    # print(html_code)
    for url in set(re.findall(r'/level/1/[^\"]*', html_code)):
         read_one_film(url[9:])


def get_title(html_code):
    """
        Функция на получение названия, для сериалов один шаблон для фильмов другой
    :param html_code:
    :return:
    """
    if html_code.find('"@context"') > -1:
        return re.search(r'name":"((?!\",\").)*', html_code).group()[7:]
    else:
        return re.search(r'"title" content="[^»]*', html_code).group()[18:]


def func_for_clear(data):
    return re.sub(r'<[^>]*>|&[^;]*;',  ' ', data)


def get_description(html_code):
    if html_code.find('"@context"') > -1:
        return re.search(r'description":"((?!\",\").)*', html_code).group()[-14:]
    else:
        if description := re.search(r'itemprop="description">((?!<\/div>).)*', html_code):
            return func_for_clear(description.group()[23:])
        else:
            return ''

def read_one_film(film_url):
    headers = {'accept-language': 'ru;q=0.8',
               'cookie': 'mda_exp_enabled=1; _ym_uid=1579529704866061345; mda=0; yandexuid=4775578911579527928; yuidss=4775578911579527928; yandex_login=nick.kurkurin; i=9i3UxfDBmCNL75FEZx4U3m5mvyntQ3SOrXWOe2GcwT9RUFwvONHEehBobaOYt8qcqsCkDxk5AOlFzVem9dcmXnILw7w=; mustsee_sort_v5=01.10.200.21.31.41.121.131.51.61.71.81.91.101.111; lfiltr=all; gdpr=0; __gads=ID=6efe48584a968282:T=1585435663:S=ALNI_MYTKh2uwZR3uJ92wdW6gcL8-agexw; yandex_ugc_modal_dialog=apply; vote_data_cookie=88a70c35167db0a8a6bd50f25936be00; fuid01=5e2c9b512f50800a.XKmg3uxApTtabYZ4CzrUZBvyIO2xRfbMMk522nR7m2BuaU-1z3cKyL1cRG-p_cLskmJIPpgAe5zAsoEi-ZXST4HeSywzVP9WIfMirel3aRia4kHnnlzLJVywKy_C0qBV; PHPSESSID=dk540f4hmu80mg3kc92agkgg91; yandex_gid=142; tc=370; uid=18669245; _csrf_csrf_token=33HPuPKQk48L5tEp4wkHRn8raahH2u039ukReeM22Ow; mobile=no; desktop_session_key=6a2c2ac7756fa9d4fd17f6f21a00f7319b15797226077f8fdf2f9c58db9fad7859fd329375e7967ec99a4b75c63a4858fa3bda88a5e5c43d9653cf126cf9d19bab169e4ef1c1332198ea1595c07d965c32cb3faf072893366bdeef4afac2adc8; desktop_session_key.sig=fR3aoymlc781RG3dpJw0hGN8sDU; _ym_wasSynced=%7B%22time%22%3A1591711356960%2C%22params%22%3A%7B%22eu%22%3A0%7D%2C%22bkParams%22%3A%7B%7D%7D; _ym_isad=2; yp=1584129332.oyu.4775578911579527928#1591797760.yu.4775578911579527928; ymex=1594303360.oyu.4775578911579527928; user-geo-region-id=142; user-geo-country-id=62; user_country=ua; _ym_visorc_22663942=b; _ym_visorc_52332406=b; _ym_visorc_56177992=b; _ym_visorc_26812653=b; ya_sess_id=3:1591722387.5.0.1579529751482:5O7H2Q:2.1|230517873.0.2|30:190171.230791.tJ1qMMOgQcJCYtveYf7HwNx3ZaE; ys=udn.cDpuaWNrLmt1cmt1cmlu#c_chck.2170997977; mda2_beacon=1591722387940; sso_status=sso.passport.yandex.ru:synchronized; _ym_visorc_238735=w; _ym_visorc_237742=w; _ym_visorc_238724=w; spravka=dD0xNTkxNzIzNDUwO2k9MjE3LjE5OS4yMzkuMTEwO3U9MTU5MTcyMzQ1MDcwNjQwMjQ5NjtoPTVjZWI2ZjQ5YWMzZGRmZDJiN2RmOTAzYWNlNDJiMjdk; mykp_button=group; my_perpages=%7B%2248%22%3A200%7D; _ym_visorc_238726=w; yandex_plus_metrika_cookie=true; _ym_d=1591728484; cycada=nCFgZm2DjNP1qOpZfi3Ikvz2/9NbechaydrerABCsV4=',
               "sec-fetch-dest": "document",
               "sec-fetch-mode": "navigate",
               "sec-fetch-site": "same-origin",
               "sec-fetch-user": "?1",
               "upgrade-insecure-requests": "1",
               "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    html_code = requests.get('https://www.kinopoisk.ru/' + film_url, headers=headers).text
    print(html_code)

    info_about_film = []

    info_about_film.append(2 if html_code.find('"https://www.kinopoisk.ru/series') > -1 else 1)     # сериал или нет

    type_ = info_about_film[0]

    info_about_film.append(get_title(html_code))                                                    # название

    info_about_film.append(get_description(html_code))                                              # описание
    print(info_about_film)




def main():
    number_page = 1
    while number_page <= 400:
        get_page_with_films(number_page)


if __name__ == '__main__':
    # main()
    # read_one_film('series/464963/')
    read_one_film('film/435/')
    # read_one_film('film/1003587/')
    # read_one_film('film/1048766/')
