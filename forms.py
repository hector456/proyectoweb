from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import Required
from wtforms import validators


class ForLogin(Form):
	usuario = StringField("Usuario:",[
		validators.Required(message="el usuario no puede estar vacio"),
		validators.length(min =5,max =20,message="Ingrese entre 5 y 20 caracteres")
		])
	password = PasswordField("Contraseña:", [
		validators.Required(message = "la contraseña no puede estar vacia"),
		validators.length(min = 5, message = "la contraseña es muy debil, debe tener mas de  5 caracteres")
		])
	enviar = SubmitField("Enviar")

class ForRegistro(Form):
	usuario = StringField("Nuevo Usuario",[
		validators.Required(message ="El usuario no puede estar vacio"),
		validators.length(min = 5, max = 20,message = "Ingrese entre 5 y 20 caracteres")

		])
	password = PasswordField("nueva Contraseña",[
		validators.Required(message = "la contraseña no puede estar vacia"),
		validators.length(min = 5, message = "la contraseña es muy debil, debe tener mas de  5 caracteres")
		])
	password2 = PasswordField("confirme contraseña",[
		validators.Required(message = "la contraseña no puede estar vacia"),
		validators.length(min = 5, message = "la contraseña es muy debil, debe tener mas de  5 caracteres")
		])