from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=128)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=128)
    e_mail = models.EmailField(max_length=128)
    birthday = models.DateField()
    gender = models.CharField(max_length=10)
    bio = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=f'images/%Y/%m/%d/')

    def __str__(self):
        return self.full_name


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateField()
    info = models.TextField(blank=True)

    def __str__(self):
        return str(self.id)


class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/%Y/%m/%d/')

    def __str__(self):
        return str(self.id)


class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    tag_name = models.CharField(max_length=128)

    def __str__(self):
        return str(self.id)


class PostTag(models.Model):
    id = models.IntegerField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)