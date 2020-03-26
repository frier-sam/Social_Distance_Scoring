import os
from flask import Flask, render_template, request
from sds import score
import json
__author__ = 'frier-sam'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
#     print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
#         print(file)
        filename = file.filename
        destination = "/".join([target, filename])
#         print(destination)
        file.save(destination)
        s = score(destination)
#         os.remove("ChangedFile.csv")
    return json.dumps(s)

if __name__ == "__main__":
    app.run(port=4444,debug=True)
