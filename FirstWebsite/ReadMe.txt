1. abre una ventana CMD
2. navega hasta la raiz de el proyecto, el mismo donde esta el archivo "manage.py"
3. corre el siguiente comando, "python.exe manage.py runserver 0.0.0.0:8000"
4. navega a "http://localhost:8000/admin/"
	username: icf     #curiosamente, el username es case-sensitive, asi que asegurate que sea minusculas
	pass:     venom
5. En el "site administration" tu vas a ver links a grupos y usuarios.  Por lo menos que los usuarios son los que pueden administrar el servicio.
6. Tu puedes agregar y eliminar usuarios si te vas a usuarios.
7. Polls, es un paquete, ( similar a package en Java ), el cual es el que yo hice como ejemplo.
	Polls ( encuestas ), es un proyecto el cual define el model para la base de datos.  Cualquier movimiento que tu hagas en Polls, agregar o eliminar, se haran los cambios en la base de datos.  Intentalo.
	En la seccion de Polls, escoge, "Add"
	Crea una encuesta, "Pregunta y fecha". Segun como este modelada la "encuesta" en la base de datos es como se van la forma a el usuario.  Por ejemplo, si tienes un varchar en la base de datos, entonces Django mostrar un tag deh HTML de tipo <input...>. 
8.	Aun hay mas, pero no he continuado...  ESta chido no?