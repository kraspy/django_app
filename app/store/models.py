from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'A', 'Activated'
        INACTIVE = 'I', 'Inactivated'

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100)
    description = models.TextField(blank=True, default='')
    price = models.DecimalField(decimal_places=2, max_digits=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=1,
        choices=Status.choices,
        default=Status.INACTIVE,
    )
    category = models.ForeignKey(
        'Category',
        null=True,
        on_delete=models.SET_NULL,
        related_name='products',
    )

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(
                fields=['name'],
            )
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __repr__(self) -> str:
        return f'{super().__class__.__name__}(name={self.name!r})'


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30)
    description = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['pk']

    def __repr__(self) -> str:
        return f'{super().__class__.__name__}(name={self.name!r})'
