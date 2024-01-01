# Generated by Django 4.1.5 on 2023-06-17 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bug_type', models.CharField(choices=[('bug1', 'UI Bug'), ('bug2', 'Functional Bug'), ('bug3', 'Performance Bug'), ('bug4', 'Compatibility Bug'), ('bug5', 'Security Bug'), ('bug6', 'Data Bug'), ('bug7', 'Integration Bug'), ('bug8', 'Usability Bug'), ('bug9', 'Accessibility Bug')], max_length=10)),
            ],
        ),
    ]