from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class PersonBlock(blocks.StructBlock):
    first_name = blocks.CharBlock()
    surname = blocks.CharBlock()
    photo = ImageChooserBlock(required=False)
    biography = blocks.RichTextBlock()

    class Meta:
        template = "blocks/person.html"
        icon = "user"
