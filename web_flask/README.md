### 0-hello_route.py
- Starts a Flask web application.
- It listens on 0.0.0.0, port 5000
- Routes:
	- /: display “Hello HBNB!”
- Uses strict_slashes=False in the route definition.

### 1-hbnb_route.py
- Starts a Flask web application listening on 0.0.0.0:5000
- Routes:
	- /: display “Hello HBNB!”
	- /hbnb: display “HBNB”
- Uses strict_slashes=False in the route definition.

### 2-c_route.py
- Starts a Flask web application listening on 0.0.0.0:5000
- Routes:
	- /: display "Hello HBNB!"
	- /hbnb: display “HBNB”
	- /c/<text>: display “C ” followed by the value of the text variable
	  (replace underscore _ symbols with a space
- Uses strict_slashes=False in the route definition.

### 3-python_route.py
- Starts a Flask web application listening on 0.0.0.0:5000
- Routes:
	- /: display "Hello HBNB!"
	- /hbnb: display “HBNB”
	- /c/<text>: display “C ” followed by the value of the text variable
	  (replace underscore _ symbols with a space
	- /python/<text>: display “Python ”, followed by the value of the text
	  variable (replace underscore _ symbols with a space )
		  - The default value of text is “is cool”
- Uses strict_slashes=False in the route definition.

### 4-number_route.py
- Starts a Flask web application listening on 0.0.0.0:5000
- Routes:
	- /: display "Hello HBNB!"
	- /hbnb: display “HBNB”
	- /c/<text>: display “C ” followed by the value of the text variable
	  (replace underscore _ symbols with a space
	- /python/<text>: display “Python ”, followed by the value of the text
	  variable (replace underscore _ symbols with a space )
	  	- The default value of text is “is cool”
	- /number/<n>: display “n is a number” only if n is an integer
- Uses strict_slashes=False in the route definition.

### 5-number_template.py
- Starts a Flask web application listening on 0.0.0.0:5000
- Routes:
	- /: display "Hello HBNB!"
	- /hbnb: display “HBNB”
	- /c/<text>: display “C ” followed by the value of the text variable
	  (replace underscore _ symbols with a space
	- /python/<text>: display “Python ”, followed by the value of the text
	  variable (replace underscore _ symbols with a space )
	  	- The default value of text is “is cool”
	- /number/<n>: display “n is a number” only if n is an integer
	- /number_template/<n>: display a HTML page only if n is an integer:
		- H1 tag: “Number: n” inside the tag BODY
- Uses strict_slashes=False in the route definition.

### 6-number_odd_or_even.py
- Starts a Flask web application listening on 0.0.0.0:5000
- Routes:
	- /: display "Hello HBNB!"
	- /hbnb: display “HBNB”
	- /c/<text>: display “C ” followed by the value of the text variable
	  (replace underscore _ symbols with a space
	- /python/<text>: display “Python ”, followed by the value of the text
	  variable (replace underscore _ symbols with a space )
	  	- The default value of text is “is cool”
	- /number/<n>: display “n is a number” only if n is an integer
	- /number_template/<n>: display a HTML page only if n is an integer:
		- H1 tag: “Number: n” inside the tag BODY
	- /number_odd_or_even/<n>: display a HTML page only if n is an integer:
		- H1 tag: “Number: n is even|odd” inside the tag BODY
- Uses strict_slashes=False in the route definition.
### 7-states_list.py
- Starts a Flask web application listening on 0.0.0.0:5000
- Fetches date using storage from the storage engine: from models import storage
  and storage.all(...)
- The SQLAlchemy session is removed after each request. This is done using a
  method that has the @app.teardown_appcontext in which storage.close() is
  called.
- Routes:
	- /states_list: display a HTML page: (inside the tag BODY)
		- H1 tag: “States”
		- UL tag: with the list of all State objects present in DBStorage sorted by name
		(A->Z)
		- LI tag: description of one State: <state.id>: <B><state.name></B>
- Uses strict_slashes=False in the route definition.
