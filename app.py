from flask import Flask, render_template, request
from chatbot import predict_class, get_response, intents

app = Flask(__name__)
app.config['SECRET_KEY'] = "a_secret_key_12345"

response_list = []

@app.route("/")
def home():
    global response_list
    response_list.clear()
    return render_template("index.html")

@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():
    global response_list
    if request.method == "POST":
        message = request.form['message']
        message = message.lower()
        response_list.append(message)
        ints = predict_class(message)
        res = get_response(ints, intents)
        response_list.append(res)
        if len(response_list) > 5:
            response_list.remove(response_list[0])
        return render_template("chatbot.html", message=message, response_list=response_list)
    return render_template("chatbot.html", message="", response_list=response_list)

if __name__ == "__main__":
    app.run(debug=True)
