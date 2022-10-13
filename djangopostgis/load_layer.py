
from django.contrib.gis.utils import LayerMapping
from .models import country,Indstates
from pathlib import Path

country_mapping = {
    'id_0': 'ID_0',
    'iso': 'ISO',
    'name_0': 'NAME_0',
    'id_1': 'ID_1',
    'name_1': 'NAME_1',
    'type_1': 'TYPE_1',
    'engtype_1': 'ENGTYPE_1',
    # 'nl_name_1': 'NL_NAME_1',
    # 'varname_1': 'VARNAME_1',
    'geom': 'MULTIPOLYGON',
}

country_shp = Path(__file__).resolve().parent / 'data' / 'IND_adm1.shp'
def run(verbose=True):
    lm = LayerMapping(country, country_shp, country_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
indstates_mapping = {
    'id_0': 'ID_0',
    'iso': 'ISO',
    'name_0': 'NAME_0',
    'id_1': 'ID_1',
    'name_1': 'NAME_1',
    'id_2': 'ID_2',
    'name_2': 'NAME_2',
    'type_2': 'TYPE_2',
    'engtype_2': 'ENGTYPE_2',
    # 'nl_name_2': 'NL_NAME_2',
    # 'varname_2': 'VARNAME_2',
    'geom': 'MULTIPOLYGON',
}
indstates_shp = Path(__file__).resolve().parent / 'data' / 'IND_adm2.shp'
def run(verbose=True):
    lm = LayerMapping(Indstates, indstates_shp, indstates_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)