from flask import Flask,request
import json

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        data = request.get_json()
        file_data ="usr/src/pybot/app/data/data.json"

        with open(file_data, 'w') as outfile:
            json.dump(data, outfile) 
            outfile.close    

        return "OK post success"

if __name__ == '__main__':
    app.run(debug=True)

#=====================================
# Use GET method for checking json post
#=====================================
# @app.route('/get', methods=['GET'])
# def get():

#     if request.method == "GET":
#         file_data ="json_post_get/data.json"
#         # file_data = "data.json"
#         file = open(file_data, 'r')
#         source = file.read()
#         file.close()

#         return source


