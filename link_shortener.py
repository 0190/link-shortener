from flask import Flask, render_template, request, redirect, url_for, Markup
from urlparse import urlparse

app = Flask(__name__)
url_list = ['http://ogoloda.li']
valid_protocols = ['http', 'https']

@app.route('/')
def index():
	return render_template('link_shortener.html')

@app.route('/newlink', methods=['POST']) #fix this
def process_input():
	link_name = request.form['link']
	parsed_link = urlparse(link_name)
	if parsed_link.scheme in valid_protocols and parsed_link.netloc:
		url_list.append(link_name)
		url = url_for('return_link', id=str(len(url_list) - 1), _external=True)
		return render_template('shortened.html', link=link_name, url=url)
	else:
		return redirect('/error')

@app.route('/l/<id>')
def return_link(id=None):
	try:
		return redirect(url_list[int(id)])
	except IndexError:
		print 'no id', id
		return render_template('no_page_error.html')

@app.route('/error')
def error():
	return render_template('processing_error.html')

if __name__ == '__main__':
    app.run()