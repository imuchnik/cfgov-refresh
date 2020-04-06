# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-05 15:19
from django.db import migrations, models
from wagtail.core import blocks as core_blocks
from wagtail.core import fields as core_fields
from wagtail.images import blocks as images_blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('language', models.CharField(choices=[('en', 'English'), ('es', 'Spanish')], max_length=2, primary_key=True, serialize=False)),
                ('submenus', core_fields.StreamField((('submenu', core_blocks.StructBlock((('title', core_blocks.CharBlock()), ('overview_page', core_blocks.PageChooserBlock(required=False)), ('featured_links', core_blocks.ListBlock(core_blocks.StructBlock((('page', core_blocks.PageChooserBlock(required=False)), ('text', core_blocks.CharBlock(required=False)), ('url', core_blocks.CharBlock(required=False)), ('body', core_blocks.CharBlock()), ('image', images_blocks.ImageChooserBlock()))), default=[])), ('other_links', core_blocks.ListBlock(core_blocks.StructBlock((('page', core_blocks.PageChooserBlock(required=False)), ('text', core_blocks.CharBlock(required=False)), ('url', core_blocks.CharBlock(required=False)), ('icon', core_blocks.CharBlock()))), default=[])), ('columns', core_blocks.ListBlock(core_blocks.StructBlock((('heading', core_blocks.CharBlock(required=False)), ('links', core_blocks.ListBlock(core_blocks.StructBlock((('page', core_blocks.PageChooserBlock(required=False)), ('text', core_blocks.CharBlock(required=False)), ('url', core_blocks.CharBlock(required=False)))), default=[])))), default=[]))))),))),
            ],
            options={
                'ordering': ('language',),
            },
        ),
    ]
