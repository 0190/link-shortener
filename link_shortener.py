from flask import Flask, render_template, request, redirect, url_for, Markup
from urlparse import urlparse

app = Flask(__name__)
url_list = ['http://ogoloda.li']
valid_protocols = ['http', 'https']

@app.route('/')
def template_renderer(name=None):
	return render_template('link_shortener.html', name=name)

@app.route('/urls', methods=['POST']) #fix this
def store_urls():
	link_name = request.form['link']
	parsed_link = urlparse(link_name)
	if parsed_link.scheme in valid_protocols and parsed_link.netloc:
		url_list.append(link_name)
		url = url_for('return_link', id=str(len(url_list) - 1), _external=True)
		return Markup('<h1>Here\'s your new link!</h1><a href=" %s " > %s </a>') % (url, url)
	else:
		return redirect('/error')

@app.route('/l/<id>')
def return_link(id=None):
	return redirect(url_list[int(id)])

@app.route('/error')
def error():
	return Markup('<h1>There seems to be a problem with your link</h1> \
		<p>Note that we only work with http and https links.</p> \
		<p>Please check the link format and <a href="/">try again</a>.</p>')

if __name__ == '__main__':
    app.run()