from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.logic import TimeLogicAdapter, MathematicalEvaluation
from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize a new ChatterBot instance and train it on some data
chatbot = ChatBot('My Chatbot', logic_adapters=[
        {'import_path': 'chatterbot.logic.BestMatch'},
        {'import_path': 'chatterbot.logic.LowConfidenceAdapter',
         'threshold': 0.6,
         'default_response': 'I am sorry, but I do not understand.'},
        {'import_path': 'chatterbot.logic.TimeLogicAdapter'},
        {'import_path': 'chatterbot.logic.MathematicalEvaluation'}
    ])
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Define a route for the chatbot interface
@app.route("/")
def home():
    return render_template("index.html")

# Define a route for generating chatbot responses
@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    bot_response = chatbot.get_response(user_input)
    return str(bot_response)

if __name__ == "__main__":
    app.run(debug=True)
