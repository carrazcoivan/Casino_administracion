1. abre la ventana shell de comandos, cmd
2. navega a el proyecto de python
3. navega a ../FirstWebsite  este sera el ROOT
4. ejecuta el siguiente comando
		python.exe manage.py runserver 0.0.0.0:8000
		
	Si esto funciona mirabas un mensaje similar a este
	" Quit the server with CTRL-BREAK"
	Lo cual significa que tu servidro ya esta corriendo
5. en tu navegador verte a "http://localhost:8000/admin/"
6. entra con la clave y el password
		username: venom
		password: venom
7. ya adentro, estas en la parte de administracion, puedes agregar usuarios.  Este proyecto tiene control sobre una base de datos de encuentas.  Esto es parte del proyecto que se llama "poll" ahi esta en la pagina de administarcion
8.  Tu puedes ingresar a Poll y agregar o eliminar tus preguntas de encuesta. Estos cambios se reflejan en la base de datos.
9. esta chido, no?