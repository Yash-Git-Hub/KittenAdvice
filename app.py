from flask import Flask, render_template
import requests
import json
app = Flask(__name__,template_folder='./templates',static_folder='./static')
@app.route('/')

def home():
    p=getadvice()
    return render_template('index.html',value=mm(p))
def getadvice():
        p=[]
        z=0
        while z<=3:
            x=requests.get("https://api.adviceslip.com/advice")
            x=json.loads(x.text)
            y=x["slip"]["advice"].split(" ")
            z=len(y)
        z=z//3
        p.append(" ".join(y[:z]))
        p.append(" ".join(y[z:z+z]))
        p.append(" ".join(y[z+z:]))
        z=0
        return(p)
def mm  (x):
    return(" ".join(map(str,x)))

if __name__ == '__main__':
    app.run(threaded=True, port=5000)

