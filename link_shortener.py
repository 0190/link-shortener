from flask import Flask, render_template, request, redirect

app = Flask(__name__)
url_list = ['http://ogoloda.li']

@app.route('/')
def template_renderer(name=None):
    return render_template('link_shortener.html', name=name)

@app.route('/urls', methods=['POST']) #fix this
def store_urls():
	url_list.append(request.form['link'])
	return 'OK!'

@app.route('/l/<id>')
def return_link(id=None):
	return redirect(url_list[int(id)])

if __name__ == '__main__':
    app.run()