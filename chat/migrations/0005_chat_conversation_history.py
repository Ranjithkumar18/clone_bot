# Generated manually for adding conversation_history field

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='conversation_history',
            field=models.JSONField(blank=True, default=list, help_text='Stores complete conversation history as JSON array'),
        ),
    ]

