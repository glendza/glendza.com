from django.db import models
from wagtail.admin.panels import FieldPanel, ObjectList, TabbedInterface
from wagtail.blocks import RichTextBlock
from wagtail.fields import StreamField
from wagtail.models import Page
from wagtail.search import index


class BlogPage(Page):
    template = "core/blog/blog_page.html"

    summary = models.CharField(
        max_length=500,
        null=True,
        blank=True,
    )
    content = StreamField(
        block_types=[
            ("richtext", RichTextBlock()),
        ],
        null=True,
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("summary"),
        FieldPanel("content"),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Content"),
            ObjectList(Page.promote_panels, heading="Promote"),
        ]
    )

    parent_page_types = ["core.BlogIndexPage"]
    subpage_types = []

    search_fields = Page.search_fields + [
        index.SearchField("summary"),
        index.SearchField("content"),
    ]

    class Meta:
        verbose_name = "blog entry page"
        verbose_name_plural = "blog entry pages"
