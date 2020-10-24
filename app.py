from flask import Flask, render_template, request
import requests


app = Flask(__name__)
first_options_list = "animal, career, celebrity, dev, explicit, fashion, food, history, money, movie, music, political, religion, science, sport, travel"


@app.route('/')
def hello_world():
    category = request.args.get('category')
    if not category:
      return render_template('index.html', categories=first_options_list)
    options_list = requests.get('https://api.chucknorris.io/jokes/categories')
    options_list = options_list.json()
    options_list =', '.join(options_list)
    if category not in options_list:
      return render_template('index.html', categories=options_list, wrong="Choose another")
    the_joke = requests.get(f'https://api.chucknorris.io/jokes/random?category={category}').json()
    joke = the_joke['value']
    return render_template(
      'index.html',
      categories=options_list,
      category=category,
      joke=joke,
      )

if __name__ == '__main__':
    app.run(debug=True)