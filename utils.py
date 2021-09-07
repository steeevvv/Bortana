import mysql.connector as mysql
import requests

api_url_base = 'https://api.themoviedb.org/3/movie/'
key = '9a30d12144d08ecb0aff498b294d7cb7'

mydb = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="movies"
)

def doesUserExist(user):
    cur = mydb.cursor(dictionary=True)
    qry = "SELECT * FROM `user` WHERE `name`= '{}'".format(user)
    cur.execute(qry)
    result = cur.fetchone()
    return False if result is None else True

def registerUser(user, password):
    cur = mydb.cursor()
    sql = "INSERT INTO user (name, password) VALUES (%s, %s)"
    val = (user, password)
    cur.execute(sql, val)
    mydb.commit()
    #print(cur.rowcount, "record inserted.")
    return True

def authenticateUser(user, password):
    cur = mydb.cursor(dictionary=True)
    qry = "SELECT * FROM `user` WHERE `name`= '{}' AND `password`= {}".format(user, password)
    cur.execute(qry)
    user = cur.fetchone()
    #print(user)
    return False if user is None else True

def TopRatedMovies():
    api_url = api_url_base + 'top_rated?api_key=' + key + '&language=en-US&page=1'
    response = requests.get(api_url)
    if response.status_code == 200:
        movies = list()
        for item in response.json()['results']:
            movies.append(item['title'])
        #print (movies)
        return movies
    return None

def MostPopularMovies():
    api_url = api_url_base + 'popular?api_key=' + key + '&language=en-US&page=1'
    response = requests.get(api_url)
    if response.status_code == 200:
        movies = list()
        for item in response.json()['results']:
            movies.append(item['title'])
        #print (movies)
        return movies
    return None

def TopRatedShows():
    api_url = 'https://api.themoviedb.org/3/tv/top_rated?api_key=' + key + '&language=en-US&page=1'
    response = requests.get(api_url)
    if response.status_code == 200:
        movies = list()
        for item in response.json()['results']:
            movies.append(item['name'])
        #print (movies)
        return movies
    return None

def MostPopularShows():
    api_url = 'https://api.themoviedb.org/3/tv/popular?api_key=' + key + '&language=en-US&page=1'
    response = requests.get(api_url)
    if response.status_code == 200:
        movies = list()
        for item in response.json()['results']:
            movies.append(item['name'])
            movies.append(item['first_air_date'])
        #print (movies)
        return movies
    return None


def SimilarMovies(movie):
    new_string = movie.replace(" ", "+")
    api_url1 = 'https://api.themoviedb.org/3/search/movie?api_key=' + key + '&query=' + new_string
    response1 = requests.get(api_url1)
    if response1.status_code == 200:
        movies1 = list()
        for item in response1.json()['results']:
            movies1.append(item['id'])
    
    movie_id = movies1[0]
    api_url = api_url_base + str(movie_id) + '/recommendations?api_key=9a30d12144d08ecb0aff498b294d7cb7&language=en-US&page=1'
    response = requests.get(api_url)
    if response.status_code == 200:
        movies = list()
        for item in response.json()['results']:
            movies.append(item['title'])
        #print (movies)
        return movies
    return None