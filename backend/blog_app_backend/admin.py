from django.contrib import admin
from .models import Category, Post, Comment, Tag



# Register your modelse.

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


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
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





