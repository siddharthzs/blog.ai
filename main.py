from flask import Flask, request, jsonify
from dotenv import load_dotenv
from dto import validate_blogai_dto


from scrapperHelper import ScrapHelper
from openaiHelper import OpenAIClient


load_dotenv()
app = Flask(__name__)

scrap = ScrapHelper()
chatgpt = OpenAIClient()

@app.route("/api/scrap", methods=["POST"])
def scrapePage():
    return scrap.getTextFromHttpLink("https://scope3.com/about")


@app.route("/api/blogpost", methods=["POST"])
def handleBlogAIPost():
    data = request.get_json()
    # Validate the data using our DTO
    validation_errors = validate_blogai_dto(data)
    if validation_errors:
        return jsonify({"errors": validation_errors}), 400

    aboutCompanyData = ""
    for url in data["blogAi"]["scrap"]["AboutUs"]:
        aboutCompanyData += scrap.getTextFromHttpLink(url)
        aboutCompanyData += " " * 30

    sampleBlogPost = []
    for blog in data["blogAi"]["scrap"]["sampleBlogPost"]:
        sampleBlogPost.append(scrap.getTextFromHttpLink(blog))

    response = chatgpt.generateBlogPost(
        data["model"],
        data["blogAi"]["include"]["blogTitle"],
        aboutCompanyData,
        sampleBlogPost,
        data["blogAi"]["include"]["additionalRequirement"],
        data["version"],
    )

    #remove extra text
    startIdx = response.find("<!DOCTYPE html>")
    endIdx = response.find("</html>") + len("</html>")
    htmlResponse = response[startIdx:endIdx]

    return htmlResponse, 200


if __name__ == "__main__":
    app.run(port=8080, debug=True)
