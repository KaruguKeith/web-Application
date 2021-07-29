'''
web browsers send requests to the web server, which in turn sends
them to the Flask application instance. The Flask application instance needs to know
what code it needs to run for each URL requested, so it keeps a mapping of URLs to
Python functions. The association between a URL and the function that handles it is
called a route'

The most convenient way to define a route in a Flask application is through the
app.route decorator exposed by the application instance.

'''
#after creating an instance from flask , the route decoratoe is exposed
    @app.route('/')
    def index():
    return '<h1>Hello World!</h1>'
#OR
   def indxex():
       return '<h1>Hello world<h1/>'

    app.add_url_rule('/', 'index', index)
#ROUTE WITH DYAMIC COMPONENT
    @app.route('/user/<name>')
    def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

#The dynamic components in routes are strings by default but can also be of different types.below codematch only URLs that have an integer in the id dynamic segment, such as /user/123. 
    @app.route('/user/ <int:id>)
