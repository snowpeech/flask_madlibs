from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app=Flask(__name__)
app.config['SECRET_KEY'] = "words"
debug = DebugToolbarExtension(app)

@app.route('/')
def pick_story():
    return render_template("choice.html")

@app.route('/form')
def input_madlib():
    
    blurb = request.args["topic"]
    topic=stories.get(blurb)
    
    qs=topic.prompts
        
    return render_template("form.html",prompts=qs, topic=blurb)

@app.route('/story')
def filled_story():
    topic = request.args["topic"]
    story=stories.get(topic)


    tale = story.generate(request.args)

    return render_template("story.html",tale = tale)