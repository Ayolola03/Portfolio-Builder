# Generated by Django 4.2.13 on 2024-05-19 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portbuilder', '0002_alter_bio_about_me_alter_bio_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='address',
            field=models.CharField(blank=True, default='-', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='phone_number',
            field=models.CharField(blank=True, default='-', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, default='-', help_text='Description of the project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, default='-', help_text='Link to the project'),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='github',
            field=models.URLField(blank=True, default='-', null=True),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='linkedin',
            field=models.URLField(blank=True, default='-', null=True),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='twitter',
            field=models.URLField(blank=True, default='-', null=True),
        ),
    ]
