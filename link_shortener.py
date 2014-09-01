from flask import Flask, render_template, request, redirect, url_for, Markup

app = Flask(__name__)
url_list = ['http://ogoloda.li']

@app.route('/')
def template_renderer(name=None):
	return render_template('link_shortener.html', name=name)

@app.route('/urls', methods=['POST']) #fix this
def store_urls():
	url_list.append(request.form['link'])
	url = url_for('return_link', id=str(len(url_list) - 1))
	full_url = 'http://127.0.0.1:5000' + url
	return Markup('<h1>Here\'s your new link!</h1><a href=" %s " > %s </a>') % (full_url, full_url)

@app.route('/l/<id>')
def return_link(id=None):
	return redirect(url_list[int(id)])

if __name__ == '__main__':
    app.run()