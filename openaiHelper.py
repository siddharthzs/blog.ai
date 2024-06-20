import os
from openai import OpenAI


class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
        )

    def generateBlogPost(self,modelName, title, aboutCompanyData, sampleBlogPost = [], additionalRequirement = [], version = 1):
        modelType = {
            "GPT3": "gpt-3.5-turbo-1106",
            "GPT4": "gpt-4o"
        }

        message = [{
                    "role": "system",
                    "content": "You are a professional SEO friendly blog content writer, skilled in writing good SEO friendly blogs which people likes to read.",
                }]
        
        if(aboutCompanyData):
            message.append({
                "role": "user",
                "content": f"Here is the Information About My Company For Which You have to Write Blogs\n --- {aboutCompanyData}"
            })
        
        if(len(sampleBlogPost) > 0):
            chat = {
                "role": "user",
                "content": "Here are some sample blogs, to know about the writting style, formatting I like when writing blogs.\n"
            }

            for i, blog in enumerate(sampleBlogPost):
                chat["content"]+= f" {i+1}: {blog}\n\n"

            message.append(chat)


        finalMessage = {
            "role": "user",
            "content": f"Write a good Blog Post on {title} using the above information. Also follow the below instructions:\n"
        }

        for i, info in enumerate(additionalRequirement): 
            finalMessage["content"] += f" {i+1}: {info}\n"

        finalMessage["content"] += "\n\n Give me HTML code Which is SEO friendly, Well Design, Colorful, and Responsive"
        message.append(finalMessage)

        print(modelType, modelName)
        print(modelType.get(modelName, None), modelType.keys())
        # print(modelType[modelName])
        # response = self.client.chat.completions.create(
        #     model=modelType[modelName],
        #     messages=message
        # )
        # print(response.choices[0].message.content)
        # return response.choices[0].message.content
        return ""
    
