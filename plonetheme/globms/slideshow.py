from zope import component

from plone.app.layout.viewlets import common

class SlideshowViewlet(common.ViewletBase):
    """Viewlet for slideshow on many pages"""
    
    def index(self):
        portal_state = component.getMultiAdapter((self.context, self.request),
                                         name=u'plone_portal_state')
        context_state = component.getMultiAdapter((self.context, self.request),
                                         name=u'plone_context_state')
        portal = portal_state.portal()
        context = self.context.aq_base
        if context_state.is_portal_root():
            self.context.plone_log('we are on root')
            if 'blocks' not in portal.objectIds():
                self.context.plone_log('no blocks folder')
                return u""
            slide = portal.blocks.home_slideshow
        else:
            self.context.plone_log('we are not on root')
            if context_state.is_default_page:
                context = context_state.parent()
            if 'globalms_slideshow' not in context.objectIds():
                self.context.plone_log('no globalms_slideshow item')
                return u""
            slide = context.globalms_slideshow
        
        return slide.restrictedTraverse('slideshow.html')()
