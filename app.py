from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    title = "Anagrams"

    text = "Update the end of the URL with '/<word>' to find anagrams for the given word."

    return render_template('home.html', title=title, text=text)


@app.route('/anagrams/<string:word>')
def anagrams(word):

    title = "Anagrams for " + word

    file = open('words.txt')

    word_list = file.read().splitlines()

    uppercase_word = word.upper()

    anagrams = []

    for w in word_list:
        if sorted(uppercase_word) == sorted(w):
            anagrams.append(w)

    return render_template('anagrams.html', title=title, anagrams=anagrams)
