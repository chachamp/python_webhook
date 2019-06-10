import json


def read_data():
    file_data ="app/data/data.json"
    file = open(file_data, 'r')
    source = file.read()
    file.close()

    y = json.loads(source)
    # Convert from JSON to Python:
    user_id = y["entry"][0]["id"]
    print (user_id)

read_data()


