from django import template

register = template.Library()

@register.filter
def url_name_first_part(value, delimiter="_"):
    """
    Returns the first part of a URL path before the first delimiter.
    """
    return value.split(delimiter)[0] if value else ""
