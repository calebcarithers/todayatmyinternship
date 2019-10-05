# Generated by Django 2.2.5 on 2019-10-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tamiAPP', '0004_usersub_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersub',
            name='num_vote_down',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='usersub',
            name='num_vote_up',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='usersub',
            name='vote_score',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
