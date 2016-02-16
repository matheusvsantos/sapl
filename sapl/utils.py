from django.apps import apps
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# SAPL business apps
#  This is a dependency order: each entry depends only on previous ones
#  The order is important for migration code
appconfs = [apps.get_app_config(n) for n in [
    'parlamentares',
    'comissoes',
    'compilacao',
    'materia',
    'norma',
    'sessao',
    'lexml',
    'protocoloadm', ]]


def register_all_models_in_admin(module_name):
    appname = module_name.split('.')[0]
    app = apps.get_app_config(appname)
    for model in app.get_models():
        class CustomModelAdmin(admin.ModelAdmin):
            list_display = [f.name for f in model._meta.fields
                            if f.name != 'id']

        if not admin.site.is_registered(model):
            admin.site.register(model, CustomModelAdmin)


def xstr(s):
    return '' if s is None else str(s)


def create_barcode_128_as_base64_png(value):
    from base64 import b64encode
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import mm, inch
    from reportlab.graphics.barcode import createBarcodeDrawing

    barcode = createBarcodeDrawing('Code128', value = value, barWidth = 170, height=50, fontSize = 2, humanReadable = True)
    data = b64encode(barcode.asString('png'))
    return data.decode('utf-8')


def make_choices(*choice_pairs):
    assert len(choice_pairs) % 2 == 0
    ipairs = iter(choice_pairs)
    choices = list(zip(ipairs, ipairs))
    yield choices
    for key, value in choices:
        yield key

YES_NO_CHOICES = [(True, _('Sim')), (False, _('Não'))]
