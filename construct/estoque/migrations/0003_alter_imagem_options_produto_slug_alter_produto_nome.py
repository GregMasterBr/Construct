# Generated by Django 4.1 on 2022-10-04 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_alter_categoria_options_imagem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagem',
            options={'ordering': ('-produto',), 'verbose_name': 'imagem', 'verbose_name_plural': 'imagens'},
        ),
        migrations.AddField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=40, unique=True, verbose_name='produto'),
        ),
    ]
