from django import template

register = template.Library()

# @register.filter(name='addclass')
# def addclass(value, arg):
#     return value.as_widget(attrs={'class': arg})


# @register.filter(name='addplaceholder')
# def addplaceholder(value, arg):
#     return value.as_widget(attrs={'placeholder': arg})

def addclass(value, token):
    value.field.widget.attrs["class"] = token
    return value

def addplaceholder(value, token):
    value.field.widget.attrs["placeholder"] = token
    return value


register.filter(addplaceholder)
register.filter(addclass)