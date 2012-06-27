import flask, os
from data import project_list

app = flask.Flask(__name__)

template_data = {
	'project_list' : project_list
}

@app.route("/")
def index():
	return flask.render_template('index.html', **template_data)

@app.route("/projects")
def projects():
	return flask.render_template('projects.html', **template_data)

@app.route("/project/<link>")
def project(link):
	for project in project_list:
		print project
		if project['link'] == link:
			template_data['project'] = project
			break

	return flask.render_template('project.html', **template_data)

@app.route("/experience")
def experience():
	return flask.render_template('experience.html', **template_data)


@app.route("/contact")
def contact():
	return flask.render_template('contact.html', **template_data)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)
	
if app.config['DEBUG']:
    from werkzeug import SharedDataMiddleware
    import os
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
      '/': os.path.join(os.path.dirname(__file__), 'static')
    })
	
	
	
	
	
