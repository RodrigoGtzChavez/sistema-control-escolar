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

@app.route('/materias')
def materias():
    materias = [
        {"clave": "701", "asignatura": "Analisis y Diseño de Algoritmos", "cuatrimestre": "Primero",
         "promedio": "10"},
         {"clave": "702", "asignatura": "UX", "cuatrimestre": "Primero",
         "promedio": "9.8"},
         {"clave": "703", "asignatura": "Tecnologia, Sociedad y Futuros Posibles", "cuatrimestre": "Primero",
         "promedio": "8"},        
    ] 
    return render_template('materias.html', materias=materias)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)