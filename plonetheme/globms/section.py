from zope import component
from zope import interface
from zope import schema

from Products.Five import BrowserView

class Section(BrowserView):
    """view for section"""

    def icon(self):
        """Return icon url to use. None if no icon"""
        return self.context.absolute_url()+'/icon.png'

    def image(self):
        """return image structure to use or None if no image"""
        return self.context.absolute_url()+'/section.png'

    def title(self):
        return self.context.Title()

    @property
    def site_url(self):
        return self.portal_state.portal_url()

    @property
    def portal_state(self):
        return component.getMultiAdapter((self.context,self.request),
                                                  name="plone_portal_state")
    
    def section_id(self):
        return 'section-' + self.context.getId()
