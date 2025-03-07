from django.db import models

class Review(models.Model):
    user_id = models.IntegerField()  # ID do guia
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Nota de 1 a 5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} - {self.rating}"