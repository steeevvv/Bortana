# Bortana
Movies & TV Shows Chatbot Assistant created as a Task in Valoro Chabtot course - Summer 2021

<!-- ABOUT THE PROJECT -->
## About The Project
Chatbot Built in Python, integrated with PHPMYADMIN DB, React, Rivescript, and Flask. it depends on TMDB API which give responses that the bot will reply to the user by.

Credits to [this](https://github.com/valoro/bot_front?fbclid=IwAR2JfYS-Hn66RGL5GJYoJ-ZSx0NOpbBzfKYT3k0SLXRBt6_eR1dENCf7Irk) repository for the frontend of the chatbot, and [this](https://github.com/NadaTarek1/Covid19-Medical-Chatbot) repository for the base Python/Flask project that I built on.

YES, It can assist you finding your next favorite movie or tv show! 

## What Can it do?
* Show Top Rated Movies
* Show Most Popular Movies
* Show Top Rated Series/TV Shows
* Show Most Popular Series/TV Shows
* Get Recommendations of movies based on certain movie
* Get Movies that certain Actor acted in :smile:

## Installation and usage
This installation guide assume you have the latest version of python.

### 1. Install flask


```bash
pip install Flask
```

### 2. Start MySQL server

On your local machine, make sure to start MySQL server and have an IDE for managing the server, like XAMPP.

### 3. Import MySQL database

A Database with two columns is required to be created on your localhost DB. First Schema called 'movies' that has a table called 'users' that has two colums, name and password.

### 4. Edit the base code if needed

You might need to change the APIKEY in `utils.py` to create one, head ovet TMDB API, and create a new API KEY.

### 5. Run flask
In the main directory of the project, where the `main.py` file is, run the following commands:

```bash
python main.py
```
Flask should now be up and running, and you can send requests to the chatbot

### 6. Run the frontend
to run the frontend, split terminal, then navigate to the directory `frontend` and type the following commands:
```bash
npm install
npm start
```
You will see a message telling you the localhost address you can visit to run the frontend
```bash
** Angular Live Development Server is listening on localhost:4200, open your browser on http://localhost:4200/ **
```

## 7. Start Conversation 
To start conversation head over to localhost:4200 in any browser and enjoy the chatbot
