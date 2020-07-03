# Generated by Django 3.0.7 on 2020-07-01 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('is_hidden', models.BooleanField(default=False, help_text='Due to system requirements a database entry cannot be deleted. Hidden represents deleted for the users.', verbose_name='hidden')),
                ('name', models.CharField(max_length=100, verbose_name='group name')),
                ('slug_name', models.SlugField(max_length=20, unique=True)),
                ('about', models.CharField(max_length=255, verbose_name='group description')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='groups/pictures')),
                ('verified', models.BooleanField(default=False, help_text='Verified groups are also known as official communities.', verbose_name='verified group')),
                ('members_limit', models.PositiveIntegerField(default=10, help_text='This will be the limit on the number of members.')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('is_hidden', models.BooleanField(default=False, help_text='Due to system requirements a database entry cannot be deleted. Hidden represents deleted for the users.', verbose_name='hidden')),
                ('is_admin', models.BooleanField(default=False, help_text="Group admins can update the group's data and manage its members.", verbose_name='group admin')),
                ('used_invitations', models.PositiveSmallIntegerField(default=0)),
                ('remaining_invitations', models.PositiveSmallIntegerField(default=0)),
                ('habits', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True, help_text='Only active users are allowed to interact in the groups.', verbose_name='active status')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='groups.Group')),
                ('invited_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invited_by', to=settings.AUTH_USER_MODEL)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Profile')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('is_hidden', models.BooleanField(default=False, help_text='Due to system requirements a database entry cannot be deleted. Hidden represents deleted for the users.', verbose_name='hidden')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('used', models.BooleanField(default=False)),
                ('used_at', models.DateTimeField(blank=True, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='groups.Group')),
                ('issued_by', models.ForeignKey(help_text='Habit group member that is providing the invitation', on_delete=django.db.models.deletion.CASCADE, related_name='issued_by', to=settings.AUTH_USER_MODEL)),
                ('used_by', models.ForeignKey(help_text='User that used the code to enter the group', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='groups.Membership', to=settings.AUTH_USER_MODEL),
        ),
    ]