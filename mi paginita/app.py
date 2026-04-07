from flask import Flask, render_template

app = Flask(__name__)

# RUTA 1: La página principal (Home)
@app.route('/')
def home():
    return render_template('index.html')

# RUTA 2: La nueva página de la historia
@app.route('/historia')
def historia():
    return render_template('historia.html')

if __name__ == '__main__':
    app.run(debug=True)
