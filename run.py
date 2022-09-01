import os
from flask import Flask, render_template

# name is a built in python variable. Its the name of the applications module?
# This is needed so flask knows where to look for templates and static files!
app = Flask(__name__)

# This is a python decorator: @, it tells flask what URL should trigger the
# following function, in this case its the root directory '/':


@app.route("/")
def index():
    '''
    This function runs when the root directory is accessed
    This is triggered by the app.route decorator which takes the
    / as its parameter. This returns an index.html file which is 
    rendered by the render_template method.
    '''
    return render_template('index.html')


@app.route("/about")
def about():
    '''
    This function runs when the about directory is accessed
    This is triggered by the app.route decorator which takes the
    /about as its parameter. This returns an about.html file which is 
    rendered by the render_template method.
    '''
    return render_template('about.html')


@app.route("/contact")
def contact():
    '''
    This function runs when the contact directory is accessed
    This is triggered by the app.route decorator which takes the
    /contact as its parameter. This returns an contact.html file which is 
    rendered by the render_template method.
    '''
    return render_template('contact.html')


@app.route("/careers")
def careers():
    '''
    This function runs when the careers directory is accessed
    This is triggered by the app.route decorator which takes the
    /careers as its parameter. This returns an careers.html file which is 
    rendered by the render_template method.
    '''
    return render_template('careers.html')


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get('PORT', '5000')),
        debug=True)
