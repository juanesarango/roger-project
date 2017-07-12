from django.db import models
from utils.sitters_scores import get_sitter_rank


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Review(BaseModel):
    RATING_CHIOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]
    rating = models.IntegerField(choices=RATING_CHIOICES)
    start_date = models.DateField(max_length=50)
    end_date = models.DateField(max_length=50)
    text = models.CharField(max_length=1500)
    dogs = models.ManyToManyField('Dog')
    sitter = models.ForeignKey('Sitter')
    owner = models.ForeignKey('Owner')

    def __str__(self):
        return f'<Review: Of {self.owner.name} for {self.sitter.name} in {self.start_date}'

    # override save method to update Sitter Ranking
    def save(self, *args, **kwargs):
        stays = Review.objects.filter(sitter__id=self.sitter.id).count()
        sitter = Sitter.objects.get(id=self.sitter.id)
        sitter.rating_score = (sitter.rating_score * stays +
                               self.rating) / (stays + 1)
        sitter.overall_rank = get_sitter_rank(
            stays,
            sitter.rating_score,
            sitter.sitter_score
        )
        sitter.save()
        super().save(*args, **kwargs)


class Sitter(BaseModel):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    rating_score = models.FloatField(default=0)
    sitter_score = models.FloatField(default=0)
    overall_rank = models.FloatField(default=0)

    def __str__(self):
        return f'<Sitter: {self.name}'


class Owner(BaseModel):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=100)

    def __str__(self):
        return f'<Owner: {self.name}'


class Dog(BaseModel):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey('Owner')

    def __str__(self):
        return f'<Dog: {self.name} of {self.owner.name}'
