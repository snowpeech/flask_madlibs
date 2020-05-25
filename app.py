from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import fairy,vacation,airplane

app=Flask(__name__)
app.config['SECRET_KEY'] = "words"
debug = DebugToolbarExtension(app)

@app.route('/home')
def pick_story():
    return render_template("choice.html")

@app.route('/form')
def input_madlib():
    print(airplane)
    blurb = request.args["topic"]
    print(f"blurb: {blurb}")
    
    blurb.prompts
    print(f"qs:{qs}")
        
    return render_template("form.html",prompts=qs)

@app.route('/story')
def filled_story():
    ans = request.args  
    
    tale = story.generate(ans)
    return render_template("story.html",tale = tale)