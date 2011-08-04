from plone.app.layout.viewlets import common

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class PersonalBarViewlet(common.PersonalBarViewlet):
    index = ViewPageTemplateFile('personal_bar.pt')