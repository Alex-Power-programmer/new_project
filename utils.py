import json

def open_file_json():
    path = 'candidates.json'
    with open(path,'r',encoding='utf-8') as f:
        file = json.load(f)
    return file
    # candidates = open_file_json()
    # line = '<pre>'
    # for candidate in candidates:
    #     line += f'{candidate['name']} <br>{candidate['position']} <br>{candidate['skills']}<br><br>'
    # line += '</pre>'


def load_candidates_from_json():
    return open_file_json


def get_candidates_id(candidates_id):
    candidates = open_file_json()
    for candidate in candidates:
        if candidate['id'] == candidates_id:
            return candidate


def get_candidates_by_name(candidates_name):
    candidates = open_file_json()
    name = []
    for candidate in candidates:
        if candidate['name'] == candidates_name:
            name.append(candidate)
    return name


def get_candidates_by_skill(skill_name):
    candidates = open_file_json()
    skills = []
    for candidate in candidates:
        if skill_name in candidate['skills']:
            skills.append(candidate)
    return skills

