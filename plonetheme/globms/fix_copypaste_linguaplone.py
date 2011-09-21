from zope import component
from zope.globalrequest import getRequest

def dontdothis(ob, event):
    """http://stackoverflow.com/q/7491100/622081"""
    raise Exception('dont do this')
