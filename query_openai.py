import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def process_image(image_url):
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        temperature=0,
        response_format={
            "type": "json_object",     
        },
        max_tokens=300,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "In the given image, There is MCQ question of Cognitive Aptitude Test.Return the correct answer. Do not return A,B or 1,2. Also provide the reasoning for the answer.\nResponse format should be in valid JSON object in following format. \n{\"answer\": \" 10KM/hour\", \"reasoning\": \"Because...\"}"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url    
                        }
                    },
                ],
            }
        ],
    )

    return response.choices[0].message.content


