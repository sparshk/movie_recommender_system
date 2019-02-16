# Movie Finder

Movie Finder is a movie recommendation system that recommends movies to users using three algorithms - User-User Collaborative Filtering, Item-Item Collaborative Filtering and Matrix Factorization.

## Codebase

It has two main components:

1) A web scraper(imdbscraper)
2) A web app that recommends movies(movie_rs)

    ### Web scraper(via Scrapy):

        1. To scrape movies from IMDB, the links.csv dataset was extracted
           from http://files.grouplens.org/datasets/movielens/ml-latest- 
           small.zip and then edited to have the first 300 links only.
        
        2. Each link was then scraped individually to gather 
           information such as title,genre,year,imdb_url,img_url,
           users_rating and description and saved as a movies.csv file.
    ### Web-app(via Django):
         
        1. To first feed the movies.csv into the movies model, a python
           script was executed in the python shell.
                 (InteractiveConsole)
                  >>> import csv
                  >>> import os
                  >>> from movie.models import movies
                  >>> with open('movies.csv') as csvfile:
                  ...     reader=csv.DictReader(csvfile)
                  ...     for row in reader:
                  ...             p=movies(title=row['title'], 
                                           genre=row['genre'],
                                           description= row['description'],
                                           imdb_url=row['imdb_url'],
                                           img_url=row['img_url'],
                                       users_rating=row['users_rating'],
                                        year=row['year'])

                  ...              p.save()
                  >>> exit()
         2. Dummy users added to reduce the cold-start error 
            in collaborative filtering algorithms.
         3. After pushing the data into the database, the user logs in 
            and rates 15 movies and then is recommended 15 movies via 
            each of the three recommender algorithms.

       
## Directory Structure

```
  .
  |-imdbscraper
    |-imdbscraper
      |...
        |-spiders
          |-imdb.py
        |-items.py
        |-pipelines.py
        |-settings.py
        |...
  |-movie_rs
    |-movie
      |-migrations
      |-static
      |-templates
        |...
      |-apps.py
      |-forms.py
      |-models.py
      |-movies.csv
      |-urls.py
      |-views.py
    |-movie_rs
      |-item_item.py
      |-manage.py
      |-matrix_factorization.py
      |-movies.csv
      |-user_user.py
    |-requirements.txt
    |-README.md


  
```

## Usage

```link
  The web application has been deployed here : https://moviesrsfinder.herokuapp.com/
  However, if you are facing issues getting recommendations, you can log in through any of the dummy users for testing           purposes. The dummy accout credentials are:
        username : sparshx (x can be any value from 1 to 15, also maintain case)
        password : 1234
  Don't rate any movies from dummy accounts.
  
  Or else, you can clone the project locally and follow these steps:
  1) change directory to the cloned file and create a virtual environment using "virtualenv env"
  2) pip install -r requirements.txt
  3) cd movie_rs
  3) python manage.py runserver
  4) Type localhost:8000 in your browser and you can now login, rate and get recommended.
```
## Dependencies
```
pandas==0.22.0
requests==2.18.4
Django==2.0.6
Scrapy==1.5.1
scipy==1.0.0
numpy==1.14.0
pymongo==3.7.2
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
