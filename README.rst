======================
Django bootstrap4 form
======================

.. image:: https://badge.fury.io/py/django-bootstrap4-form.png
   :alt: PyPI version
   :target: https://pypi.python.org/pypi/django-bootstrap4-form

.. image:: https://travis-ci.org/gwasser/django-bootstrap4-form.png?branch=master   
    :target: https://travis-ci.org/gwasser/django-bootstrap4-form

.. image:: https://coveralls.io/repos/gwasser/django-bootstrap-form/badge.png?branch=master  
   :target: https://coveralls.io/r/gwasser/django-bootstrap-form?branch=master
   

Twitter Bootstrap4 for Django Forms.

A simple Django template tag to work with `Bootstrap 4 <http://getbootstrap.com/>`_

Forked from the original `django-bootstrap-form` by @tzangms.

Installation
============

Install `django-bootstrap4-form` with `pip`

.. code-block:: sh

    $ pip install django-bootstrap4-form

Usage
======

Add "bootstrap4form" to your INSTALLED_APPS.

At the top of your template load in our template tags::

	{% load bootstrap4form %}

Then to render your form::

	<form role="form">
	    <legend>Form Title</legend>
	    {% csrf_token %}
	    {{ form|bootstrap4form }}
	    <div class="form-group">
	      <button type="submit" class="btn btn-primary">Submit</button>
	    </div>
	</form>

You can also set class="form-vertical" on the form element.

To use class="form-inline" on the form element, also change the "|boostrap4form" template tag to "|bootstrap4form_inline".

It is also possible to create a horizontal form. The form class and template tag are both changed, and you will also need slightly different CSS around the submit button::

	<form class="form-horizontal">
	    <legend>Form Title</legend>
	    {% csrf_token %}
	    {{ form|bootstrap4form_horizontal }}
	    <div class="form-group">
	      <div class="col-sm-10 col-sm-offset-2">
	      	<button type="submit" class="btn btn-primary">Submit</button>
	      </div>
	    </div>
	</form>

