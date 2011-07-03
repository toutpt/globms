from zope import component
from zope import interface
from zope import schema

from plone.registry.interfaces import IRegistry
from plone.memoize import view
from Products.Five import BrowserView

ICON = 'icon.png'

class IHomePageSettings(interface.Interface):
    
    blocks_ids = schema.List(title=u"Blocks ids",
                             description=u"Put id|path, one per line",
                             value_type=schema.ASCIILine(title=u"Block"))

class HomePage(BrowserView):
    """home page of the globms website"""

#project-management|our-services/project-management    
#process-auditing|our-services/process-auditing
#technical-expertise|our-services/technical-expertise
#short-assignments|our-services/short-assignments
#jobs-careers|jobs-careers
#it-and-financial-articles|news-and-articles/it-and-financial-articles
#global-market-solutions-on-the-web|global-market-solutions/on-the-web

    @property
    @view.memoize_contextless
    def blocks_ids(self):
        blocks_ids = {}
        registry = component.getUtility(IRegistry)
        records = registry.forInterface(IHomePageSettings, check=False)
        for block_id in records.blocks_ids:
            id,path = block_id.split('|')
            blocks_ids[id]=path
        return blocks_ids

    @property
    def portal_state(self):
        return component.getMultiAdapter((self.context, self.request),
                                         name="plone_portal_state")

    @property
    def lang(self):
        return self.portal_state.language()

    @property
    def default_lang(self):
        return self.portal_state.default_language()

    def block(self, blockid):

        dl = self.default_lang
        l = self.lang
        try:
            path = self.blocks_ids[blockid]
            block = self.context.restrictedTraverse(path,None)
        except KeyError:
            self.context.plone_log('key error: %s'%blockid)
            return
        if block is None:
            #try to get if from default lang
            portal = self.portal_state.portal()
            try:
                block = portal.restrictedTraverse(dl+'/'+path)
            except KeyError:
                pass
            except AttributeError:
                pass
            if block is None:
                self.context.plone_log('no block: %s'%blockid)
                return

        if not l==dl:
            #Try to find translations:
            default_page = block.getDefaultPage()
            if default_page is not None:
                btrans = block[default_page].getTranslation(language=l)
            else:
                btrans = block.getTranslation(language=l)
            if btrans is not None:
                block = btrans

        icon = getattr(block, ICON, None)
        if icon is not None:
            icon = icon.absolute_url()
        title = block.Title()
        description = block.Description()
        return {'icon':icon,'title':title,'description':description,
                'href':block.absolute_url()}

    def site_title(self):
        return u"Global Market Solution: Financial Software Technology"

    def partners(self):
        try:
            partners = self.context.restrictedTraverse('partners')
        except KeyError:
            self.context.plone_log('no partners folder')
            return
        except AttributeError:
            self.context.plone_log('no partners folder')
            return
        blocks = []
        slide=[]
        index = 0
        totaux = 0
        len_partners = len(partners.objectIds())
        partners_url = partners.absolute_url()
        #Image + title + description
        for partner_id in partners.objectIds():
            image = partners[partner_id]
            block={'src':partners_url+'/'+partner_id,
                   'url':image.Description(),
                   'alt':image.Title()}
            if index%4==0:
                if slide:
                    blocks.append(slide)
                slide = []
            slide.append(block)
            index+=1
            totaux+=1
            if totaux == len_partners:
                blocks.append(slide)

        return blocks

