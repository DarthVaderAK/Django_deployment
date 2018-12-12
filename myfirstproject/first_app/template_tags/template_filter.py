from django import template

register = template.Library()

def cut(value,arg):
    """This function cuts out all the word(args) in the string value"""
    return value.replace(arg,'')

register.filter("cut",cut)
