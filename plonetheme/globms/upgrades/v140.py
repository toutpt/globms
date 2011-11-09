from Products.CMFCore.utils import getToolByName

def upgrade(context):
    jsregistry = getToolByName(context, 'portal_javascripts')
    jsregistry.registerScript('++theme++plonetheme.globms/js/project.js')
 
