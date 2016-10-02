import os
from flask import Flask, render_template, json, jsonify
app = Flask(__name__)

def getJson(name):
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT, 'static', 'data/' + name)
        projects = json.load(open(json_url))
        return projects

# Homepage
@app.route("/")
def main():
    projects = getJson("projects.json")
    return render_template('home.html', projects=projects)

@app.route("/<project>")
def stock(project):
    projects = getJson("projects.json")
    selected_project = None
    for p in projects:
        if p == project:
            selected_project = projects[p]
    return render_template('item.html', project=selected_project)

if __name__ == "__main__":
    app.run(debug=True)
