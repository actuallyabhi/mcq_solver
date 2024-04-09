import json

def load_json(data): 
    try:
        json_data = json.loads(data)
        answer = json_data.get("answer")
        reasoning = json_data.get("reasoning")
        return answer, reasoning
    except (json.JSONDecodeError, Exception):
        return str(data), "No reasoning provided"