from django.db import models
from cloudinary.models import CloudinaryField  
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    profile_picture = CloudinaryField('pictures/',default='http://res.cloudinary.com/dim8pysls/image/upload/v1639001486/x3mgnqmbi73lten4ewzv.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(max_length=250, blank=True)
  

    def __str__(self):
        return f'{self.user.username} Profile'
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()
    
    @classmethod
    def filter_profile_by_id(cls, id):
        profile = Profile.objects.filter(user__id = id).first()
        return profile

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()


er.name} Post'


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
