from zope import component

from plone.app.layout.viewlets import common

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class SlideshowViewletRoot(common.ViewletBase):
    def slides(self):
        sections = self.context.objectIds()
        catalog = self.context.portal_catalog
        brains = catalog(portal_type="Image", getId="bandeau.png")
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

#        slides = []
#        slideshow = getattr(self.context,'slideshow',None)
#        if slideshow is None:
#            return []
#        slide_ids = slideshow.objectIds()
#        for slide_id in slide_ids:
#            slide = getattr(slideshow,slide_id)
#            slide_url = slide.absolute_url()
#            slides.append({'src':slide_url+'/image_thumb','url':slide_url,
#                           'title':slide.Title(),
#                           'description':slide.Description()})
#        return slides

    def block(self):
        block = getattr(self.context,'home-slide-block')
        return {'title':block.Title(),
                'description':block.Description(),
                'img':self.context.absolute_url()+'/home-slide-block.jpg'}

class SlideshowViewlet(common.ViewletBase):
    """Viewlet for slideshow on many pages"""

    def bandeau(self):
        portal_state = component.getMultiAdapter((self.context, self.request),
                                         name=u'plone_portal_state')
        context_state = component.getMultiAdapter((self.context, self.request),
                                         name=u'plone_context_state')
        context = self.context
        if context_state.is_default_page():
            context = context_state.parent()
        if 'bandeau.png' in context.objectIds():
            return {'src':context.absolute_url()+'/bandeau.png',
                    'alt':context.Title()}
