'''
All Flask applications must create an application instance. The web server passes all
requests it receives from clients to this object for handling, using a protocol called
Web Server Gateway Interface (WSGI, pronounced “wiz-ghee”).

'''
#The application instance is an object of class Flask, usually created as follows:
from flask import Flask
import flask
app = flask(__name__)
'''
The only required argument to the Flask class constructor is the name of the main
module or package of the application. For most applications, Python’s __name__ vari‐
able is the correct value for this argument.

Flask uses this argument to determine the location of the applica‐
tion, which in turn allows it to locate other files that are part of the
application, such as images and templates.

'''