# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-20 19:52
from __future__ import unicode_literals

from django.db import migrations
import v1.blocks
import v1.models.snippets
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailsnippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('ask_cfpb', '0018_migrate_answer_field_help_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerpage',
            name='sidebar',
            field=wagtail.wagtailcore.fields.StreamField([('call_to_action', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False)), (b'size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'regular', b'Regular'), (b'large', b'Large Primary')]))]))])), ('related_links', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), ('related_metadata', wagtail.wagtailcore.blocks.StructBlock([(b'slug', wagtail.wagtailcore.blocks.CharBlock(max_length=100)), (b'content', wagtail.wagtailcore.blocks.StreamBlock([(b'text', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100)), (b'blob', wagtail.wagtailcore.blocks.RichTextBlock())], icon=b'pilcrow')), (b'list', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))], icon=b'list-ul')), (b'date', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(max_length=100)), (b'date', wagtail.wagtailcore.blocks.DateBlock())], icon=b'date')), (b'topics', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(default=b'Topics', max_length=100)), (b'show_topics', wagtail.wagtailcore.blocks.BooleanBlock(default=True, required=False))], icon=b'tag'))])), (b'is_half_width', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))])), ('email_signup', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(default=b'Stay informed', required=False)), (b'default_heading', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text=b'If selected, heading will be styled as an H5 with green top rule. Deselect to style header as H3.', label=b'Default heading style', required=False)), (b'text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Write a sentence or two about what kinds of emails the user is signing up for, how frequently they will be sent, etc.', required=False)), (b'gd_code', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Code for the topic (i.e., mailing list) you want people who submit this form to subscribe to. Format: USCFPB_###', label=b'GovDelivery code', required=False)), (b'disclaimer_page', wagtail.wagtailcore.blocks.PageChooserBlock(help_text=b'Choose the page that the "See Privacy Act statement" link should go to. If in doubt, use "Generic Email Sign-Up Privacy Act Statement".', label=b'Privacy Act statement', required=False)), (b'form_field', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'btn_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'required', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'info', wagtail.wagtailcore.blocks.RichTextBlock(label=b'Disclaimer', required=False)), (b'inline_info', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Show disclaimer on same line as button. Only select this option if the disclaimer text is a few words (ie, "Privacy Act statement") rather than a full sentence.', label=b'Inline disclaimer', required=False)), (b'label', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'text', b'Text'), (b'checkbox', b'Checkbox'), (b'email', b'Email'), (b'number', b'Number'), (b'url', b'URL'), (b'radio', b'Radio')], required=False)), (b'placeholder', wagtail.wagtailcore.blocks.CharBlock(required=False))]), icon=b'mail', required=False))])), ('sidebar_contact', wagtail.wagtailcore.blocks.StructBlock([(b'contact', wagtail.wagtailsnippets.blocks.SnippetChooserBlock(b'v1.Contact')), (b'has_top_rule_line', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text=b'Add a horizontal rule line to top of contact block.', required=False))])), ('rss_feed', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'blog_feed', b'Blog Feed'), (b'newsroom_feed', b'Newsroom Feed')])), ('social_media', wagtail.wagtailcore.blocks.StructBlock([(b'is_share_view', wagtail.wagtailcore.blocks.BooleanBlock(default=True, help_text=b'If unchecked, social media icons will link users to official CFPB accounts. Do not fill in any further fields.', label=b'Desired action: share this page', required=False)), (b'blurb', wagtail.wagtailcore.blocks.CharBlock(default=b"Look what I found on the CFPB's site!", help_text=b'Sets the tweet text, email subject line, and LinkedIn post text.', required=False)), (b'twitter_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Custom text for Twitter shares. If blank, will default to value of blurb field above.', max_length=100, required=False)), (b'twitter_related', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) A comma-separated list of accounts related to the content of the shared URL. Do not enter the  @ symbol. If blank, it will default to just "cfpb".', required=False)), (b'twitter_hashtags', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) A comma-separated list of hashtags to be appended to default tweet text.', required=False)), (b'twitter_lang', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Loads text components in the specified language, if other than English. E.g., use "es"  for Spanish. See https://dev.twitter.com/web/overview/languages for a list of supported language codes.', required=False)), (b'email_title', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Custom subject for email shares. If blank, will default to value of blurb field above.', required=False)), (b'email_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Custom text for email shares. If blank, will default to "Check out this page from the CFPB".', required=False)), (b'email_signature', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Adds a custom signature line to email shares. ', required=False)), (b'linkedin_title', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Custom title for LinkedIn shares. If blank, will default to value of blurb field above.', required=False)), (b'linkedin_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'(Optional) Custom text for LinkedIn shares.', required=False))])), ('reusable_text', v1.blocks.ReusableTextChooserBlock(v1.models.snippets.ReusableText))], blank=True),
        ),
    ]
