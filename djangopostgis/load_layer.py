
from django.contrib.gis.utils import LayerMapping
from .models import country,Indstates,India,Indblocks
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

india_mapping = {
    'id_0': 'ID_0',
    'iso': 'ISO',
    'name_0': 'NAME_0',
    'objectid_1': 'OBJECTID_1',
    'iso3': 'ISO3',
    'name_engli': 'NAME_ENGLI',
    'name_iso': 'NAME_ISO',
    'name_fao': 'NAME_FAO',
    'name_local': 'NAME_LOCAL',
    # 'name_obsol': 'NAME_OBSOL',
    'name_varia': 'NAME_VARIA',
    # 'name_nonla': 'NAME_NONLA',
    'name_frenc': 'NAME_FRENC',
    'name_spani': 'NAME_SPANI',
    'name_russi': 'NAME_RUSSI',
    'name_arabi': 'NAME_ARABI',
    'name_chine': 'NAME_CHINE',
    # 'waspartof': 'WASPARTOF',
    # 'contains': 'CONTAINS',
    'sovereign': 'SOVEREIGN',
    'iso2': 'ISO2',
    # 'www': 'WWW',
    'fips': 'FIPS',
    'ison': 'ISON',
    'validfr': 'VALIDFR',
    'validto': 'VALIDTO',
    'pop2000': 'POP2000',
    'sqkm': 'SQKM',
    'popsqkm': 'POPSQKM',
    'unregion1': 'UNREGION1',
    'unregion2': 'UNREGION2',
    'developing': 'DEVELOPING',
    'cis': 'CIS',
    'transition': 'Transition',
    'oecd': 'OECD',
    'wbregion': 'WBREGION',
    'wbincome': 'WBINCOME',
    'wbdebt': 'WBDEBT',
    # 'wbother': 'WBOTHER',
    'ceeac': 'CEEAC',
    'cemac': 'CEMAC',
    'ceplg': 'CEPLG',
    'comesa': 'COMESA',
    'eac': 'EAC',
    'ecowas': 'ECOWAS',
    'igad': 'IGAD',
    'ioc': 'IOC',
    'mru': 'MRU',
    'sacu': 'SACU',
    'uemoa': 'UEMOA',
    'uma': 'UMA',
    'palop': 'PALOP',
    'parta': 'PARTA',
    'cacm': 'CACM',
    'eurasec': 'EurAsEC',
    'agadir': 'Agadir',
    'saarc': 'SAARC',
    'asean': 'ASEAN',
    'nafta': 'NAFTA',
    'gcc': 'GCC',
    'csn': 'CSN',
    'caricom': 'CARICOM',
    'eu': 'EU',
    'can': 'CAN',
    'acp': 'ACP',
    'landlocked': 'Landlocked',
    'aosis': 'AOSIS',
    'sids': 'SIDS',
    'islands': 'Islands',
    'ldc': 'LDC',
    'geom': 'MULTIPOLYGON',
}
india_shp = Path(__file__).resolve().parent / 'data' / 'IND_adm0.shp'
def run(verbose=True):
    lm = LayerMapping(India, india_shp, india_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

indblocks_mapping = {
    'id_0': 'ID_0',
    'iso': 'ISO',
    'name_0': 'NAME_0',
    'id_1': 'ID_1',
    'name_1': 'NAME_1',
    'id_2': 'ID_2',
    'name_2': 'NAME_2',
    'id_3': 'ID_3',
    'name_3': 'NAME_3',
    'type_3': 'TYPE_3',
    'engtype_3': 'ENGTYPE_3',
    # 'nl_name_3': 'NL_NAME_3',
    # 'varname_3': 'VARNAME_3',
    'geom': 'MULTIPOLYGON',
}
indblocks_shp = Path(__file__).resolve().parent / 'data' / 'IND_adm3.shp'
def run(verbose=True):
    lm = LayerMapping(Indblocks, indblocks_shp, indblocks_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
