from django.contrib import admin
from .models import Event, Gallery, VideoGallery, Comment, Paragraph, ListItem, ContactMessage, Announcement, AnnouncementImage

# Inline для фотографий
class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 1
    verbose_name = "Фотография"
    verbose_name_plural = "Фотографии"

# Inline для видеороликов
class VideoGalleryInline(admin.TabularInline):
    model = VideoGallery
    extra = 1
    verbose_name = "Видеоролик"
    verbose_name_plural = "Видеоролики"

# Админка для комментариев с функцией одобрения
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'event', 'approved', 'created_date')
    list_filter = ('approved', 'created_date')
    search_fields = ('author', 'text')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, f'Вы одобрили {queryset.count()} комментариев.')

    approve_comments.short_description = 'Одобрить выбранные комментарии'

# Inline для абзацев текста
class ParagraphInline(admin.StackedInline):
    model = Paragraph
    extra = 1
    verbose_name = "Абзац"
    verbose_name_plural = "Абзацы"

# Inline для элементов списка
class ListItemInline(admin.TabularInline):
    model = ListItem
    extra = 1
    verbose_name = "Элемент списка"
    verbose_name_plural = "Элементы списка"

# Inline для изображений объявлений
class AnnouncementImageInline(admin.TabularInline):
    model = AnnouncementImage
    extra = 1
    verbose_name = "Изображение объявления"
    verbose_name_plural = "Изображения объявлений"

# Админка для мероприятий с фотографиями, видео, абзацами и элементами списка
class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ('title', 'event_date', 'is_past_event')
    search_fields = ('title', 'event_date')
    ordering = ('-event_date',)
    inlines = [ListItemInline, GalleryInline, VideoGalleryInline, ParagraphInline]

# Админка для сообщений обратной связи
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'message']

# Админка для объявлений с изображениями
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    inlines = [AnnouncementImageInline]

# Регистрация моделей в админке
admin.site.register(Event, EventAdmin)
admin.site.register(Comment, CommentAdmin)
