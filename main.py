from flask import Flask, request, jsonify

from dto import validate_blogai_dto
from openaiHelper import OpenAIClient


app = Flask(__name__)


@app.route('/api/blogpost', methods=['POST'])
def handleBlogAIPost():
    data = request.get_json()
    # Validate the data using our DTO
    validation_errors = validate_blogai_dto(data)
    if validation_errors:
        return jsonify({"errors": validation_errors}), 400

    return jsonify("Hello"), 200
    



if __name__ == '__main__':
    app.run(port=8080,debug=True)
