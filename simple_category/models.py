from django.db import models
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from treebeard.mp_tree import MP_Node


@python_2_unicode_compatible
class Category(MP_Node):
    parent = models.ForeignKey('self', verbose_name=_('Parent'),
                               blank=True, null=True)
    name = models.CharField(verbose_name=_('Name'), max_length=20)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True)

    date_added = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('Date added'))
    last_modified = models.DateTimeField(auto_now=True,
                                         verbose_name=_('Last modified'))

    active = models.BooleanField(verbose_name=_('Active'), default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_view', args=[self.slug])

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
