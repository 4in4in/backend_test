import json
from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)


@app.route("/api/questionnaries/get_questionnary", methods=["GET"])
def get_questionnary():
    if not "questionnary_name" in request.args:
        return {"Error": "not questionnary_name argument!"}
    else:
        args = request.args
        questionnary_filename = args["questionnary_name"]
        questionnary_filename = questionnary_filename + ".json"
        with open(questionnary_filename, "r", encoding="utf-8") as q:
            questionnary = json.load(q)
        return {"response": questionnary}


@app.route("/api/qustionnaries/dump_qustionnary_answers", methods=["POST"])
def dump_qustionnary_answers():
    answers = request.json
    if answers is None:
        return {"Error!": "No answers data!"}
    else:
        questionnary_name = answers.get("questionnary_name")
        qanswers = answers.get("answers")
        print("questionnary name: {}".format(questionnary_name))
        if qanswers is not None:
            for qnum, answer in qanswers.items():
                print("  question number: {}".format(qnum))
                print("    answer: {}".format(answer))
        else:
            return {"Error!": "Not anought data!"}
    return {"test": "dumped!"}


if __name__ == "__main__":
    app.run(host="localhost")
            