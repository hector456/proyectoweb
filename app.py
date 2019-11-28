from flask import Flask
from flask import render_template,request,session,url_for, redirect
from flask import flash

import forms, csv


app = Flask(__name__, template_folder = "vista")
app.secret_key = "my_session"




@app.route('/')
def Inicio():
	if("user" in session):
		user = session["user"]
		print(user)
	return render_template("Base.html")



@app.route('/Login', methods =["GET","POST"])
def Login():
	formulario1 = forms.ForLogin(request.form)

	if(request.method == "POST" and formulario1.validate()):
		with open("Usuarios.csv") as f:
			reader = csv.reader(f)
			for i in reader:
				if(formulario1.usuario.data == i[0] and formulario1.password.data == i[1]):
					session['user'] = formulario1.usuario.data
					return render_template("Ingresado.html")
			flash("Usuario o contraseña incorrecta")
			return redirect(url_for("Login"))
	#session['user'] = formulario1.usuario.data si paso la validacion crea una nueva sesion
	return render_template("Login.html", formulario = formulario1 )







@app.route('/Registrar', methods =["GET" ,"POST"])
def Registrar():
	formulario2 = forms.ForRegistro(request.form)
	if(request.method == "POST" and formulario2.validate()):
		if(formulario2.password.data == formulario2.password2.data):
			with open('Usuarios.csv', 'a+', newline='') as archivo:
				archivo_csv = csv.writer(archivo,delimiter = ",")
				registro = [formulario2.usuario.data, formulario2.password.data]
				archivo_csv.writerow(registro)
				flash("Usuario creado correctamente")
				return redirect(url_for("Login"))
		else:	
			flash('Las passwords no son iguales')
			return redirect(url_for('Registrar'))
	return render_template("Registrar.html", formulario = formulario2)

@app.route('/salir', methods =["GET"])
def salir():
	if("user" in session):
		session.pop("user")
		return render_template("salir.html")
	return redirect(url_for("Inicio"))

@app.route('/Clientes', methods=["GET"])
def Clientes():
	with open("clientes.csv") as f:
		reader = csv.reader(f)
		lista = []
		for i in reader:
			lista.append(i)
	return render_template("/Clientes.html", list = lista)

@app.route('/Acerca')
def Acerca():
	return render_template('/Acerca.html')

@app.errorhandler(404)
def no_encontrado(e):
    return render_template('404.html')

@app.errorhandler(500)
def no_encontrado(e):
    return render_template('500.html')


app.run(port = 3000, debug = True)