import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?"]
    ],
    [
        r"hi|hello",
        ["Hello", "Hi"]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot"]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you. How can I assist you?"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye", "It was nice talking to you"]
    ]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
