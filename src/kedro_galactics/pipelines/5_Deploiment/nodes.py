"""
This is a boilerplate pipeline 'Deploiment'
generated using Kedro 0.18.10
"""

# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)
# Define Flask route for POST requests
@app.route("/predict", methods=["POST"])

def predict():
    # Set the filepath to save the POST request data
    filepath = "where_i_want_to_save_my_data"

    # Save data from POST request to JSON file
    save_from_post_request(request, filepath)
    with KedroSession.create("kedro-galactics", project_path=".") as
    session:
        processed_data = session.run(
                pipeline_name ="", # Le nom du pipe à exécuter
        ) 
    output = pd.read_csv('PATH/Data')
    return output.to_json(orient='records')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=False)