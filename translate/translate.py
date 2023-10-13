from googletrans import Translator

with open('input.txt', 'r') as file:
    text = file.read()

translator = Translator()
translated_text = translator.translate(text, dest='en').text

with open('output.txt', 'w') as file:
    file.write(translated_text)