from django import template

from simple_category.models import Category

register = template.Library()


@register.assignment_tag
def get_category_list():
    """
    Tag returns query set of objects
    Example:
        {% load simple_category_tags %}
        {% get_category_list as categories %}
        {% for category in categories %}
        ...
        {% endfor %}

    """
    return Category.objects.filter(active=True)


@register.inclusion_tag('templatetags/category_list.html')
def category_list():
    """
    Tag returns rendered categories
    Example:
        {% load simple_category_tags %}
        {% category_list %}
    :return:
    """
    categories = Category.objects.filter(active=True)
    return {'categories': categories}
