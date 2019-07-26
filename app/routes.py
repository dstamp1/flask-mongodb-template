import os
from app import app
from flask import render_template, request, redirect

from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'database-name' 

# URI of database
app.config['MONGO_URI'] = 'mongo-uri' 

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')
def index():
    #Connect to the DB with the mongo object
    
    #Use the .find() method to return all of the events
    events = []
    return render_template('index.html', events = events)

#This route will handle the POST of our form. It should also be able to redirect to homepage on a GET request
@app.route('/addevent')
def add_event():
    
    return render_template('add_event.html')
    
    return redirect('/')