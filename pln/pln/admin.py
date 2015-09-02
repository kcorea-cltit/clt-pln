from django.contrib import admin

from pln.models import Application, Platform, Function, Price, Support, PLNTool, Testimonial


admin.site.register(Application)
admin.site.register(Platform)
admin.site.register(Function)
admin.site.register(Price)
admin.site.register(Support)
admin.site.register(PLNTool)
admin.site.register(Testimonial)

