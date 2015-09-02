# mixins.py

from pln.models import Application, Function, Platform, Price, Support, PLNTool


class FilterContextMixin(object):
    ''' -- generates context data for filter.html '''
    
    def get_context_data(self, **kwargs):
        ''' -- makes a dictionary of tool attributes and attribute types'''
        context = super(FilterContextMixin, self).get_context_data(**kwargs)
        context['tool_attributes'] = [
            {
               'name': 'Application',
               'types': Application.objects.all(),
            },
            {
               'name': 'Function',
               'types': Function.objects.all(),
            },
            {
               'name':  'Platform',
               'types': Platform.objects.all(),
            },
            {
               'name': 'Price',
               'types': Price.objects.all(),
            },
            {
               'name': 'Support',
               'types': Support.objects.all(),
            },
        ]
        return context

class PLNToolsContextMixin(object):
    ''' -- '''
    
    def get_context_data(self, **kwargs):
        ''' -- '''
        context = super(PLNToolsContextMixin, self).get_context_data(**kwargs)
        context['tools'] = PLNTool.objects.all()
        return context
