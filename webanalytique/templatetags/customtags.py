from django import template

register = template.Library()


@register.filter
def get_label(dictionary, key):
    return dictionary[key]['label']


@register.filter
def get_item(dictionary, key):
    return dictionary[key]
