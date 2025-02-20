import json

def load_candidates_from_json():
    path = 'candidates.json'
    with open(path,'r',encoding='utf-8') as f:
        file = json.load(f)
    return file


candidates = load_candidates_from_json()


def get_candidate(candidates_id):
    for candidate in candidates:
        if candidate['id'] == candidates_id:
            return candidate
    return {'not_found': "Кандидат не найден"}

def get_candidates_by_name(candidates_name):
    name_list = []
    for candidate in candidates:
        if  candidates_name.title() in candidate['name']:
            name_list.append(candidate)
    return name_list


def get_candidates_by_skill(skill_name):
    list_skills = []
    for candidate in candidates:
        if skill_name.lower() in candidate['skills'].lower().split():
            list_skills.append(candidate)
    return list_skills