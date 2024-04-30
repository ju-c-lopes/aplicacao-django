from django import template

register = template.Library()

@register.filter
def split_word(word, divisor):
    return word.split(divisor)
