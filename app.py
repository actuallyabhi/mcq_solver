import os
import traceback
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from query_openai import process_image


from helpers import load_json



app = Flask(__name__)
CORS(app)

@app.route('/process_image_with_openai', methods=['POST'])
@cross_origin(origin='*')
def process_image_with_openai():
    try:
        image_url = request.data
        if not image_url:
            return jsonify({
                "answer": "No image provided",
                "reasoning": "No reasoning provided"
            })

        result = process_image(image_url.decode("utf-8"))
        answer, reasoning = load_json(result), ""
        print(answer, reasoning)
        return jsonify({
                "answer": answer,
                "reasoning": reasoning
            })
            
    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "answer": "Error occurred",
            "reasoning": str(e)
        })

if __name__ == '__main__':
    load_dotenv()
    is_dev = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=is_dev)