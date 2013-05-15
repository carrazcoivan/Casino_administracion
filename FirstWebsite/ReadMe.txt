/**
  * Django online tutorial
  *With Django you don't put your code in the PHP's equivalent to /var/www because it risks being visible by others over the web
  * Put it in some directory outside of the document root, such as /home/mycode.
  *
  * Remember that everytime you beging a new Django project you need to invoke the following setup
  *		-- django-admin.py startproject projectName
  *
  * you get the following structure:
  *	projectName/   					// container for the project
  *		manage.py				// command line utility which interacts with the current django proyect.
  *		pollsFolder				// folder representing a python-app
  *		projectName/				// actual python package for your project. This is the package name used to import anything inside it ( e.g. import projectName.settings )
  *			__init__.py			// empty file that tells python that this dir should be considered a python package
  *			settings.py			// configuration for this django project
  *			urls.py				// table of contents for your site.
  *			wsgi.py				// entry-point for wsgi-compatible webservers to server your project
  * 
  * 
  * from Outer project folder run "manage.py runserver".... which runs the server
  * If you prefer, to change the server's IP, pass along with the port.  To listen on all public IPs ( useful to show off your work on other computers ), use:
  *		-- mange.py runserver 0.0.0.0:8000
  *		-- python.exe manage.py runserver 0.0.0.0:8000 // don't forget
  *
  * Settings.py can be used to configure the keys in teh DB's default item to match your DB connection settings.
  * 	-- ENGINE: django.db.backends.sqlite3|mysql|oracle
  * 	-- NAME; name of DB.  If using sqlite3 you need to specify the absolute path.
  *		-- USER: DB username ( not used in SQLite )
  *		-- PASSWORD: DB pass ( not used in SQLite )
  *		-- HOST: host where DB is on, it could be 127.0.0.1 ... SQLite DB will be created automatically, if using another DBMS it needs to be setup and running now
  * 	-- Set TIME_ZONE
  * 	-- INSTALLED_APPS: holds names for all Django apps activated in this Django instance.  Apps can be packaged and distributed for use in other projects.
  * 
  * Each of the apps use at least 1 DB table, so the tables need to be created.  To do that, run:
  *		-- manage.py syncdb 		// looks at Installed_apps and crates necessary DB tables according to the settings.
  *
  * At this point the project is ready..
  *
  * 
  * CREATING MODELS
  * Every Django isntance consists of a Python package. We can create other Python apps next to manage.py so that they can be imported as its own top level module rather than a submodule of projectName.
  * Poll package will define the models -- in other words the DB layout and additional metadata.
  * MODEL: definitive source of data about your data.  It contains the essential fields and behaviors of the data you're storing.
  *
  * With Models, Django is able to create DB tables for this app and creates a python DB access API for accessing the model objects.  The Field types used within each model you create is used as a DB-type, CharField => VARCHAR, 
  *		Field types: https://docs.djangoproject.com/en/dev/ref/models/fields/#field-types
  *		The variables used within the model are used as column names
  *		Model fields help the server decide what type of HTML-widget will used to display those values, VARCHAR => <input type="text"... />
  *		
  * FIELD options
  * Each field has a set of common args available to all field types.  All are optional.
  *		null: True,Django stores empty values as NULL in DB
  *				Default is False
  *		blank: True, allows a field to be blank, Default is False
  *		choices: choices IS an iterable list or tuple of 2-tuples used as choices for this field.  Django represents these choices as a select box instead of the standard text field and will limit choices to the choices given.
  * 		LIST_OPTIONS = ( ('OPT1', 'option 1'),...,('OPTN', 'option N') )  // this is a list of n choices  
  *				// the first element of each tuple gets stored in teh DB, the second element gets displayed in the widget
  *		
  * Given an instance of a model object, the display value for a choices field can be accessed using the method:
  *		get_variableName_display()  //aparently, Django makes sure to create a default method for each variable declared in a model.  get_variableName_display() returns the value of the variable, "variableName".  NICE
  * 
  *	OTHER FIELD OPTIONS
  * 	default: allows us to specify a default value for the field.   If given a callable object, the callable object will be called when a new object is created
  *		help_text: text displayed with the form widget.
  * 	primary_key: if True, this field is the primary key for the model
  *						by default Djago inserts a value as a primary key, which is as an auto-increment integer.
  *		unique: if True, this field must be unique throughout the table.  This is the default value that Django gives to each model: "id = models.AutoField(primary_key=True)"
  * 		EACH MODEL REQUIRES EXACTLY ONE FIELD TO HAVE A "primary_key=True".
  * 
  *	VERBOSE FIELD NAMES
  *	Django creates a verbose name for each field, by default it takes the field name and converts the underscores to spaces
  *	If given, the default string is used as a verbose representation of the field
  *		first_name=models.CharField("person's first name", max_length=30)  # verbose name: "person's first name"
  *		first_name=models.CharField(max_length=30)	# verbose name is "first name"
  * For ForeignKey, ManyToManyField and OneToOneField require the first arg to be a model class, here you can use the keyword argument, "verbose_name"
  *		poll = models.ForeignKey( Poll, verbose_name="related poll")
  *
  * RELATIONSHIPS
  * Django offers a way to define relattionship between tables:
  *		Many-to-one: you need "django.db.models.ForeignKey".    use it like any other Field type
  *			-- ForeignKey: requires a positional arg, the class to which the model is related
  *							class Car(models.Model)
  *					 			manufacturer=models.ForeignKey(Manufacturer)
  *		Many-to-many: use as a any other field
  *			-- ManyToManyField: requires a positional arg, the class to which the model is related
  *					class Pizza(models.Model)
  *						toppings = models.ManyToManyField(Topping)  # it is advisable for toppings to be plural, because there's many toppings for one/many pizzas, ??a list/tuple??
  *
  *		Django allows you to create a more detailed connection between two models, more precisely a relationship between two entities, through the keyword "through".
  *		
  *		// in this example the keyword "through" is used to represent a ManyToMany relationship between a Group and a person.
			  class Person(models.Model):
				name = models.CharField(max_length=128)

				def __unicode__(self):
					return self.name

			class Group(models.Model):
				name = models.CharField(max_length=128)
				members = models.ManyToManyField(Person, through='Membership')

				def __unicode__(self):
					return self.name

		// Membership is the "intermediary" model, it contains ONE foregin key to the target model ( Person ), and ONE foregin key to the source model (Group)
		// An exception exists when we have a ManyToMany relationship to itself, through an intermediary model.  Two foreing keys to the same model are permitted.  You must use "symmetrical=False"
			class Membership(models.Model):
				person = models.ForeignKey(Person)
				group = models.ForeignKey(Group)
				date_joined = models.DateField()
				invite_reason = models.CharField(max_length=64)
				
	//Now create ManyToMany relationships
	>> ringo = Person.objects.create(name="Ringo Starr")
	>> paul  = Person.objects.create(name="Paul McCartney")
	>> beatles=Group.objects.create(name="Beatles")
	>> memb  = Membership(person=ringo, group=beatles, date_joined=date(1962,8,16),invite_reason="Needed a drummer")
	>> memb.save()
	>> beatles.members.all()
	>> ring.group_set.all()
	>> 
  *
  *
  * META OPTIONS
  * inner class Meta can be used to provide metadata to the model class.  metadata is anything that is not a field, like "ordering", db table name, human readable singular/plural names ( verbose_name, verbose_name_plural)
  *		
  *
  * MODEL METHODS
  * Custom methods on models add "row-level" functionality to your objs.  Whereas Manager methods are intended to do "table-wide" things, models method act on a particular model instance.
  *
  * ABSTRACT BASE CLASSES
  * In order to use abstract classes you specify this piece of info in the inner Meta class of a particular model
  *			class Meta:
  *				abstract = True
  *  the abstract class is not used to create DB tables, it is uused as a base class for other models, by adding fields the child class.
  *
  *
  * MODEL VARIABLE NAMES RESTRICTIONS
  *		1. don't use python reserved words
  *		2. dont' use two consecutive underscores
  * Dont't forget to include polls in the INSTALLED_APPS tuple.
  * Now that you setup the models.py script, Python knows to include the models, so run the following:
  *		-- manage.py sql polls
  *		
  * STOPPED ON SECTION: MODELS - Meta inheritance 
  *  
  *	CHECK FOR ERRORS IN MODELS
  * 	-- manage.py validate
  *
  *	If you call syncdb it will create the missing tables from the installed apps, it may be called as many times as you need
  * 
  * LAST LESSON: WRITING FIRST DJANGO APP, PART 2 -- Enter the admin site
  *
  *
  *
  * CUSTOMIZE YOUR PROJECT'S TEMPLATES
  * Create a templates directory and create a folder "admin" within that folder.  You can put your template files here.
  * Temlates files are html files with lots of of text like {% block branding %} and {{title}}, these symbols are part of Django's template language.
  * Django automatically looks for a templates subdirectory within each app package, for use as a fallback.  Don't forget that django.contrib.admin is an app. 
  *
  * PART 3
  * url uses patterns to match the URL provided in teh url line.  IF a pattern finds a match, it will call its corresponding view.  Which is specified with the name of the view module.  e.i. views.index.
  * don't forget that every view you create, needs to be mapped to the urls.py file if you want those views to be seen
  * Every package can have its own templates folder that django looks for automatically
  * 
  * \the polls package contains a template folder and another polls folder .  This is called "template namespacing" and is used to differentiate among files.
  * Helps Django to avoid getting confused.  Now you can call the index by using the url, "polls/index.html"
  * 
  * Instead of creating the output template, there is an idiom which makes it easier, all thanks to the function "render()"
  * Look at the views.py file for an example at step 4
  * render(): takes the request, a name of a template, and a dictionary
  *		returns an HttpResponse obj of the given template rendered with the given context.
  *
  * 404 ERROR
  * You can create a default 500 or 404 error page by including a template in your views
  * Remember you will be able to see this page only if you set debug to false in the setings of your website
  * NOTE: these views must be kept in the root of your templates folder...
  *
  * 500 ERROR 500 ERROR 500 ERRO NOTE: IF you set debug to false in the settings, make sure to include the allowed hosts.  if you leave this list empty, the 500 error will appear.  You need to include at least 'localhost'.
  * DJANGO BOOK
  *		http://www.djangobook.com/en/2.0/index.html
  
  * handler400/handler500="sitename.view.nameofview"
  *
  *
  * Since views can be named in the urls.py script, you can refer to your vies by name:
  * <a href="/polls/{{ poll.id }}/">{{ poll.question }}</a>
  *	you can use a named view in the following view
  * <a href="{% url 'viewname' args %}">.....</a>
  * 
  * NAMESPACING URL NAMES - are used to help django which app-view to use.  You can specify a namespace in the ursl.py file.
  * 	-- url(r'^polls/', include('polls.urls', namespace="polls")), 
  *		
  *	 Now in the templates you can use a namespace url: 
  *		-- <a href="{% url 'polls:detail' anArgs.att %}">...</a>
  *
  *
  * USE GENERIC VIEWS: LESS CODE
  * Up until now views have been written the "hard way" o_O...  django uses generic views to which simplify things.
  * We begin with URLconf file, polls/urls.py
  *  url(r'^$, views.IndexView.as_view(), name='index'),.... etc
  *
  * New Views
  * The index, detail, and results views are removed to use generic views.
  *
  *
  *
  *
  */