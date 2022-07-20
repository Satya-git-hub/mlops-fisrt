from crypt import methods
from flask import Flask, render_template, request, jsonify
import os
import yaml
import joblib
import numpy as np
from src.get_data import read_config

webapp_root = "webapp"
params_path = "params.yaml"
static_dir = os.path.join(webapp_root, "static")
template_dir = os.path.join(webapp_root, "templates")

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)


def predict(data):
    config = read_config(params_path)
    model_path = config["webapp_model_dir"]
    model = joblib.load(model_path)
    prediction = model.predict(data)
    return prediction[0]


def api_response(request):
    data = np.array([list(request.json.values())])
    response = predict(data)
    return {"response" : response}
    '''
    {
    "alcohol": "11.9", 
    "chlorides": "0.5", 
    "citric_acid": "0.6", 
    "density": "1", 
    "fixed_acidity": "5.6", 
    "free_sulfur_dioxide": "69.72", 
    "pH": "3.74", 
    "residual_sugar": "11.3", 
    "sulphates": "1.75", 
    "total_sulfur_dioxide": "114.221", 
    "volatile_acidity": "1.5"
    }
    '''

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            if request.form:
                data = dict(request.form).values()
                data = [list(map(float, data))]
                response = predict(data)
                return render_template("index.html", response=response)
            elif request.json:
                response = api_response(request)
                return jsonify(response)
        except Exception as e:
            print(e)
            error = "Something went WRONG !!!"
            render_template("404.html", error=error)

    else:
        return render_template("index.html")


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    app.run(host, port, debug=True)
