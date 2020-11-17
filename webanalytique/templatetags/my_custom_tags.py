from django import template

register = template.Library()


@register.simple_tag
def getitem(dict, key):
    return dict[key]
