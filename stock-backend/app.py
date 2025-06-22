from flask import Flask, request, jsonify
from flask_cors import CORS
from stock_predictor import get_stock_prediction
from sentiment_analysis import analyze_sentiment

app = Flask(__name__)
CORS(app)  # Allow requests from React frontend

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    symbol = data.get('symbol', '').upper()

    try:
        prediction = get_stock_prediction(symbol)
        sentiment = analyze_sentiment(symbol)
        return jsonify({
            'prediction': round(prediction, 2),
            'sentiment': sentiment
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
