from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    nombre = ''
    total_sin_descuento = 0
    total_con_descuento = 0
    descuento_aplicado = 0

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        edad = int(request.form.get('edad'))
        tarros = int(request.form.get('tarros'))

        # Calcular el total sin descuento
        total_sin_descuento = tarros * 9000

        # Calcular descuento según la edad
        descuento = 0
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        # Calcular el descuento en pesos
        descuento_en_pesos = total_sin_descuento * descuento

        # Aplicar descuento al total
        total_con_descuento = total_sin_descuento - descuento_en_pesos

        descuento_aplicado = descuento_en_pesos

    return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento,
                           total_con_descuento=total_con_descuento, descuento_aplicado=descuento_aplicado)

@app.route('/ejercicio2')  # Agregamos la ruta para ejercicio2
def ejercicio2():
    return "Contenido del ejercicio 2"

if __name__ == '__main__':
    app.run(debug=True)