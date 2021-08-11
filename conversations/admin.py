from conversations import models
from django.contrib import admin


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    pass
