from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')  # The "@" decorator associates this route with the function immediately following  
def hello_world():
    return render_template('index.html', phrase='hello', times=5)


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/dojo')
def dojo():
    return 'Dojo!'


@app.route('/say/<name>')
def say(name):
    return f'Hi {str(name)}!'


@app.route('/repeat/<int:num>/<string:word>')
def repeat(num,word):
    something= ''
    for i in range(0,num):
        something += f'{word} '
    return something


@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry! No response, try again!'




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
