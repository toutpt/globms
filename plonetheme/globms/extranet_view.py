from Products.Five import BrowserView

class Extranet(BrowserView):
    """Intranet view"""
    def __init__(self, context, request):
        self.context = context
        self.request = request
