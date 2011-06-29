from zope import component

from plone.app.layout.viewlets import common

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class SlideshowViewletRoot(common.ViewletBase):
    def slides(self):
        slides = []
        slideshow = getattr(self.context,'slideshow',None)
        if slideshow is None:
            return []
        slide_ids = slideshow.objectIds()
        for slide_id in slide_ids:
            slide = getattr(slideshow,slide_id)
            slide_url = slide.absolute_url()
            slides.append({'src':slide_url+'/image_thumb','url':slide_url,
                           'title':slide.Title(),
                           'description':slide.Description()})
        return slides

    def block(self):
        block = getattr(self.context,'home-slide-block')
        return {'title':block.Title(),
                'description':block.Description(),
                'img':self.context.absolute_url()+'/home-slide-block.jpg'}

class SlideshowViewlet(common.ViewletBase):
    """Viewlet for slideshow on many pages"""

    def index(self):
        portal_state = component.getMultiAdapter((self.context, self.request),
                                         name=u'plone_portal_state')
        context_state = component.getMultiAdapter((self.context, self.request),
                                         name=u'plone_context_state')
        portal = portal_state.portal()
        context = self.context.aq_base
        if context_state.is_default_page:
            context = context_state.parent()
        slide = getattr(context,'bandeau.png', None)
        if slide is None:
            return u""
        return slide.restrictedTraverse('slideshow.html')()

