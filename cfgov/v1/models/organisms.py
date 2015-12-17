from wagtail.wagtailcore import blocks
from wagtail.wagtailsnippets.blocks import SnippetChooserBlock

from . import atoms
from . import molecules
from .snippets import Contact as ContactSnippetClass


class Well(blocks.StructBlock):
    content = blocks.RichTextBlock(required=True, label='Well')

    class Meta:
        icon = 'title'
        template = '_includes/organisms/well.html'


class FullWidthText(blocks.StreamBlock):
    content = blocks.RichTextBlock(icon='edit')
    quote = molecules.Quote()
    cta = molecules.CallToAction()
    related_links = molecules.RelatedLinks()

    class Meta:
        icon = 'edit'
        template = '_includes/organisms/full-width-text.html'


class ImageText5050Group(blocks.StructBlock):
    heading = blocks.CharBlock(icon='title')
    image_texts = blocks.ListBlock(molecules.ImageText5050())

    class Meta:
        icon = 'image'
        template = '_includes/organisms/image-text-50-50-group.html'


class ImageText2575Group(blocks.StructBlock):
    heading = blocks.CharBlock(icon='title')
    image_texts = blocks.ListBlock(molecules.ImageText2575())

    class Meta:
        icon = 'image'
        template = '_includes/organisms/image-text-25-75-group.html'


class HalfWidthLinkBlobGroup(blocks.StructBlock):
    link_blobs = blocks.ListBlock(molecules.HalfWidthLinkBlob())

    class Meta:
        icon = 'link'
        template = '_includes/organisms/half-width-link-blob-group.html'


class PostPreview(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=100, required=True)
    body = blocks.RichTextBlock(required=True)
    image = atoms.ImageBasic(required=False)

    post = blocks.PageChooserBlock(required=True)

    link = atoms.Hyperlink(required=False)

    class Meta:
        icon = 'view'
        template = '_includes/organisms/post-preview.html'


class EmailSignUp(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=100, required=True)
    text = blocks.CharBlock(required=True)
    gd_code = blocks.CharBlock(required=False)

    form_field = blocks.ListBlock(molecules.FormFieldWithButton(), icon='mail', required=False)

    class Meta:
        icon = 'mail'
        template = '_includes/organisms/email-signup.html'


class RelatedPosts(blocks.StructBlock):
    limit = blocks.CharBlock(default='3', label='Limit')
    show_heading = blocks.BooleanBlock(required=False, default=True,
                                       label='Show Heading and Icon?',
                                       help_text='This toggles the heading and'
                                       + ' icon for the related types.')
    relate_posts = blocks.BooleanBlock(required=False, default=True,
                                       label='Blog Posts', editable=False)
    relate_newsroom = blocks.BooleanBlock(required=False, default=True,
                                          label='Newsroom', editable=False)
    relate_events = blocks.BooleanBlock(required=False, default=True,
                                        label='Events')
    view_more = atoms.Hyperlink(required=False)

    class Meta:
        icon = 'link'
        template = '_includes/molecules/related-posts.html'


class MainContactInfo(blocks.StructBlock):
    header = blocks.CharBlock()
    body = blocks.RichTextBlock()
    contact = SnippetChooserBlock(ContactSnippetClass)

    class Meta:
        icon = 'wagtail'
        template = '_includes/organisms/main-contact-info.html'


class Table(blocks.StructBlock):
    headers = blocks.ListBlock(blocks.CharBlock(max_length=20))
    rows = blocks.ListBlock(blocks.StreamBlock([
        ('hyperlink', atoms.Hyperlink(required=False)),
        ('text', blocks.CharBlock(max_length=20)),
        ('text_blob', blocks.TextBlock()),
        ('rich_text_blob', blocks.RichTextBlock()),
    ]))

    class Meta:
        icon = 'form'
        template = '_includes/organisms/table.html'
        label = 'Table'
