from flask import Flask, jsonify, request, render_template
import requests
import os

app = Flask(__name__)

BOOKS_API_URL = os.getenv("BOOKS_API_URL", "http://localhost:5001/books")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/search', methods=['GET'])
def search_books():
    genre = request.args.get('genre')
    if not genre:
        return render_template("index.html", error="Please enter a genre.")
    
    try:
        response = requests.get(f"{BOOKS_API_URL}?genre={genre}")
        response.raise_for_status()
        books = response.json()
        return render_template("index.html", books=books, genre=genre)
    except requests.exceptions.RequestException as e:
        return render_template("index.html", error="Failed to fetch data from API")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)