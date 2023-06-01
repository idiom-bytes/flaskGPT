from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

chat = ChatOpenAI(
    temperature=1.0,
    max_tokens=100,
    model_name="gpt-3.5-turbo",
    verbose=True
)

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api/prompt', methods=['POST'])
def prompt():
    data = request.get_json()
    prompt = data.get('prompt', '')

    messages = [
        SystemMessage(content="You are a funny chatboth only capable of answering one question at a time. Remember to have fun!"),
        HumanMessage(content=prompt)
    ]

    output = chat(messages)
    return jsonify({'response': output.content})

if __name__ == '__main__':
    app.run(port=3000)