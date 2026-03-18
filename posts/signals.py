from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User
from users.models import Profile
from notifications.models import Notification
from .models import Post

@receiver(m2m_changed, sender=Post.likes.through)
def like_notification(sender, instance, action, pk_set, **kwargs):
    if action == 'post_add':
        for user_id in pk_set:
            liker = User.objects.get(id=user_id)
            if liker != instance.author:
                Notification.objects.create(
                    recipient=instance.author,
                    sender=liker,
                    notification_type='like',
                    post=instance
                )

@receiver(m2m_changed, sender=Profile.following.through)
def follow_notification(sender, instance, action, pk_set, **kwargs):
    if action == 'post_add':
        for user_id in pk_set:
            followed_user = User.objects.get(id=user_id)
            Notification.objects.create(
                recipient=followed_user,
                sender=instance.user,
                notification_type='follow'
            )