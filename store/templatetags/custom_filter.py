from django import template

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return "$"+str(number)

from base64 import b64encode

@register.filter
def bin_2_img(_bin):
    if _bin is not None: return b64encode(_bin).decode('utf-8')

@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1

