from zope import interface
from plone.indexer import indexer

@indexer(interface.Interface)
def location(obj):
    return obj.getLocation()

