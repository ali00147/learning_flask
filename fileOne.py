from flask import json
from flask import request
from flask import Flask

app= Flask(__name__)

@app.route("/")
def apiroot():
    return "welcome Maslah"

@app.route("/github",methods=["POST"])
def apigithub():
    if request.headers["Content_Type"]=="application/json":
        return json.dumps(request.json)


if __name__=="__main__":
    app.run(debug=False, port=50001)


