from Products.Five import BrowserView

ICON = 'icon.png'

class HomePage(BrowserView):
    """home page of the globms website"""
    blocks_ids={'project-management':{'en':'our-services/project-management',
                                      'fr':'nos-services/gestion-de-projet',
                                      'de':''},
                'process-auditing':{'en':'our-services/process-auditing',
                                 'fr':'nos-services/audition',
                                 'de':''},
                'technical-expertise':{'en':'our-services/technical-expertise',
                                 'fr':'expertise-technique',
                                 'de':''},
                'short-assignments':{'en':'our-services/short-assignments',
                                    'fr':'',
                                    'de':''},
                'jobs-careers':{'en':'jobs-careers',
                                'fr':'offres-emplois',
                                'de':''},
                'it-and-financial-articles':{'en':'news-and-articles/it-and-financial-articles',
                                'fr':'actualites-et-articles/articles-it-et-financier',
                                'de':''},
                'global-market-solutions-on-the-web':{'en':'global-market-solutions/on-the-web',
                                'fr':'global-market-solutions/sur-le-web',
                                'de':''}}
    color = {'project-management':'#aaa',
             'process-auditing':'#bbb',
             'technical-expertise':'#ccc',
             'short-assignments':'#ddd'}

    @property
    def lang(self):
        return 'en'

    def block(self, blockid):
        try:
            path = self.blocks_ids[blockid][self.lang]
            block = self.context.restrictedTraverse(path,None)
        except KeyError:
            self.context.plone_log('key error: %s'%blockid)
            return
        icon = getattr(block, ICON, None)
        if icon is not None:
            icon = icon.absolute_url()
        title = block.Title()
        description = block.Description()
        color = self.color.get(blockid,None)
        return {'icon':icon,'title':title,'description':description,
                'color':color,'href':block.absolute_url()}

    def site_title(self):
        return u"Global Market Solution: Financial Software Technology"

    def partners(self):
        try:
            partners = self.context.restrictedTraverse('partners')
        except KeyError:
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

        self.context.plone_log(blocks)
        return blocks
