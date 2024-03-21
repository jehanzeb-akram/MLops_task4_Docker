from flask import Flask, request, jsonify
from joblib import load

app = Flask(__name__)

# Load the pre-trained model
model = load('iris_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['features']])
    return jsonify(prediction=int(prediction[0]))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
