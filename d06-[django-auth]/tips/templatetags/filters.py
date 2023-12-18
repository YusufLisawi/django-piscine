from django import template

register = template.Library()

@register.filter
def add_class(field, css):
    l = str(field).split(' ')
    l.insert(1, f'class="{css}"')
    field = ' '.join(l)
    return field
    # return field.as_widget(attrs={"class":css})
    # return field.as_widget(attrs={"class":css})