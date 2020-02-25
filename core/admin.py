from django.contrib import admin

from .models import Tyre, UserInfo, Feedback, TyresGroup, Images

admin.site.register(TyresGroup)
admin.site.register(Tyre)
admin.site.register(Images)
admin.site.register(UserInfo)
admin.site.register(Feedback)