from flask import Flask, render_template,request
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/' ,methods=['GET', 'POST'])
def my_link():
    text =""
    if request.method == "POST":

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("let us hear your beautiful voice")
            r.pause_threshold = 0.8
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            #this is being printed in terminal
            print("I am printing your words in the browser :) ")

            try:
                text =r.recognize_google(audio,language='en')
                #this is being printed on the Browser
                print ( "You have said \n" + text)
            except Exception as e:
                print(e)
                print("i cant hear you :( )")
                return("reload the page and click the button. I couldnt hear you :( ")
    return render_template("index.html",text=text)
    document['btn'].bind("click",my_link)

if __name__ == '__main__':
  app.run(debug=True)
