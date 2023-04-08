from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

with open("wine_recommender.pkl", "rb") as f:
    titles, similarity_matrix = pickle.load(f)
    
def recommend_wines_by_title(wine_title, n_recommendations=10):
    # Find the index of the wine with the given title
    wine_index = titles[titles == wine_title].index[0]
    
    # Get similarity scores for the given wine
    similarity_scores = list(enumerate(similarity_matrix[wine_index]))
    
    # Sort the wines based on the similarity scores
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    
    # Get the indices of the most similar wines (excluding the input wine itself)
    most_similar_indices = [score[0] for score in similarity_scores[1:n_recommendations+1]]
    
    # Return the titles of the most similar wines
    return titles.iloc[most_similar_indices]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        wine_title = request.form["wine_title"]
        recommendations = recommend_wines_by_title(wine_title)
        return render_template("index.html", wine_title=wine_title, recommendations=recommendations)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

