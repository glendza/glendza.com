from django.db import models
from wagtail.admin.panels import FieldPanel, PublishingPanel
from wagtail.models import DraftStateMixin, PreviewableMixin, RevisionMixin, TranslatableMixin
from wagtail.snippets.models import register_snippet


@register_snippet
class HeaderContent(
    DraftStateMixin,
    RevisionMixin,
    PreviewableMixin,
    TranslatableMixin,
    models.Model,
):
    logo = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )

    panels = [
        FieldPanel("logo"),
        PublishingPanel(),
    ]

    def __str__(self):
        return "Header content"

    def get_preview_template(self, request, mode_name):
        return "core/common/main_layout.html"

    def get_preview_context(self, request, mode_name):
        return {
            "footer_content": self,
        }

    class Meta(TranslatableMixin.Meta):
        verbose_name_plural = "Header Content"
