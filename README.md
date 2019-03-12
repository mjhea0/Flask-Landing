# Flask-Landing

Boilerplate project template for a simple landing page to collect prelaunch emails. Powered by Flask, of course. <3

## QuickStart

### Config

Rename *config_sample.py* as *config.py* and then update.

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

#### Migrating DB
Use the following after adding a columns to the models in models.py. This will create the needed columns in your database.
```sh
$ python manage.py db migrate
$ python manage.py db upgrade
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
