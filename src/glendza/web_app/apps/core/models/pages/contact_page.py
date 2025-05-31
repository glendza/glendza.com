from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.fields import RichTextField
from wagtailcaptcha.models import WagtailCaptchaEmailForm


class ContactEmailFormField(AbstractFormField):
    page = ParentalKey(
        "core.ContactPage",
        on_delete=models.CASCADE,
        related_name="form_fields",
    )


class ContactPage(WagtailCaptchaEmailForm):
    template = "core/contact/contact_page.html"
    landing_page_template = "core/contact/contact_page_landing.html"

    max_count = 1
    subpage_types = []
    parent_page_types = ["core.HomePage"]

    intro = RichTextField(
        blank=True,
        null=True,
        help_text="Text to display at the top of the contact page.",
    )
    thank_you_text = RichTextField(
        blank=True,
        null=True,
        help_text="Text displayed on the page after the form has been submitted successfully.",
    )

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel("intro"),
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address"),
                        FieldPanel("to_address"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            heading="Email Settings",
        ),
    ]

    class Meta:
        verbose_name = "contact page"
        verbose_name_plural = "contact pages"
