from zope import component
from zope import interface
from zope import schema

from Products.Five import BrowserView
from Acquisition import aq_parent, aq_inner

class Job(BrowserView):
    """A job is a document you can apply to"""
    
    def application_form(self):
        """Return URL of the application form"""
        parent = self.context_state.parent()
        return parent.absolute_url()+'/application-form?job='+self.context.getId()

    @property
    def context_state(self):
        return component.getMultiAdapter((self.context,self.request),
                                                  name="plone_context_state")
        
class JobsVocabulary(BrowserView):
    """vocab to list every jobs"""

    def __call__(self):
        field = aq_inner(self.context)
        form = aq_parent(field)
        container = aq_parent(form)
        filter = {'portal_type':'Document'}
        jobs = container.listFolderContents(contentFilter=filter)
        return [(job.getId(), job.Title()) for job in jobs]
