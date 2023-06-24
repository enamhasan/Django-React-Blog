from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.template.defaultfilters import slugify

from .utils import unique_slug_generator

User = get_user_model()


class Category(models.Model):
    # Post Category
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    enabled = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Tag(models.Model):
    # Post Tag
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Tags'
        default_permissions = ()
        permissions = (
            ('view_tag', 'Can view tag'),
            ('add_tag', 'Can add tag'),
            ('change_tag', 'Can change tag'),
            ('delete_tag', 'Can delete tag'),
        )

    def __str__(self):
        return self.name


class Post(models.Model):
    """Model For Blog Posts"""

    title = models.CharField(max_length=100)
    content = models.TextField()
    featuredImage = models.ImageField(upload_to='post_image', blank=True, null=True)
    excerpt = models.TextField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', related_query_name='post')
    tags = models.ManyToManyField('Tag', related_name='posts', related_query_name='post')

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts', related_query_name='post')
    # tags = models.ManyToManyField('Tag', related_name='posts', related_query_name='post')
    featured = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, null=True)
    is_published = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    published_on = models.DateTimeField(null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)

    """@property
    def comment_count(self):
        #return Commnets.objects.filter(Post=self).aggregate(Sum('quantity'))['quantity__sum'] """

    @property
    def author_full_name(self):
        try:
            return f'{self.author.first_name} {self.author.last_name}'
        except:
            return "Name Not Set"

    def __str__(self):
        return self.title

    class Meta:
        indexes = [models.Index(fields=['slug'])]
        ordering = ['-published_on']


@receiver(post_save, sender=Post)
def generate_unique_slug_for_posts(sender, instance, created, *args, **kwargs):
    if created:
        instance.slug = unique_slug_generator(instance)
        instance.save()
        print('Slug Generated For The Post')


@receiver(pre_save, sender=Post)
def update_published_on(sender, instance, **kwargs):
    """Update The Date Of 'Published On' When The Post Gets Published"""

    if instance.id:
        old_value = Post.objects.get(pk=instance.id).published_on
        if not old_value:
            instance.published_on = timezone.now()
    print('Published On Updated')


class Comment(models.Model):
    """Model For The Comments In The Blog Posts"""

    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments', related_query_name='comment')
    is_displayed = models.BooleanField(default=True)
    published_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post - "{self.post.title}", Body - "{self.body}"'


class Contact(models.Model):
    """Model For The Contact Form"""

    senderName = models.CharField(max_length=100)
    senderEmail = models.EmailField()
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Name - "{self.senderName}", Email - "{self.senderEmail}"'
