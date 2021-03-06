from zope import component

from plone.app.layout.viewlets import common

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.navigation.interfaces import INavigationRoot

class SlideshowViewlet(common.ViewletBase):
    """Viewlet for slideshow on many pages"""

    def is_home(self):
        if self.context.portal_type == 'Plone Site':return False
        return INavigationRoot.providedBy(self.context)

    def bandeau(self):
        portal_state = component.getMultiAdapter((self.context, self.request),
                                         name=u'plone_portal_state')
        context_state = component.getMultiAdapter((self.context, self.request),
                                         name=u'plone_context_state')
        context = self.context

        if context_state.is_default_page():
            context = context_state.parent()

        #special case for intranet extranet:
        path = self.context.getPhysicalPath()

        if 'bandeau.png' in context.objectIds() or 'intranet' in path or 'extranet' in path:
            return {'src':context.absolute_url()+'/bandeau.png',
                    'alt':context.Title()}

    def slides(self):
        portal_state = component.getMultiAdapter((self.context, self.request),
                                         name=u'plone_portal_state')
        sections = self.context.objectIds()
        catalog = self.context.portal_catalog
        brains = catalog(portal_type="Image",
                         getId="bandeau-home.png",
                         Language=portal_state.language())
        slides = []
        for brain in brains:
            if brain.exclude_from_nav:
                continue
            image = brain.getObject()
            parent = image.aq_parent
            slides.append({'src':brain.getURL(),
                           'url':parent.absolute_url(),
                           'title':parent.Title(),
                           'description':parent.Description()})
        return slides

    def home_news(self):
        catalog = self.context.portal_catalog
        query = {'portal_type':'News Item',
                 'sort_on':'effective',
                 'sort_order':'reverse',
                 'limit':1,
                 'Language':'en'}
        brains = catalog(**query)
        if brains:
            news = brains[0]
            news_ob = news.getObject()
            info = {'title':news.Title,
                    'description':news.Description,
                    'image':news.getURL()+'/image_mini',
                    'url':news.getURL()}
            if not news_ob.getImage():
                info['image']=False
            return info
