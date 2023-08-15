from django.contrib import admin
from django.contrib.admin.models import LogEntry, DELETION
from .models import Category, Post, Comment, Tag, Contact
from django_summernote.admin import SummernoteModelAdmin





# Register your modelse.

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['action_time', 'user', 'content_type', 'object_id', 'action_flag']
    list_filter = ['action_flag', 'user', 'content_type']
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request):
        return False

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_editable = ('slug',)
    list_filter = ('name',)
    search_fields = ('name__startswith',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_editable = ('slug',)
    list_filter = ('name',)
    search_fields = ('name__startswith',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('senderName', 'senderEmail', 'subject', 'created_at')
    list_filter = ('senderName', 'senderEmail', 'subject')
    search_fields = ('senderName__startswith', 'senderEmail__startswith', 'subject__startswith')


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'category', 'is_published', 'created_on', 'published_on', 'last_edited')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category', 'author')
    search_fields = ('title__startswith', 'author__first_name__startswith', 'author__last_name__startswith', 'category__name__startswith')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('author', 'category')

    def author_full_name(self, obj):
        return f'{obj.author.first_name} {obj.author.last_name}'
    author_full_name.short_description = 'Author'

    def total_comments(self, obj):
        return obj.comments_list.count()
    total_comments.short_description = 'Total Comments'


    def comments_list(self, obj):
        return obj.comments.filter(is_displayed=True)
    comments_list.short_description = 'Comments List'


    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)


class PostAdmin():
    summernote_fields = ('content',)





