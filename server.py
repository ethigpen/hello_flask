from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')  # The "@" decorator associates this route with the function immediately following  
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/success')
def success():
    return 'success'


@app.route('/dojo')
def dojo():
    return 'Dojo!'


@app.route('/say/<name>')
def say(name):
    return f'Hi {str(name)}!'


@app.route('/repeat/<num>/<word>')
def repeat(num,word):
    something= ''
    for i in range(0,int(num)):
        something += f'{str(word)} '
    return something


@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry! No response, try again!'

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
