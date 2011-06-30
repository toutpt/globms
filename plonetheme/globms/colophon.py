from zope import component
from zope import interface
from zope import schema

from plone.app.layout.viewlets import common
from plone.app.registry.browser import controlpanel
from plone.registry import interfaces

class IColophon(interface.Interface):
    """Colophon is configurable"""
    
    col1 = schema.List(title=u"Column 1",
                       value_type=schema.TextLine(title=u"URL"),
                       required=False)
    col2 = schema.List(title=u"Column 2",
                       value_type=schema.TextLine(title=u"URL"),
                       required=False)
    col3 = schema.List(title=u"Column 3",
                       value_type=schema.TextLine(title=u"URL"),
                       required=False)
    col4 = schema.List(title=u"Column 4",
                       value_type=schema.TextLine(title=u"URL"),
                       required=False)

class ColophonControlPanel(controlpanel.RegistryEditForm):
    """Control panel form"""

    schema = IColophon
    label = u"Colophon links"
    description = u"You can manage colophon links here"
    def updateWidgets(self):
        super(ColophonControlPanel, self).updateWidgets()
        for i in range(4):
            self.widgets['col%s'%(i+1)].rows = 8

class ColophonControlPanelView(controlpanel.ControlPanelFormWrapper):
    """Control panel form view"""
    form = ColophonControlPanel

class Colophon(common.ViewletBase):
    """Colophon rendering controller"""
    
    def columns(self):
        columns = []
        registry = component.getUtility(interfaces.IRegistry)
        colophon = registry.forInterface(IColophon, check=False)

        if not colophon:
            return []

        for i in range(4):
            column = getattr(colophon,'col%s'%(i+1))
            if column:
                columns.append(column)

        return columns

