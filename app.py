from flask import Flask
from utils import (load_candidates,
                   get_candidate_by_id,
                   get_candidates_by_skill,
                   get_formatted_candidates,
                   get_formatted_candidate)

app = Flask(__name__)


@app.route("/")
def index():
    return get_formatted_candidates(load_candidates())


@app.route("/candidates/<int:id>")
def candidate_by_name(id):
    candidate = get_candidate_by_id(load_candidates(), id)
    if candidate is None:
        return f'Кандидат с id={id} не найден'
    return get_formatted_candidate(candidate)


@app.route("/skills/<skill>")
def candidates_by_skill(skill):
    return get_formatted_candidates(get_candidates_by_skill(load_candidates(), skill))


if __name__ == '__main__':
    app.run()
