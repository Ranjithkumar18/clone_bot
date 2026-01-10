from django.db import models
from django.contrib.auth.models import User
import json

class Chat(models.Model):
    chat_id = models.CharField(max_length=100)
    session_id = models.PositiveIntegerField(unique=True, help_text="Global session ID starting from 1, sequential across all users")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats')
    title = models.CharField(max_length=200)
    conversation_history = models.JSONField(default=list, blank=True, help_text="Stores complete conversation history as JSON array")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']
        unique_together = [['chat_id', 'user']]  # Ensure chat_id is unique per user, but session_id is globally unique

    def __str__(self):
        return f"Session {self.session_id}: {self.user.username} - {self.title}"
    
    @classmethod
    def get_next_session_id(cls):
        """Get the next global session ID (starting from 1, sequential across all users)"""
        last_chat = cls.objects.order_by('-session_id').first()
        if last_chat and last_chat.session_id:
            return last_chat.session_id + 1
        return 1
    
    def get_conversation_history(self):
        """Get conversation history as a list of message dicts"""
        if not self.conversation_history:
            # If empty, build from ChatMessage objects for backward compatibility
            history = []
            for msg in self.messages.all().order_by('created_at'):
                history.append({
                    'role': msg.role,
                    'content': msg.content,
                    'created_at': msg.created_at.isoformat()
                })
            return history
        return self.conversation_history
    
    def add_to_history(self, role, content):
        """Add a message to conversation history"""
        if not self.conversation_history:
            self.conversation_history = []
        
        self.conversation_history.append({
            'role': role,
            'content': content
        })
        self.save()

class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    role = models.CharField(max_length=20)  # 'user' or 'assistant'
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.chat.title} - {self.role}"

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    filename = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)
    file_size = models.BigIntegerField()  # Size in bytes
    extracted_text = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.filename}"
