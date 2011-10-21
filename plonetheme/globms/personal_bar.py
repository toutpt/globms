from plone.app.layout.viewlets import common

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class PersonalBarViewlet(common.PersonalBarViewlet):
    index = ViewPageTemplateFile('personal_bar.pt')
    
    def extranet_url(self):
        portal_url = self.portal_state.portal_url()
        return portal_url + '/en/extranet'

    def intranet_url(self):
        portal_url = self.portal_state.portal_url()
        return portal_url + '/en/intranet'

    def logout_url(self):
        portal_url = self.portal_state.portal_url()
        language = self.portal_state.language()
        return '%s/%s/logout'%(portal_url, language)

    def isloggedin(self):
        return not self.portal_state.anonymous()
