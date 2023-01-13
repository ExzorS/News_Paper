from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author = models.IntegerField(default=0)

    # def update_rating(self):
    #     без понятия как это сделать


class Category(models.Model):
    name_category = models.CharField(max_length=50, unique=True)


article = 'AR'
news = 'NE'

POST_TYPE = [
    (article, 'Статья'),
    (news, 'Новость')
]


class Post(models.Model):
    author_post = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=2, choices=POST_TYPE)
    time_in_post = models.DateTimeField(auto_now_add=True)
    category_post = models.ManyToManyField(Category, through='PostCategory')
    post_header = models.CharField(max_length=50, choices=POST_TYPE, default='Incredible Post!')
    post_text = models.TextField(choices=POST_TYPE)
    rating_post = models.IntegerField(default=0, choices=POST_TYPE)

    def like(self):
        self.rating_post + 1
        self.save()

    def dislike(self):
        self.rating_post - 1
        self.save()

    def preview(self):
        return self.post_text()[0, 124] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    time_in_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)

    def like(self):
        self.rating_comment + 1
        self.save()

    def dislike(self):
        self.rating_comment - 1
        self.save()





