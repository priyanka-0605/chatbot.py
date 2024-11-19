# a reference to the Natural Language Toolkit (NLTK), which is a popular open-source library used for natural language processing (NLP) in Python.
import nltk
from nltk.chat.util import Chat, reflections
nltk.download('punkt')
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How can I assist you today?",]
    ],
    [
        r"hi|hello|hey",
           ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!","what about you?"]
    ],
     [
        r"i am fine|i am doing good as well|thanks for the concern",
        ["That's great to hear !"]
    ],
     [
        r"what is your name?",
        ["My name is chatbot","I am a chatbot created to assist you.", "You can call me Chatbot."]
    ],
    [ r"quit",
        ["Bye! Take care.", "It was nice talking to you!"]
    ],
     [ r"how can we stop procastinate ?",
        ["you need to make a healthy routine .eat healthy,stay hydrated,meditate,take a morning walk"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that.", "Can you rephrase that?"]
    ],
]
chatbot = Chat(pairs,reflections)
print("Hi! I'm a chatbot. how may i assist you,Type 'quit' to exit.")
chatbot.converse()
# The NLTK library provides a range of tools and resources for processing and analyzing natural language data, such as tokenization, stemming, tagging, parsing, semantic reasoning, and more
