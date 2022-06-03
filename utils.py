import json


CANDIDATES_FILE = 'candidates.json'


def _load_json_file(filename):
    with open(filename) as file:
        return json.load(file)


def load_candidates():
    return _load_json_file(CANDIDATES_FILE)


def get_candidate_by_name(candidates, name):
    for candidat in candidates:
        if candidat['name'].lower() == name.lower():
            return candidat
    return None


def get_candidates_by_skill(candidates, skill):
    candidates_with_skill = []
    for candidat in candidates:
        skills = [skill.lower().strip() for skill in candidat['skills'].split(',')]
        print(skills)
        if skill.lower() in skills:
            candidates_with_skill.append(candidat)
    return candidates_with_skill


def get_formatted_candidates(candidates):
    result_str = ''
    for candidat in candidates:
        result_str += f'''
<pre>
  ---------------------------------------
  ФИО: {candidat["name"]}
  Возраст: {candidat["age"]}, пол: {candidat["gender"]}
  Должность: {candidat["position"]}
  Навыки: {candidat["skills"]}

<pre>'''
    return result_str if result_str else 'Список кандидатов пуст'


def get_formatted_candidate(candidate):
    return f'''<img src="{candidate["picture"]}">
<pre>
  ---------------------------------------
  ФИО: {candidate["name"]}
  Возраст: {candidate["age"]}, пол: {candidate["gender"]}
  Должность: {candidate["position"]}
  Навыки: {candidate["skills"]}
<pre>'''
