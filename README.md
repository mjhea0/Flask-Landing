# Flask-Landing

Boilerplate project template for a simple landing page to collect prelaunch emails. Powered by Flask, of course. <3

## QuickStart

### Install

1. Clone
1. Create and activate a virtualenv
1. Install the dependencies

### Config

Rename *app/config_sample.py* as *app/config.py* and then update.

#### Set Environment Variables

```sh
$ export APP_SETTINGS="app.config.DevelopmentConfig"
```

or

```sh
$ export APP_SETTINGS="app.config.ProductionConfig"
```

#### Create DB

```sh
$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py create_admin
$ python manage.py create_data
```

#### Run

```sh
$ python manage.py runserver
```

#### Testing

Without coverage:

```sh
$ python manage.py test
```

With coverage:

```sh
$ python manage.py cov
```
