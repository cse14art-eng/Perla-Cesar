from flask import Flask, render_template

# 1. ESTA ES LA LÍNEA CLAVE (va aquí, al inicio)
app = Flask(__name__)

# 2. RUTA PARA LA PÁGINA PRINCIPAL
@app.route('/')
def home():
    return render_template('index.html')

# 3. RUTA PARA LA PÁGINA DE LA HISTORIA
@app.route('/historia')
def historia():
    return render_template('historia.html')

# 4. ESTO ES PARA QUE FUNCIONE EN TU PC
if __name__ == '__main__':
    app.run(debug=True)
