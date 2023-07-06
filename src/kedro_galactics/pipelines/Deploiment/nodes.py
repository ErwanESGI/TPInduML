"""
This is a boilerplate pipeline 'Deploiment'
generated using Kedro 0.18.10
"""

# app.py
from flask import Flask, request, jsonify
from kedro.framework.session import KedroSession
import pandas as pd

app = Flask(__name__)

# Define Flask route for POST requests
@app.route("/predict", methods=["POST"])
def predict():
    # Save data from POST request to JSON file
    #save_from_post_request(request, filepath)
    with KedroSession.create("kedro-galactics", project_path=".kedro-galactics") as session:
        processed_data = session.run(pipeline_name="training_model")
    output = pd.read_csv('')
    return output.to_json(orient='records')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=False)
