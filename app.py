import os
import tempfile
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from query_openai import process_image
import base64
from helpers import load_json



app = Flask(__name__)
CORS(app)

@app.route('/process_image_with_openai', methods=['POST'])
@cross_origin(origin='*')
def process_image_with_openai():
    try:
        image = request.files.get('file')
        if not image:
            return jsonify({
                "result": "Image is required"
            })
        with tempfile.NamedTemporaryFile(delete=True) as temp:
            image.save(temp)
            image_path = temp.name
            with open(image_path, "rb") as img_file:
                base64_img = base64.b64encode(img_file.read()).decode('utf-8')
                result = process_image(base64_img)
                answer, reasoning = load_json(result)
                return jsonify({
                        "answer": answer,
                        "reasoning": reasoning
                    })
    except Exception as e:
        return jsonify({
            "answer": "Error occurred",
            "reasoning": str(e)
        })

if __name__ == '__main__':
    load_dotenv()
    is_dev = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=is_dev)