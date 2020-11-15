from django import template

# register = template.library()
#
# '''
# Using Decorators to create custom & register custom filters
# '''
# @register.filter(name='cut')
# def cut(value,arg):
#     """
#     This custom filter cuts out all values of 'arg' from the string value.
#     """
#     return value.replace(arg,'')


#Custom filter
# def cut(value,arg):
#     """
#     This custom filter cuts out all values of 'arg' from the string value.
#     """
#     return value.replace(arg,'')

# '''
# Register the filter in order to call it
# string  = name of filter
# function= the function calls the filter
# '''
# register.filter('cut',cut)
