from django.contrib import admin
from .models import Message, Member


class MessageAdmin(admin.ModelAdmin):
    pass


class MemberAdmin(admin.ModelAdmin):
    pass


admin.site.register(Message, MessageAdmin)
admin.site.register(Member, MemberAdmin)
