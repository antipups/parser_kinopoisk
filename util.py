import pymysql


connect = pymysql.Connect(host='localhost', user='root', password='', db='kinopoisk')
cursor = connect.cursor()


def check_film(kino_id):
    cursor.execute(f'SELECT * FROM movies WHERE kinopoisk_id = {str(kino_id)}')
    return len(cursor.fetchall())


def insert_categories(categories, id_of_movies):
    """
        Добавление категорий в БД, тех которых не хватает, и сразу связывание их с фильмом.
    :param categories:      категории
    :param id_of_movies:    айди добавленного фильма
    :return:
    """
    if len(categories) > 20:
        return
    cursor.execute('INSERT IGNORE INTO categories (title_of_category) VALUES ("' + '"), ("'.join(categories) + '")')

    connect.commit()

    cursor.execute('SELECT id '
                   'FROM categories '
                   'WHERE title_of_category IN ("' + '", "'.join(categories) + '")')
    ids_of_categories = tuple(str(id_of_movies) + ', ' + str(row[0]) for row in cursor.fetchall())
    cursor.execute('INSERT INTO mov_with_cat (id_of_mov, id_of_cat) VALUES (' + '), ('.join(ids_of_categories) + ')')
    connect.commit()


def insert_year(year):
    cursor.execute(f'INSERT IGNORE INTO years (title_of_year) VALUES ({year})')
    connect.commit()

    cursor.execute('SELECT id '
                   'FROM years '
                   f'WHERE title_of_year = {year}')
    return cursor.fetchall()[0][0]


def insert_directors(directors, id_of_movies):
    """
        Добавление категорий в БД, тех которых не хватает, и сразу связывание их с фильмом.
    :param directors:       режисеры
    :param id_of_movies:    айди добавленного фильма
    :return:
    """
    cursor.execute('INSERT IGNORE INTO directors (title_of_director) VALUES ("' + '"), ("'.join(directors) + '")')
    connect.commit()

    cursor.execute('SELECT id '
                   'FROM directors '
                   'WHERE title_of_director IN ("' + '", "'.join(directors) + '")')
    ids_of_directors = tuple(str(id_of_movies) + ', ' + str(row[0]) for row in cursor.fetchall())
    cursor.execute('INSERT INTO mov_with_dir (id_of_mov, id_of_dir) VALUES (' + '), ('.join(ids_of_directors) + ')')
    connect.commit()


def insert_new_movie(data):
    """
        Добавление фильма
    :param data:    инфа о фильма
    :return:
    """
    id_of_year = insert_year(data[3])

    cursor.execute('INSERT INTO movies (movie_name, `description`, id_of_year, rating, slug, poster, movie_or_serial, kinopoisk_id) '
                   'VALUES ( "{}", "{}", {}, "{}", "{}", "{}", "{}", {})'.format(data[0], data[1].replace('"', "'"), str(id_of_year), data[4], data[6], data[7], str(data[8]), data[9][data[9].find('/') + 1:]))
    connect.commit()

    cursor.execute('SELECT MAX(id) FROM movies')
    id_of_movie = cursor.fetchall()[0][0]
    insert_categories(data[2], id_of_movie)
    insert_directors(data[5], id_of_movie)


def get_large_year():
    cursor.execute('SELECT kinopoisk_id FROM `movies` WHERE id_of_year IN (SELECT id FROM years WHERE title_of_year > "2020" OR title_of_year < "1900")')
    return tuple('film/' + str(row[0]) for row in cursor.fetchall())


def update_years(kinopoisk_id, year):
    cursor.execute(f'UPDATE movies SET id_of_year = (SELECT id FROM years WHERE title_of_year = "{year}") WHERE kinopoisk_id = {kinopoisk_id}')
    connect.commit()


if __name__ == '__main__':
    pass
