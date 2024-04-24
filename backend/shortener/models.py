from hashlib import md5
from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

class URL(models.Model):
    full_url = models.URLField(unique=True)
    hashed_url = models.URLField(unique=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def clicked(self):
        self.clicks+=1
        self.save()
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.hashed_url = md5(self.full_url.encode()).hexdigest()

        validate = URLValidator()
        try:
            validate(self.full_url)
        except ValidationError as e:
            return 
    
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.full_url