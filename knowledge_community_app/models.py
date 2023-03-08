from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    """Base model: everyone will have this data"""
    create: str = models.DateTimeField("Create at ", auto_now_add=True)
    modify: str = models.DateTimeField("Modify at ", auto_now=True)
    active: bool = models.BooleanField("Active? ", default=True)

    class Meta:
        abstract = True


class User(Base):
    """User data"""
    name: str = models.CharField('Name', max_length=50)
    email: str = models.EmailField('E-mail', max_length=100)
    password: str = models.CharField('Password', max_length=20)

    def __repr__(self) -> str:
        return str(self.name)


class Posts(Base):
    """Content body of site"""
    title: str = models.CharField('Title', max_length=30)
    image: str = StdImageField('Image', upload_to='images', variations={'thumb': (300, 300)})
    slug: str = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    content: str = models.CharField('Content', max_length=200)

    def __repr__(self) -> str:
        return str(self.title)


def post_pre_save(signal, instance, sender, **kwargs) -> None:
    instance.slug = slugify(instance.title)


signals.pre_save.connect(post_pre_save, sender=Posts)
