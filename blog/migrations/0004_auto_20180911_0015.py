# Generated by Django 2.1 on 2018-09-10 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_delete_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog2',
            name='image',
            field=models.ImageField(default='SOME STRING', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blog2',
            name='texte',
            field=models.TextField(default='SOME STRING'),
        ),
        migrations.AlterField(
            model_name='blog2',
            name='titre',
            field=models.CharField(max_length=150),
        ),
    ]