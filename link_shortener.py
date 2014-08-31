from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def template_renderer(name=None):
    return render_template('link_shortener.html', name=name)

@app.route('/urls', methods=['POST']) #fix this
def store_urls():
	url = request.form['url']

if __name__ == '__main__':
    app.run()