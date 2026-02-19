from flask import Flask, render_template, request, jsonify
import data_base  # tu lógica de verbos

app = Flask(__name__)

@app.route("/")
def index():
    infinitives = list(data_base.present.values())  # todos los infinitivos
    return render_template("index.html", verbs=infinitives)

@app.route("/check", methods=["POST"])
def check():
    data = request.json
    infinitive = data["infinitive"].lower()
    past_input = data["past"].lower()
    present_input = data["present"].lower()

    past_correct = data_base.past.get(past_input) == infinitive
    present_correct = data_base.present.get(present_input) == infinitive

    return jsonify({"past": past_correct, "present": present_correct})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

