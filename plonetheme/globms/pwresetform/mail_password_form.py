from zope import interface
from zope import schema

from zope.i18nmessageid import MessageFactory
from plone.autoform.form import AutoExtensibleForm
from z3c.form import form, button

from plone.z3cform import layout
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone import PloneMessageFactory as pmf
from AccessControl import Unauthorized
from Products.CMFCore.utils import getToolByName
from Products.statusmessages.interfaces import IStatusMessage

_ = MessageFactory('passwordresettool')

class IMailPasswordForm(interface.Interface):
    """form schema"""
    userid = schema.ASCIILine(title=_("label_my_user_name_is",default=u"My user name is"))

class MailPasswordForm(AutoExtensibleForm, form.Form):
    schema = IMailPasswordForm
    label = _(u"heading_lost_password",
              default = u"Lost Password")
    ignoreContext = True

    @button.buttonAndHandler(u'Reset Password')
    def handleApply(self, action):
        data, errors = self.extractData()
        # do something
        request = self.request
        registration = getToolByName(self.context, 'portal_registration')
        plone_utils = getToolByName(self.context, 'plone_utils')
        try:
            response = registration.mailPassword(data['userid'],request)
            self.request.response.redirect('mail_password_response')
        except ValueError, e:
            IStatusMessage(self.request).add(e, 'error')
            self.request.response.redirect('@@mail_password_form')

class MailPasswordView(layout.FormWrapper):
    form = MailPasswordForm

    index = ViewPageTemplateFile('mail_password_form.pt')
