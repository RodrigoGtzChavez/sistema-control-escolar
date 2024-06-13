from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estudiantes')
def estudiantes():
    data = [
        {"matricula": "230701", "nombre": "Gerardo", "apellido_paterno": "Mathus",
         "apellido_materno": "Gómez Sandoval"},
         {"matricula": "230702", "nombre": "Alberto", "apellido_paterno": "Preciado",
         "apellido_materno": "Férnandez"},
         {"matricula": "230703", "nombre": "Elsa", "apellido_paterno": "Serrano",
         "apellido_materno": "Salcedo"},
         {"matricula": "230704", "nombre": "Isabel", "apellido_paterno": "López",
         "apellido_materno": "Acero"}
    ] 

    return render_template('estudiantes.html', data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)