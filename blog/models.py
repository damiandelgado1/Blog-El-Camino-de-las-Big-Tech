from django.db import models

# Content Blog
class Blog(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre del Blog")
    image = models.ImageField(upload_to="", blank=True, null=True, verbose_name="Imagen del Blog")
    category = models.CharField(max_length=50, verbose_name="Descripcion del Blog")
    content = models.TextField(verbose_name="Descripcion del Blog")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.category}, {self.created_at}"

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"