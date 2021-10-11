from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 작성자는 나중에

# 포스트에 제목이 나오게
    def __str__(self) :
        return f'[{self.pk}]{self.title}'