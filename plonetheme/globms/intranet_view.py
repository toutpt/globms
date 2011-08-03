from zope import component
from Products.Five import BrowserView

class Intranet(BrowserView):
    """Intranet view"""
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def news(self):
        news = []
        query = {'portal_type':'News Item', 'sort_order':'Effective',
                 'sort_limit':2}
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
        path = '/'.join(self.context.getPhysicalPath())
        query = {'portal_type':'File', 'sort_on':'Date','sort_order':'reverse',
                 'path':{'query': path},'sort_limit':5}
        catalog = self.tools.catalog()
        brains = catalog(**query)
        files = []
        for brain in brains:
            files.append({'title':brain.Title,
                'description':brain.Description,
                'url':brain.getURL(),
                'icon':brain.getIcon})

        return files

    @property
    def tools(self):
        return component.getMultiAdapter((self.context, self.request),
                                         name=u'plone_tools')
