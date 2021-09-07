from flask import Flask, render_template, request, jsonify, Response

import bot
import utils

app = Flask(__name__)

#Route
@app.route("/chat", methods = ["POST"])
def chat():

    request_data = request.get_json()
    message= request_data["message"]

    data = {}
    status, response = bot.chat(message)
    if status == 0:
        data["reply"] = response
        data["status"] = 'Success'
        return jsonify(data)
    else: 
        data["reply"] = response
        data["status"] = 'Failed'
        return jsonify(data)


'''
#Route
@app.route("/test", methods = ["POST"])
def test():
    request_data = request.get_json()
    message= request_data["message"]
    return jsonify(utils.save(message)) #pass
'''




#app run
if __name__ == "__main__":
    app.run()

