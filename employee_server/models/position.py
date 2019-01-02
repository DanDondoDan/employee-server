from django.db import models


class Position(models.Model):

    position = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(
            self.position,
            )

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'
