from django.db import models
from wagtail.admin.panels import FieldPanel, PublishingPanel
from wagtail.fields import RichTextField
from wagtail.models import DraftStateMixin, PreviewableMixin, RevisionMixin, TranslatableMixin
from wagtail.snippets.models import register_snippet


@register_snippet
class FooterContent(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    TranslatableMixin,
    models.Model,
):
    copyright_text = RichTextField()
    github_url = models.URLField(blank=True, null=True)

    panels = [
        FieldPanel("copyright_text"),
        FieldPanel("github_url"),
        PublishingPanel(),
    ]

    def __str__(self):
        return "Footer content"

    def get_preview_template(self, request, mode_name):
        return "core/common/main_layout.html"

    def get_preview_context(self, request, mode_name):
        return {
            "footer_content": self,
        }

    class Meta(TranslatableMixin.Meta):
        verbose_name_plural = "Footer Content"
