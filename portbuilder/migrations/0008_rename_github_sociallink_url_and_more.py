# Generated by Django 4.2.13 on 2024-05-20 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portbuilder', '0007_rename_url_sociallink_github_sociallink_linkedin_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sociallink',
            old_name='github',
            new_name='url',
        ),
        migrations.RemoveField(
            model_name='sociallink',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='sociallink',
            name='twitter',
        ),
        migrations.AddField(
            model_name='sociallink',
            name='platform',
            field=models.CharField(choices=[('LinkedIn', 'LinkedIn'), ('GitHub', 'GitHub'), ('Twitter', 'Twitter')], default='exit', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sociallink',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
