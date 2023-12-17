from django import template

register = template.Library()

@register.filter
def join_with(value, args):
    return args.join(str(v) for v in value)