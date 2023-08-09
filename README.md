# movierec
# Movie_Recommendation_System
This is a  content-based recommender system that recommends movies similar to the movie the user likes and analyses the reviews given by the user.In this project, machine learning methods will be used to create a Movie Recommendation System. From a user’s perspective, they are catered to fulfill the user’s needs in the shortest time possible.From an organization’s perspective, they want to keep the user as long as possible on the platform so that it will generate the most possible profit for them. With better recommendations, it creates positive feedback from the user as well. 


## Requirements
- [ ] Python 3.6 or higher IDLE
- [ ] Anaconda -Jupyter
- [ ] Anaconda -Spyder

## Modules Used
- [ ] Numpy
- [ ] Pandas
- [ ] Sklearn



## Dataset
Movie recommendation systems use a set of different filtration strategies and algorithms to help users find the most relevant films. The most popular categories of the ML algorithms used for movie recommendations include content-based filtering and collaborative filtering systems.
Finding proper movie datasets is crucial to mastering the basic ML methods, and give your movie recommendation project a try. 
The right movie datasets that are most valuable for machine learning projects should contain information on the keywords,original_language,original_title,popularity,release_date,tagline,title,cast,crew,Director etc... Such datasets might be hard to find, so we’ve prepared a list of the most popular movie datasets for machine learning for users convenience.


## Model
The model used for the movie recommendation system  is a content-based filtering model. It utilizes the cosine similarity function to calculate the similarity between the features of the movies and recommends movies with the highest similarity scores to the user. The features used in the model include movie titles, genres, and descriptions which are transformed into feature vectors using the TF-IDF vectorizer.

## Overview
The movies are recommended based on the content of the movie you entered or selected. The main parameters that are considered for the recommendations are the genre, director, and top 3 casts. The details of the movies, such as title, genre, runtime, rating, poster, casts, etc., are fetched from TMDB. The reviews of each individual movie given by the users are "web-scraped" from the IMDB website with the help of beautifulsoup4, and the reviews are subjected to sentiment analysis, where the model predicts whether the review is positive or negative.


## Contribution
Contributions are welcome! If you want to contribute to the project, please create a pull request with a detailed explanation of the changes.
