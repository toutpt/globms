from zope import component
from Products.Five import BrowserView

class Intranet(BrowserView):
    """Intranet view"""
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def news(self):
        news = []
        query = {'portal_type':'News Item'}
        catalog = self.tools.catalog()
        brains = catalog(**query)
        for brain in brains:
            news.append({'title':brain.Title,
                'description':brain.Description,
                'url':brain.getURL()})
        return news
    
    def folders(self):
        filter = {'portal_type':'Folder'}
        return self.context.listFolderContents(contentFilter=filter)

    def files(self):
        filter = {'portal_type':'File'}
        return self.context.listFolderContents(contentFilter=filter)

    @property
    def tools(self):
        return component.getMultiAdapter((self.context, self.request),
                                         name=u'plone_tools')
