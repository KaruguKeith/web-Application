from flask import Flask #IMPORT FLASK
app= Flask(__name__) # CREATE AN INSTANCE OF FLASK .this exposes the app route decorator


#ROUTE METHOD 1


@app.route('/')#Decorators are a standard feature of the Python language. A com‐mon use of decorators is to register functions as handler functions to be invoked when certain events occur.
               #app.route decorator is the preferred method to register view functions
def index():#The example registers function index() as the handler for the application’s root URL.
            #INDEX IS A VIEW FUNCTION
    return '<h1>Hello world</h1>'#RESPONSE THE CLIENT RECEIVES
                                 #Embedding response strings with HTML code in Python source files leads to code that is difficult to maintain.


#ROUTE METHOD 2


def index():
    return '<h1> Hello world<h1/>'

app.add_url_rule('/', 'index', index)#takes three argu‐ments: the URL('/'), the endpoint name('index'), and the view function(index).


#DYNAMIC ROUTE. The portion of the route URL enclosed in angle brackets i.e <name> is the dynamic part
#STATIC PART . the user part is the static part
#AnyURLs that match the static portions will be mapped to this route, and when the view function is invoked, the dynamic component will be passed as an argument. i.e The name


@app.route('/user/<name>')
def user(name):
 return '<h1>Hello, {}!</h1>'.format(name)
#In the preceding example, the name argument is used to generate a response that includes a personalized greeting.



#The dynamic components in routes are strings by default but can also be of different types. 
'''the dynamic components in routes are strings by default but can also be of different types.below codematch only URLs that have an integer in the id dynamic segment, such as /user/123. 
    @app.route('/user/ <int:id>)
Flask supports the types string, int, float, and path for routes. The path type is a special string type that caninclude forward slashes, unlike the string type.
'''

