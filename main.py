from utils import open_file_json, load_candidates_from_json, get_candidates_by_name, get_candidates_by_skill, get_candidates_id
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def go():
    return render_template("list.html")
@app.route('/candidate/<x>')
def hello(x):
    candidates_name = get_candidates_by_name(x)
    return render_template('list.html',candidate=candidates_name)

#<p><a href="candidates/<x>" </a></p>

app.run(debug=True)