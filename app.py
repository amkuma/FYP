from flask import Flask, request, jsonify
from prediction import predict_bipolarity

def create_app():
    app = Flask(__name__)

    @app.route('/predict', methods=['POST'])
    def predict():
        try:
            data = request.get_json(force=True)
            user_input = data['input']
            prediction_result = predict_bipolarity(user_input)
            return jsonify(prediction_result)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
