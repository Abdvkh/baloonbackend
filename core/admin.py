from django.contrib import admin

from .models import Tyre, UserInfo, Feedback, TyresGroup

admin.site.register(TyresGroup)
admin.site.register(Tyre)
admin.site.register(UserInfo)
admin.site.register(Feedback)