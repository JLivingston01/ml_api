from flask import Flask, jsonify, request


from calculations import get_predictions,models

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "Hello, World!"

@app.route("/api_v1/predict/cards=<int:cards>&length=<int:length>&model_id=<string:model_id>")
def predict(cards,length,model_id):
    

    return jsonify(get_predictions(cards,length,model_id))

app.run(port=5000,debug=True)


