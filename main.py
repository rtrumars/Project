from flask import Flask, render_template, request

app = Flask('app')

@app.route('/')
def main():
  return render_template('main.html')

if __name__ == "__main__":
    app.run(threaded=True, port=5000)