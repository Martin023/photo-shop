from django.db import models
from cloudinary.models import CloudinaryField  
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver





class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=250, blank=True)
    caption = models.CharField(max_length=250, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-pk"]

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def total_likes(self):
        return self.likes.count()
    
    @classmethod
    def get_profile_posts(cls,profile):
        posts = Image.objects.filter(profile__pk= profile)
        return posts
    @classmethod
    def update_post_caption(cls,id,caption):
        update =cls.objects.filter(id=id).update(caption=caption)
        return update

    def __str__(self):
        return f'{self.user.name} Post'


class Comments(models.Model):
    comment = models.CharField(max_length=100)
    post=models.ForeignKey(Image,related_name='comments',on_delete=models.CASCADE ,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.comment} Image'
    
    def save_comment(self):
        self.save()
    
    def delete_comment(self):
        self.delete()
    
    @classmethod
    def filter_comments_by_post_id(cls, id):
        comments = Comments.objects.filter(post__id=id)
        return comments
    

    class Meta:
        ordering = ["-pk"]


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'
