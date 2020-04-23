from jinja2 import Template

flask_template = {
    "requirements.txt": "ok",
    "config.py": "oka"
}


def render_template(file):
    flask_template.get('config,py')
    func = flask_template.get(file, lambda : 'invalid')
    type(func)
    return func()
