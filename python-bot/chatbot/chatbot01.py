from chatterbot import chatbot 
from chatterbot.trainers import listtrainer 
from spacy.cli import download

download("en_core_web_sm")

class enesm:
  iso_639_ = "en_core_web_sm"
chatbot = chatbot("hackerbot", tagger_language=enesm)

conversa = [
  "Hello",
  "Hello, sir! How it going?",
  "Nice",
  "What's the matter? Something new?",
  "The ChatGPT can help ypu to programming",
  "It's wonderful man!",
  "Yes, it's actually so nice."
]

trainer = listtrainer(chatbot)
trainer.train(conversa)
while True:
  mensagem = input("Ask or say something: ")
  if mensagem == "stop":
    break
  resposta = chatbot.get_response(mensagem)
  print(resposta)