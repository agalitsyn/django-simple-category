
************************
Django simple category
************************

It is a simple category system for using in another django-apps.
It's based on efficient tree implementation, called `django-treebeard <https://github.com/tabo/django-treebeard>`_.

Usage
=====

In basic setup, you can add ``Category`` in any model::

    # models.py

    from django.db import models
    from django.utils.translation import ugettext_lazy as _

    from simple_category.models import Category

    class Product(models.Model):
        category = models.ForeignKey(Category, verbose_name=_('Category'))

For your convenience we have added the templatetags.
Assignment tag ``get_category_list`` returns query set of objects, so you can iterate as you wish::

    {% load simple_category_tags %}
    {% get_category_list as categories %}
    {% for category in categories %}
    ...
    {% endfor %}

Inclusion tag ``category_list`` returns rendered categories::

    {% load simple_category_tags %}
    {% category_list %}


If you want to manipulate the output of that template tag, just override the
templates ``simple_category/templates/templatetags/category_list.html``.
