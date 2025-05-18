from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # necesario para mensajes flash

# Simulamos IDs registrados (en realidad sería base de datos)
ids_registrados = ['123456', '654321']

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Recoger datos del formulario
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

        # Validaciones
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
        
        # Aquí agregarías el código para guardar los datos en la base de datos
        flash("Registro exitoso")
        return redirect(url_for('inicio'))

    # GET
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
        email = request.form.get('email', '').strip()
        contrasena = request.form.get('contrasena', '').strip()

        # Simulación de usuario existente
        if email == 'ejemplo@correo.com' and contrasena == '1234':
            flash('Inicio de sesión exitoso')
            return redirect(url_for('home'))  # Cambia a tu ruta post-login
        else:
            flash('Credenciales inválidas. Intenta de nuevo.')
            return redirect(url_for('login'))

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
