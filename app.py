from flask import Flask, render_template, request, redirect, url_for, flash


#no
from flask import Flask, render_template, redirect, url_for, request, session, jsonify
from datetime import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta' 
#no 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///citybike.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


ids_registrados = ['123456', '654321']



usuario_prueba = {
    'id': 1,
    'nombre': 'alex',
    'apellido': 'acevedo',
    'email': 'a@.com',
    'password': '1',  
    'fecha_registro': datetime(2025, 1, 1),
    'tipo_membresia': 'Premium'
}



@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        idioma = request.form.get('idioma', '').strip()
        nombre = request.form.get('nombre', '').strip()
        apellidos = request.form.get('apellidos', '').strip()
        identificacion = request.form.get('identificacion', '').strip()
        telefono = request.form.get('telefono', '').strip()
        email = request.form.get('email', '').strip()
        contrasena = request.form.get('contrasena', '').strip()
        confirmar = request.form.get('confirmarContrasena', '').strip()
        nombre_usuario = request.form.get('NombreUsuario', '').strip()

        errores = {}

        if not idioma:
            errores['idioma'] = "Selecciona un idioma."
        if not nombre:
            errores['nombre'] = "El nombre es obligatorio."
        if not apellidos:
            errores['apellidos'] = "Los apellidos son obligatorios."
        if not identificacion.isdigit():
            errores['identificacion'] = "La identificación debe ser solo números."
        elif identificacion in ids_registrados:
            errores['identificacion'] = "Este ID ya está registrado."
        if not telefono:
            errores['telefono'] = "El teléfono es obligatorio."
        if '@' not in email:
            errores['email'] = "El email debe tener un @."
        if not contrasena:
            errores['contrasena'] = "La contraseña es obligatoria."
        if contrasena != confirmar:
            errores['confirmar'] = "Las contraseñas no coinciden."

        if errores:
            return render_template('registro.html', errores=errores, 
                                   idioma=idioma,
                                   nombre=nombre, apellidos=apellidos,
                                   identificacion=identificacion,
                                   telefono=telefono, email=email,
                                   nombre_usuario=nombre_usuario)
        
        flash("Registro exitoso")
        return redirect(url_for('inicio'))

    return render_template('registro.html', errores={},
                           idioma='', nombre='', apellidos='',
                           identificacion='', telefono='',
                           email='', nombre_usuario='')
    
      

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario', '').strip()
        contrasena = request.form.get('contrasena', '').strip()

        if (usuario in ['alex', 'a@.com']) and contrasena == '1':
            session['usuario_id'] = usuario  # Guardar en la sesión
            flash('Inicio de sesión exitoso')
            return redirect(url_for('inicio'))  
        else:
            flash('Credenciales inválidas. Intenta de nuevo.')
            return redirect(url_for('login'))

    return render_template('login.html')



@app.route('/mapa')
def mapa():
    return render_template('mapa.html')


@app.route('/planes')
def planes():
    return render_template('planes.html')


@app.route('/puntos')
def puntos():
    return render_template('puntos.html')



@app.route('/logout')
def logout():
    session.pop('usuario_id', None)
    return redirect(url_for('login'))


@app.route('/perfil')
def perfil():
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
    
    usuario_id = session['usuario_id']
    
    
    return render_template(
        'perfil.html', 
       
    )





if __name__ == '__main__':
    app.run(debug=True)
