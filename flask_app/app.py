import numpy as np
import os
from flask import Flask, request, render_template
import pickle
app = Flask(__name__)

# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     )

#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)

#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass

def test():
    return 1
@app.route('/')
def home():
    return render_template('main.html')

@app.route('/predict', methods=["POST"])
def predict():
    csv_file = request.form.values()
    # prediction = model.predict(csv_file)
    prediction = test()
    return render_template('main.html', prediction_text = prediction)
app.run()
    # return app