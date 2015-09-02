# views.py

from django.views.generic import TemplateView

from pln.mixins import FilterContextMixin, PLNToolsContextMixin


class IndexView(FilterContextMixin, PLNToolsContextMixin, TemplateView):
    ''' -- landing page for CLT-PLN '''

    template_name = "index.html"

