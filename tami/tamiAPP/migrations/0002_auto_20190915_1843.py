# Generated by Django 2.2.5 on 2019-09-15 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tamiAPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersub',
            name='rank',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='usersub',
            name='description',
            field=models.TextField(default='anon'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usersub',
            name='where',
            field=models.CharField(blank=True, default='anon', max_length=100, null=True),
        ),
    ]