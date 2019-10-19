from flask import Flask
from flask import render_template,redirect, url_for
import os
import json

app = Flask(__name__)

@app.route('/')
def rozetked_page_articles():
    os.system("Lab_1.py")
    with open("articles.json", "r", encoding="utf-8") as read_file1:
        data_set = json.load(read_file1)
    return render_template('index.html', rozetked_page_articles = data_set['articles'], rozet_url = data_set)

@app.route('/update_page', methods=['POST'])
def update_page_():
    return redirect(url_for('rozetked_page_articles'))

@app.route('/reverse', methods=['GET'])
def html_page():
    with open("articles.json", "r", encoding="utf-8") as read_file1:
        data_set1 = json.load(read_file1)
    return render_template('index1.html', rozetked_page_articles1 = data_set1['articles'][::-1], rozet_url1 = data_set1)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)