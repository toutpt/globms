from zope import component
from Products.Five import BrowserView

class Intranet(BrowserView):
    """Intranet view"""
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def news(self):
        query = {'portal_type':'News Item'}
        catalog = tools.catalog()
        brains = catalog(**query)
        return {'title':brain.Title,
                'description':brain.Description,
                'url':brain.getURL()}
    
    def projects(self):
        filter = {'portal_types':['File','Folder']}
        return self.context.listFolderContents(contentFilter=filter)

    @property
    def tools(self):
        return component.getMultiAdapter((self.context, self.request),
                                         name=u'plone_tools')
