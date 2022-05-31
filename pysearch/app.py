from bing_image_urls import bing_image_urls
from flask import Flask, request, render_template
import random 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        result = request.form
        url = bing_image_urls(result["KW"], limit=1)[0]
    else:
        url = ''
    return render_template('./index.html', embed=url)

app.run(debug=True)