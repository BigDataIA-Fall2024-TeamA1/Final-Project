import json

def test_json():
    data = {"test": "value"}
    return json.dumps(data)

print(test_json())