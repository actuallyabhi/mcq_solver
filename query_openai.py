import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def process_image(base64_image):
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Given the image below, There is MCQ question of Cognitive Aptitude Test. Return the correct answer. Also provide the reasoning for the answer.\n Response format should be in valid JSON object. {\"answer\": \"A\", \"reasoning\": \"Because...\"}"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "data:image/png;base64," + base64_image
                        },
                    },
                ],
            }
        ],
    )

    return response.choices[0].message.content


# api_key = os.getenv("OPENAI_API_KEY")
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": f"Bearer {api_key}"
# }

    # payload = {
    #   "model": "gpt-4-vision-preview",
    #   "messages": [
    #     {
    #       "role": "user",
    #       "content": [
    #         {
    #           "type": "text",
    #           "text": "Given the image below, There is MCQ question of Cognitive Aptitude Test. Return the correct answer. Also provide the reasoning for the answer."
    #         },
    #         {
    #           "type": "image_url",
    #           "image_url": {
    #             "url": f"data:image/png;base64,{base64_image}"
    #           }
    #         }
    #       ]
    #     }
    #   ],
    #   "max_tokens": 300,
    #   "temperature": 0,
    #   "response_format": {

    #   }
    # }

    # response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    # return response.json()
