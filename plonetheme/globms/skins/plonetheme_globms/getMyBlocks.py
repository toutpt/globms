## Script (Python) "getMyBlocks"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=zone
##title=Return a list of the content types allowed here filtered by getNotAddableTypes
#

if zone not in context.blocks:
    return []
zoneob = context.blocks.get(zone)

items = zoneob.contentItems()
blocks = []
for id, item in items:
    blocks.append(item)

return blocks