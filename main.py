import requests
import pymysql


connect = pymysql.Connect(host='localhost', user='root', password='', db='kinopoisk')
connect.cursor()