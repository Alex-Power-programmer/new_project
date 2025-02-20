from utils import load_candidates_from_json, get_candidates_by_name, get_candidates_by_skill, get_candidate
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def go():
    return render_template("list.html", candidates=load_candidates_from_json())


@app.route('/candidate/<x>')
def id_candidates(x):
    return render_template("single.html",i=get_candidate(int(x)))


@app.route('/skill/<skill_name>')
def skill(skill_name):
    list_skills = get_candidates_by_skill(skill_name)
    skill = skill_name.title()
    digit = len(list_skills)
    return render_template("skills.html",list_skills= list_skills,skill=skill, digit=digit)


@app.route('/search/<candidate_name>')
def search(candidate_name):
    candidates_names = get_candidates_by_name(candidate_name)
    digit = len(candidates_names)
    return render_template('search.html', candidates_names=candidates_names, digit=digit)


@app.route('/search/candidate/<x>')
def search_candidate(x):
    return render_template('single.html',i=get_candidate(int(x)) )