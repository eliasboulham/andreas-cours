# Generated by Django 4.2 on 2023-05-30 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0007_tag_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]