# administration page
----
Django administration page provides you admin crud for students (In this case for USCO students), that can be used in your django projects.

This package officially supports all currently supported versions of Python/Django:

|      Python   | 2.7 | 3.3 | 3.4 | 3.5 | 3.6 |
| :------------ | --- | --- | --- | --- | --- |
| Django 1.7    |  :x:  |  :x:  |  :x:  | :x: | :x: |
| Django 1.8    |  :white_check_mark:  |  :white_check_mark:  |  :white_check_mark:  |  :white_check_mark:  | :large_blue_circle: |
| Django 1.9    |  :white_check_mark:  | :x: |  :white_check_mark:  |  :white_check_mark:  | :large_blue_circle: |
| Django 1.10   |  :white_check_mark:  | :x: |  :white_check_mark:  |  :white_check_mark:  | :large_blue_circle: |
| Django 1.11   |  :white_check_mark:  | :x: | :white_check_mark:   | :white_check_mark:   | :white_check_mark:  |
| Django 2.0    |  :x:                 | :x: | :white_check_mark:   | :white_check_mark:   | :white_check_mark:  |
| Django [master](https://github.com/django/django/archive/master.tar.gz) | :x: | :x: | :x: | :x: | :x: |

| Key |                                                                     |
| :-: | :------------------------------------------------------------------ |
| :white_check_mark: | Officially supported, tested, and passing                           |
| :large_blue_circle: | Tested and passing, but not officially supported                    |
| :white_square_button: | Not officially supported, may break at any time, most tests passing |
| :x: | Known incompatibilities                                             |

Authored by [Duvan Mejia](https://stackoverflow.com/users/9872532/duvan-sgf?tab=profile).

----

* [Requirements](#requirements)
* [Installation](#installation)
* [Configuration](#configuration)
  * [Migration Configuration](#migration-configuration)
    * [Swappable Models](#swappable-models)
    * [Alternative Name Types](#alternative-name-types)
    * [Continent Data](#continent-data)
  * [Run Migrations](#run-migrations)
  * [Import Configuration](#import-configuration)
    * [Download Directory](#download-directory)
    * [Download Files](#download-files)
    * [Currency Data](#currency-data)
    * [Countries That No Longer Exist](#countries-that-no-longer-exist)
    * [Postal Code Validation](#postal-code-validation)
    * [Custom `slugify()` function](#custom-slugify-function)
    * [Cities Without Regions](#cities-without-regions)
    * [Languages/Locales To Import](#languageslocales-to-import)
    * [Limit Imported Postal Codes](#limit-imported-postal-codes)
    * [Plugins](#plugins)
  * [Import Data](#import-data)
* [Writing Plugins](#writing-plugins)
* [Examples](#examples)
* [Third Party Apps/Extensions](#third-party-apps--extensions)
* [TODO](#todo)
* [Notes](#notes)
* [Running Tests](#running-tests)
* [Release Notes](#release-notes)

----

## Requirements

cymysql==0.9.4
Django==1.11.5
django-cymysql==2.0.0
django-datatable==0.3.1
django-filter==1.1.0
django-model-utils==3.1.1
virtualenv==15.1.0

That's is all.

## Installation

Clone this repository into your project:

```bash
git clone https://github.com/DuvanSGF/Django-with-Admin-LTE.git
```

Download the zip file and unpack it:

```bash
wget https://github.com/DuvanSGF/Django-with-Admin-LTE/master.zip
unzip master.zip
```

Install with pip:

```bash
pip install ""Requirements""
```

## Configuration

You'll need to see the documentation If you not understand something. See that [documentation](https://docs.djangoproject.com/en/1.11/) for guidance.

You'll need to add `estudiantes` to `INSTALLED_APPS` in your projects `settings.py` file:

```python
INSTALLED_APPS = (
    # ...
    'estudiantes',
    # ...
)
```

### Migration Configuration

These settings should be reviewed and set or modified BEFORE any migrations have been run.


### Run Migrations

After you have configured all migration settings, run

```bash
python manage.py migrate estudiantes
```

to create the required database tables and add the continent data to its table.


### Import Configuration

These settings should also be reviewed and set or modified before importing any data.



## Notes

If you is here! Congrats only two steps more and it's ready!

I'm finding some bugs and I will fix.


## Running Tests

1. Install postgres, MySQL (In my case I have installed XAMPP).
2. Create `usco` database.
3. Run the following command :
        $ python manage.py migrate

        and then:
        $ python manage.py makemigrations estudiantes

        then:
        $ python manage.py createsuperuser
        Username: admin

        You will then be prompted for your desired email address:
        Email address: admin@example.com

4. Run tests:

        $ python manage.py runserver

        Now, open a Web browser and go to “/admin/” on your local domain – e.g., http://127.0.0.1:8000/site/. You should see the admin’s login screen:

 <img src="https://raw.githubusercontent.com/RamEduard/admin-lte-express/master/public/readme/login.png" width="300">

## Release Notes

### 0.4.1

Use Django's native migrations

#### Upgrading from 0.4.1

Upgrading from 0.4.1 is likely to cause problems trying to apply a migration when the tables already exist. In this case a fake migration needs to be applied:

```bash
python manage.py migrate cities 0001 --fake
```

### 0.4

** **This release of django-cities is not backwards compatible with previous versions** **

The country model has some new fields:
 - elevation
 - area
 - currency
 - currency_name
 - languages
 - neighbours
 - capital
 - phone

Alternative name support has been completely overhauled. The code and usage should now be much simpler. See the updated examples below.

The code field no longer contains the parent code. Eg. the code for California, US is now "CA". In the previous release it was "US.CA".

These changes mean that upgrading from a previous version isn't simple. All of the place IDs are the same though, so if you do want to upgrade it should be possible.



















This project is created for Crud with estudents

Instalacion


kratos@gmail.com
username:kratos
#duvan12345


admin
12345

Administrador
crack12345
