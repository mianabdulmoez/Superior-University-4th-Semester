from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple mock logic for the chatbot
def get_bot_response(user_input):
    user_input = user_input.lower()

    if "account" in user_input:
        return "We offer Savings, Current, and Fixed Deposit accounts. What would you like to know more about?"
    elif "loan" in user_input:
        return "We provide home loans, personal loans, and car loans. Want to check eligibility?"
    elif "branch" in user_input:
        return "You can find branch locations here: https://www.sc.com/pk/"
    elif "credit card" in user_input:
        return "We offer Platinum, Gold, and Student credit cards. Would you like to apply?"
    elif "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you with your banking needs today?"
    else:
        return "Sorry, I didn't understand that. Please ask about accounts, loans, branches, or credit cards."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    response = get_bot_response(user_input)
    return jsonify({"bot_response": response})

if __name__ == "__main__":
    app.run(debug=True)
