from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.username', read_only=True)
    recipient = serializers.CharField(source='recipient.username', read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'sender', 'recipient', 'notification_type', 'is_read', 'created_at']
        read_only_fields = ['sender', 'recipient', 'notification_type', 'created_at']