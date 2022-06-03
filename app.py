from flask import Flask
from utils import (load_candidates,
                   get_candidate_by_name,
                   get_candidates_by_skill,
                   get_formatted_candidates, get_formatted_candidate)

app = Flask(__name__)


@app.route("/")
def index():
    return get_formatted_candidates(load_candidates())


@app.route("/candidates/<name>")
def candidate_by_name(name):
    candidate = get_candidate_by_name(load_candidates(), name)
    if candidate is None:
        return f'В списке кандидатов не найден "{name}"'
    return get_formatted_candidate(candidate)


@app.route("/skills/<skill>")
def candidates_by_skill(skill):
    return get_formatted_candidates(get_candidates_by_skill(load_candidates(), skill))


if __name__ == '__main__':
    app.run()
