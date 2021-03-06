# Generated by Django 3.0.7 on 2020-09-09 07:55

from django.db import migrations


def set_chat_id(apps, schema_editor):
    User = apps.get_model('time_chart', 'User')
    for row in User.objects.all():
        if not row.bot_chat_id:
            row.bot_chat_id = row.id
            row.save()


class Migration(migrations.Migration):

    dependencies = [
        ('time_chart', '0011_user_bot_chat_id'),
    ]

    operations = [
        migrations.RunPython(set_chat_id, reverse_code=migrations.RunPython.noop),
    ]
