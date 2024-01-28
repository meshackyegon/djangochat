from django.contrib import admin

from .models import Room, Message, Messages
# class RoomAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'floor', 'room_type', 'status', 'price', 'created_at', 'updated_at')
#     list_display_links = ('id', 'name')
#     list_filter = ('name', 'floor', 'room_type', 'status', 'price', 'created_at', 'updated_at')
#     search_fields = ('name', 'floor', 'room_type', 'status', 'price', 'created_at', 'updated_at')
#     list_per_page = 25

# class Meta:
#     model = Room
#     fields = '__all__'

# class MessageAdmin(admin.ModelAdmin):
#     list_display = ('id', 'room', 'name', 'email', 'phone', 'message', 'created_at')
#     list_display_links = ('id', 'room')
#     list_filter = ('room', 'name', 'email', 'phone', 'message', 'created_at')
#     search_fields = ('room', 'name', 'email', 'phone', 'message', 'created_at')
#     list_per_page = 25
# class Meta:
#     model = Room
#     fields = '__all__'
# class MessagesAdmin(admin.ModelAdmin):
#     list_display = ('id', 'room', 'name', 'email', 'phone', 'message', 'created_at')
#     list_display_links = ('id', 'room')
#     list_filter = ('room', 'name', 'email', 'phone', 'message', 'created_at')
#     search_fields = ('room', 'name', 'email', 'phone', 'message', 'created_at')
#     list_per_page = 25
# class Meta:
#     model = Room
#     fields = '__all__'


# admin.site.register(Room, RoomAdmin)
# admin.site.register(Message, MessageAdmin)
# admin.site.register(Messages, MessagesAdmin)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Messages)