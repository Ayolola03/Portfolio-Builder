# Generated by Django 4.2.13 on 2024-05-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portbuilder', '0003_alter_contactinfo_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
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
