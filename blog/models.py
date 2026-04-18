from django.db import models

# Content Blog
class Blog(models.Model):
    name = models.TextField(verbose_name="Nombre del Blog")
    image = models.ImageField(upload_to="", blank=True, null=True, verbose_name="Imagen del Blog")
    description = models.TextField(verbose_name="Descripcion del Blog")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name, self.description, self.created_at

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"