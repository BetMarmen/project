import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///basedato.db")


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        usuario = request.form.get('usuario')
        contraseña = request.form.get('contraseña')
        # print(usuario, contraseña, confirmacion)
        if not usuario:
            flash("Rellena el campo 'Usuario'")
            return render_template('login.html')
        if not contraseña:
            flash("Rellena el campo 'Contraseña'")
            return render_template('login.html')
        row = db.execute(
            "SELECT * FROM users WHERE user = :usuario", usuario=usuario)
        if len(row) != 1 or not check_password_hash(row[0]["password"], contraseña):
            flash("El usuario o la contraseña son invalidos")
            return render_template('login.html')
        session["user_id"] = row[0]["id"]
        session["role"] = row[0]["role"]
        if row[0]["role"] == 1:
            admint="1"
            print(admint)
            return render_template("admin.html", admint=admint)
        else:
            return redirect("/")
    return render_template('login.html')

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect('/login')


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        usuario = request.form.get('usuario')
        contraseña = request.form.get('contraseña')
        confirmacion = request.form.get('confirmacion')
        role = request.form.get('role')
        # print(usuario, contraseña, confirmacion)
        if not role:
            flash("Rellena el campo 'Rol'")
            return render_template('register.html')
        if not usuario:
            flash("Rellena el campo 'Usuario'")
            return render_template('register.html')
        if not contraseña:
            flash("Rellena el campo 'Contraseña'")
            return render_template('register.html')
        if not confirmacion:
            flash("Rellena el campo 'Confirmar Contraseña'")
            return render_template('register.html')
        if contraseña != confirmacion:
            flash("Rellena el campo 'La contraseña no es la misma")
            return render_template('register.html')
        userID = db.execute(
            "SELECT * FROM users WHERE user = :usuario", usuario=usuario)
        if len(userID) == 1:
            flash("El nombre de usuario que usted ingreso ya existe")
            return render_template('register.html')
        hash = generate_password_hash(contraseña)
        print(hash)
        insert = db.execute(
            "INSERT INTO users (user, password, role) VALUES (:usuario,:hash,:role)", usuario=usuario, hash=hash, role=role)
        flash("USUARIO REGISTRADO!!!")
        IdUser = db.execute(
            "SELECT id FROM users WHERE user = :usuario", usuario=usuario)
        session["user_id"] = IdUser[0]["id"]

        return redirect("/login")
    return render_template('register.html')

@app.route("/doctores")
@login_required
def doctores():
    """Show history of transactions"""

    doctores = db.execute("SELECT * FROM doctores ")
    return render_template("doctores.html", doctores=doctores)

@app.route('/doctor/<int:id>')
def mostrar_doctor(id):
    doctor = db.execute('SELECT * FROM doctores WHERE doctor_id = ?', id)[0]

    print(doctor)


    return render_template('mostrarDoctor.html', doctor=doctor)

@app.route("/especialidades")
@login_required
def especialidades():
    doctores = db.execute('SELECT * FROM doctores;')

    return render_template("especialidades.html", doctores=doctores)

@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin():

    if request.method == "POST":
        nombre = request.form.get('nombre')
        especialidad = request.form.get('especialidad')
        disponibilidad = request.form.get('disponibilidad')
        numero = request.form.get('numero')
        correo = request.form.get('correo')
        estado = request.form.get('estado')
        foto = request.form.get('foto')

        if not nombre:
            flash("Rellena el campo 'Nombre'")
            return render_template('admin.html')
        if not correo:
            flash("Rellena el campo 'Correo'")
            return render_template('admin.html')
        if not estado:
            flash("Rellena el campo 'Estado'")
            return render_template('admin.html')
        if not disponibilidad:
            flash("Rellena el campo 'Disponibilidad'")
            return render_template('admin.html')
        if not numero:
            flash("Rellena el campo 'Numero'")
            return render_template('admin.html')
        if not especialidad:
            flash("Rellena el campo 'Especialidad'")
            return render_template('admin.html')
        if not estado:
            flash("Rellena el campo 'Estado'")
        if not foto:
            flash("Rellena el campo 'Foto'")
            return render_template('admin.html')

        insert = db.execute(
            "INSERT INTO doctores (nombre, especialidad, disponibilidad, número, correo, estado, foto) VALUES (:nombre,:especialidad,:disponibilidad,:numero,:correo,:estado,:foto)", nombre=nombre, especialidad=especialidad, disponibilidad=disponibilidad, numero=numero, correo=correo, estado=estado, foto=foto)

        flash("DOCTOR REGISTRADO!!!")
        return redirect("/admin")

    return render_template("admin.html")


#Busqueda
@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    if request.method == 'GET':
        
        doctores = db.execute("SELECT * FROM doctores WHERE especialidad LIKE ?", "%" + request.args.get('buscador') + "%")
        print(doctores)
        return render_template("especialidades.html", doctores=doctores)
    else:
        return render_template("especialidades.html")







@app.route("/adminedit", methods=["GET", "POST"])
@login_required
def adminedit():
    if request.method == "POST":
        print("Metodo POST")
        nombre = request.form.get('nombre')
        especialidad = request.form.get('especialidad')
        disponibilidad = request.form.get('disponibilidad')
        numero = request.form.get('numero')
        correo = request.form.get('correo')
        estado = request.form.get('estado')
        doctor_id = request.form.get('iddoc')

        # if not nombre:
        #     flash("Rellena el campo 'Nombre'")
        #     return render_template('adminedit.html')
        # if not correo:
        #     flash("Rellena el campo 'Correo'")
        #     return render_template('adminedit.html')
        # if not estado:
        #     flash("Rellena el campo 'Estado'")
        #     return render_template('adminedit.html')
        # if not disponibilidad:
        #     flash("Rellena el campo 'Disponibilidad'")
        #     return render_template('adminedit.html')
        # if not numero:
        #     flash("Rellena el campo 'Numero'")
        #     return render_template('adminedit.html')
        # if not especialidad:
        #     flash("Rellena el campo 'Especialidad'")
        #     return render_template('adminedit.html')
        # if not estado:
        #     flash("Rellena el campo 'Estado'")
        #     return render_template('adminedit.html')

        print(f"Este es el id del doc: {doctor_id}")


        db.execute("""UPDATE doctores SET especialidad = :especialidad, disponibilidad = :disponibilidad, número = :numero, correo = :correo, estado = :estado WHERE doctor_id = :doctor_id""",
            especialidad=especialidad,
            disponibilidad=disponibilidad,
            numero=numero,
            correo=correo,
            estado=estado,
            doctor_id=doctor_id)

        flash("DOCTOR ACTUALIZADO!!!")
        return redirect("/admin")
    consulta= db.execute("SELECT * FROM doctores")
    return render_template("adminedit.html", consulta=consulta)


