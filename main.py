from flask import Flask, render_template, request

app = Flask('app')

@app.route('/')
def home():
  return render_template('home.html')
  

if __name__ == "__main__":
    app.run(threaded=True, port=5000)