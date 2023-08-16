# Generated by Django 4.2.3 on 2023-07-31 21:02

from django.db import migrations

categories = {
    0: {'name':'General', 'descr':'General category'},
    1: {'name':'Home', 'descr':'Home related'},
    2: {'name':'Work', 'descr':'Work'},
    3: {'name':'Family', 'descr':''},
    4: {'name':'Friends', 'descr':''},
    5: {'name':'Hobby', 'descr':''},
    # 4: {'name':'', 'descr':''},
}

def populate_categories(apps, schema_editor, data=categories):
    Cat = apps.get_model('memo', 'Category')
    for k,v in data.items():
        cat = Cat.objects.create(name=v['name'], description=v['descr'])

class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_categories),
    ]
