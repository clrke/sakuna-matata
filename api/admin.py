from django.contrib import admin
from .models import DisasterManager, Channel, Message


class DisasterManagerAdmin(admin.ModelAdmin):
    pass


class ChannelAdmin(admin.ModelAdmin):
    pass


class MessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(DisasterManager, DisasterManagerAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(Message, MessageAdmin)
