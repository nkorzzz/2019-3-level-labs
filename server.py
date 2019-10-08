from flask import Flask
from flask import render_template
import os
import json
os.system("Lab_1.py")
app = Flask(__name__)

@app.route('/')
def rozetked_page_articles():
    with open("articles.json", "r", encoding="utf-8") as read_file1:
        data_set = json.load(read_file1)
    return render_template('index.html', rozetked_page_articles = data_set['articles'], rozet_url = data_set)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)