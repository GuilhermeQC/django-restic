from django.db import models


class Toys(models.Model):
    name = models.CharField(max_length=150, blank=False, default="")
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=250, blank=True, default="")
    toy_category = models.CharField(
        max_length=200, blank=False, default="Action Figure")
    release_date = models.DateTimeField()
    was_included_in_home = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ("name",)
