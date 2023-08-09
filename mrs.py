# -*- coding: utf-8 -*-

# Importing required libraries
import numpy as np
import pandas as pd
import difflib  # Library for fuzzy string matching
from sklearn.feature_extraction.text import TfidfVectorizer  # Library for creating feature vectors
from sklearn.metrics.pairwise import cosine_similarity  # Library for calculating similarity scores

# Loading the movies dataset
movies_data = pd.read_csv("C:/Users/Siva Shankar/Desktop/Sample/movies.csv")

# Saving a copy of the dataset to a CSV file
movies_data.to_csv("D:\ss.csv") 

# Printing the description of the dataset
print("\n\n Description Of the DataSet :\n", movies_data.describe())

# Printing the dimensions of the dataset
print("\n\nDimenstion Of the DataSet :", movies_data.shape)

# Printing the first 5 rows of the dataset
print("\n\n First 5 rows  in the SataSet :\n", movies_data.head())

# Printing the count of null values in the dataset
print("\n\n Count Of Null Values in the DataSet :\n", movies_data.isnull().sum())

# Filling any missing values in the dataset
movies_data = movies_data.fillna('')

# Selecting the features to be used for recommendations
selected_features = ['genres','keywords','tagline','cast','director']

# Printing the selected features
print("\n\n Selected Features in the dataset :  ",selected_features)

# Filling any missing values for the selected features
for feature in selected_features:
  movies_data[feature] = movies_data[feature].fillna('')

# Combining the selected features into a single column
combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']

# Printing the combined features
print("\n\n The combined features after merging the features :\n", combined_features)

# Creating feature vectors from the combined features
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# Printing the feature vectors
print("\n\n After converting the data into textual data :\n",feature_vectors)

# Calculating the cosine similarity between the feature vectors
similarity = cosine_similarity(feature_vectors)

# Printing the similarity scores
print("\n\n Printing the Similar :\n",similarity)

# Printing the shape of the similarity scores
print("\n\n Printing the shape : ",similarity.shape)

# Taking user input for their favourite movie
movie_name = input(' Enter your favourite movie name : ')

# Creating a list of all movie titles in the dataset
list_of_all_titles = movies_data['title'].tolist()

# Printing the list of all movie titles in the dataset
print("\n\ncPrinting a list with all the movie names given in the dataset :\n",list_of_all_titles)

# Finding the closest matches to the user's input
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

# Printing the closest movie names to the user's input
print("\n\nPrinting the Closest Movie names to the given Movie : \n",find_close_match)

# Selecting the closest match
close_match = find_close_match[0]

# Get the index of the selected movie in the dataset
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
print(index_of_the_movie)

# Get the similarity scores for the selected movie and enumerate them
similarity_score = list(enumerate(similarity[index_of_the_movie]))
print(similarity_score)

# Get the length of the similarity score list
len(similarity_score)

# Sort the similarity score list in descending order
sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
print(sorted_similar_movies)

# Print suggested movies
print('Movies suggested for you: \n')

i = 1
for movie in sorted_similar_movies:
    index = movie[0]
    title_from_index = movies_data[movies_data.index == index]['title'].values[0]
    if i < 30:
        print(i, '.', title_from_index)
        i += 1

# Get user input for their favorite movie
movie_name = input('Enter your favourite movie name: ')

# Get a list of all movie titles
list_of_all_titles = movies_data['title'].tolist()

# Find the closest match to the user's input in the list of movie titles
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

# Get the closest match
close_match = find_close_match[0]

# Get the index of the closest match
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

# Get the similarity scores for the closest match and enumerate them
similarity_score = list(enumerate(similarity[index_of_the_movie]))

# Sort the similarity score list in descending order
sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

# Print suggested movies
print('Movies suggested for you: \n')

i = 1
for movie in sorted_similar_movies:
    index = movie[0]
    title_from_index = movies_data[movies_data.index == index]['title'].values[0]
    if i < 30:
        print(i, '.', title_from_index)
        i += 1

