# Generated by Django 2.0.5 on 2019-03-10 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operations', '0004_usermessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermessage',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='usermessage',
            name='to_user',
        ),
        migrations.AddField(
            model_name='usermessage',
            name='reciever',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to=settings.AUTH_USER_MODEL, verbose_name='收消息用户'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermessage',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='发消息用户'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='message',
            field=models.TextField(default='', help_text='消息内容', verbose_name='消息内容'),
        ),
    ]