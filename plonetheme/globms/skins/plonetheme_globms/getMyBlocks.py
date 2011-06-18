## Script (Python) "getMyBlocks"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=zone
##title=Return a list of the content types allowed here filtered by getNotAddableTypes
#

zoneob = context.blocks.get(zone)

items = zoneob.contentItems()
blocks = []
for id, item in items:
    blocks.append(item)
context.plone_log('end')

return blocks