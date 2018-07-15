from django import template

register = template.Library()

# You can also register those functions using decorators
# since I am passing a function in what is a function call
@register.filter(name='cutMe')
def cutMe(value, arg):
    """
        This cuts all of values of "arg" from the string!
    """
    return value.replace(arg,'')

#register.filter('cutMe', # Aliasing the functiont cutMe as "cutMe"
#                 cutMe)   # The function itselft that I want to pass
