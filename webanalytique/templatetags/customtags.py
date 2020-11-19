from pprint import pprint

from django import template

register = template.Library()


@register.filter
def get_label(dictionary, key):
    return dictionary[key]['label']
