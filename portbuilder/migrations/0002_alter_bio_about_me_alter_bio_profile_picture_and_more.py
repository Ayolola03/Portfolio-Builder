# Generated by Django 4.2.13 on 2024-05-18 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portbuilder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='about_me',
            field=models.TextField(blank=True, help_text='A brief description about yourself'),
        ),
        migrations.AlterField(
            model_name='bio',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='email',
            field=models.EmailField(help_text='Primary email address', max_length=254),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='cvs/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, help_text='Description of the project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, help_text='Link to the project'),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]