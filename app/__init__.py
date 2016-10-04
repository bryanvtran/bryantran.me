import os
from flask import Flask, render_template, json, jsonify
from collections import OrderedDict
app = Flask(__name__)

def getJson(name):
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, 'static', 'data/' + name)
        projects = json.load(open(json_url), object_pairs_hook=OrderedDict)
        return projects

# Homepage
@app.route("/")
def main():
    projects = getJson("projects.json")
    return render_template('home.html', projects=projects)

@app.route("/<project>")
def proj(project):
    projects = getJson("projects.json")
    selected_project = None
    for p in projects:
        if p['slug'] == project:
            selected_project = p
    return render_template('item.html', page=project, project=selected_project)

if __name__ == "__main__":
    app.run(debug=True)
