# Generated by Django 4.1.3 on 2023-01-13 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('News_Portal', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_type', models.CharField(choices=[('AR', 'Статья'), ('NE', 'Новость')], max_length=2)),
                ('time_in_post', models.DateTimeField(auto_now_add=True)),
                ('post_header', models.CharField(choices=[('AR', 'Статья'), ('NE', 'Новость')], default='Incredible Post!', max_length=50)),
                ('post_text', models.TextField(choices=[('AR', 'Статья'), ('NE', 'Новость')])),
                ('rating_post', models.IntegerField(choices=[('AR', 'Статья'), ('NE', 'Новость')], default=0)),
                ('author_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News_Portal.author')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News_Portal.category')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News_Portal.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category_post',
            field=models.ManyToManyField(through='News_Portal.PostCategory', to='News_Portal.category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('time_in_comment', models.DateTimeField(auto_now_add=True)),
                ('rating_comment', models.IntegerField(default=0)),
                ('comment_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News_Portal.post')),
                ('comment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
