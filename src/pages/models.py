from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    subheading = RichTextField(blank=True)
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock()),
        ('person', blocks.StructBlock([
            ('first_name', blocks.CharBlock()),
            ('surname', blocks.CharBlock()),
            ('photo', ImageChooserBlock(required=False)),
            ('biography', blocks.RichTextBlock()),
        ])),
    ], use_json_field=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('subheading'),
        FieldPanel('body'),
    ]
