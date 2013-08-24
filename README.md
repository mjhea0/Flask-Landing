## Flask-Landing

Boilerplate project template for a simple landing page to collect prelaunch emails. Powered by Flask. <3

### Quickstart

1. Clone the repo:

        $ git clone git@github.com:mjhea0/Flask-Landing.git
        $ cd Flask-Landing
        
2. Activate a virtualenv:

        $ virtualenv --no-site-packages env
        $ source env/bin/activate
        
3. Install dependencies:

        $ pip install -r requirements.txt
        
4. Create the database:

        $ python db_create.py
        
5. Run:

        $ python run.py

### Dependencies

 - Flask==0.10.1
 - Flask-WTF==0.8.4
 - WTForms==1.0.4
 - Flask-SQLAlchemy==1.0
 - coverage==3.6
 - nose==1.3.0
 - selenium==2.35.0

### Structure

  	.
	├── README.md
	├── TODO.md
	├── app
	│   ├── __init__.py
	│   ├── module
	│   │   ├── __init__.py
	│   │   ├── forms.py
	│   │   ├── models.py
	│   │   └── views.py
	│   ├── static
	│   │   ├── css
	│   │   │   └── main.css
	│   │   ├── img
	│   │   │   ├── favicon.ico
	│   │   │   └── favicon.png
	│   │   ├── js
	│   │   │   └── main.js
	│   │   └── robots.txt
	│   └── templates
	│       ├── 404.html
	│       ├── 500.html
	│       ├── base.html
	│       ├── index.html
	│       ├── login.html
	│       └── view_signups.html
	├── config.py
	├── db_create.py
	├── requirements.txt
	├── run.py
	├── shell.py
	└── tests
	    └── landing_tests.py

### Tests

To run the tests:

    $ nosetests --with-coverage --cover-erase --cover-package=app --cover-html
