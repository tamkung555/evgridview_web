import os
from django.contrib.gis.utils import LayerMapping
from .models import Transformer_C2

transformerpba_mapping = {
    'tag': 'TAG',
    'subtypecod': 'SUBTYPECOD',
    'op_volt': 'OP_VOLT',
    'facilityid': 'FACILITYID',
    'phasedesig': 'PHASEDESIG',
    'ratekva': 'RATEKVA',
    'circuitcou': 'CIRCUITCOU',
    'configurat': 'CONFIGURAT',
    'owner': 'OWNER',
    'presenttap': 'PRESENTTAP',
    'customerty': 'CUSTOMERTY',
    'loadstatus': 'LOADSTATUS',
    'phasea_kva': 'PHASEA_KVA',
    'phaseb_kva': 'PHASEB_KVA',
    'phasec_kva': 'PHASEC_KVA',
    'capnum': 'CAPNUM',
    'totalkvar': 'TOTALKVAR',
    'lanum': 'LANUM',
    'constructi': 'CONSTRUCTI',
    'location': 'LOCATION',
    'angle': 'ANGLE',
    'labeltext': 'LABELTEXT',
    'transforme': 'TRANSFORME',
    'installati': 'INSTALLATI',
    'creationus': 'CREATIONUS',
    'datecreate': 'DATECREATE',
    'lastuser': 'LASTUSER',
    'datemodifi': 'DATEMODIFI',
    'feederid': 'FEEDERID',
    'feederid2': 'FEEDERID2',
    'feederinfo': 'FEEDERINFO',
    'electrictr': 'ELECTRICTR',
    'enabled': 'ENABLED',
    'wbs': 'WBS',
    'existingkw': 'EXISTINGKW',
    'existingkv': 'EXISTINGKV',
    'existing_1': 'EXISTING_1',
    'workreques': 'WORKREQUES',
    'designid': 'DESIGNID',
    'worklocati': 'WORKLOCATI',
    'workflowst': 'WORKFLOWST',
    'workfuncti': 'WORKFUNCTI',
    'designtext': 'DESIGNTEXT',
    'graphicdes': 'GRAPHICDES',
    'numberofus': 'NUMBEROFUS',
    'attachment': 'ATTACHMENT',
    'matrefno': 'MATREFNO',
    'lat': 'Lat',
    'long': 'Long',
    'geom': 'MULTIPOINT',
}

transformer_c2_mapping = {
    'fid_1': 'FID_1',
    'objectid': 'OBJECTID',
    'tag': 'TAG',
    'subtypecod': 'SUBTYPECOD',
    'op_volt': 'OP_VOLT',
    'facilityid': 'FACILITYID',
    'phasedesig': 'PHASEDESIG',
    'ratekva': 'RATEKVA',
    'circuitcou': 'CIRCUITCOU',
    'configurat': 'CONFIGURAT',
    'owner': 'OWNER',
    'presenttap': 'PRESENTTAP',
    'customerty': 'CUSTOMERTY',
    'loadstatus': 'LOADSTATUS',
    'phasea_kva': 'PHASEA_KVA',
    'phaseb_kva': 'PHASEB_KVA',
    'phasec_kva': 'PHASEC_KVA',
    'capnum': 'CAPNUM',
    'totalkvar': 'TOTALKVAR',
    'lanum': 'LANUM',
    'constructi': 'CONSTRUCTI',
    'location': 'LOCATION',
    'angle': 'ANGLE',
    'labeltext': 'LABELTEXT',
    'transforme': 'TRANSFORME',
    'installati': 'INSTALLATI',
    'creationus': 'CREATIONUS',
    'datecreate': 'DATECREATE',
    'lastuser': 'LASTUSER',
    'datemodifi': 'DATEMODIFI',
    'feederid': 'FEEDERID',
    'feederid2': 'FEEDERID2',
    'feederinfo': 'FEEDERINFO',
    'electrictr': 'ELECTRICTR',
    'enabled': 'ENABLED',
    'wbs': 'WBS',
    'existingkw': 'EXISTINGKW',
    'existingkv': 'EXISTINGKV',
    'existing_1': 'EXISTING_1',
    'workreques': 'WORKREQUES',
    'designid': 'DESIGNID',
    'worklocati': 'WORKLOCATI',
    'workflowst': 'WORKFLOWST',
    'workfuncti': 'WORKFUNCTI',
    'designtext': 'DESIGNTEXT',
    'graphicdes': 'GRAPHICDES',
    'numberofus': 'NUMBEROFUS',
    'attachment': 'ATTACHMENT',
    'matrefno': 'MATREFNO',
    'globalid': 'GLOBALID',
    'opvoltint': 'OPVOLTINT',
    'objectid_1': 'OBJECTID_1',
    'name': 'NAME',
    'code': 'CODE',
    'creation_1': 'CREATION_1',
    'datecrea_1': 'DATECREA_1',
    'lastuser_1': 'LASTUSER_1',
    'datemodi_1': 'DATEMODI_1',
    'workrequ_1': 'WORKREQU_1',
    'designid_1': 'DESIGNID_1',
    'workloca_1': 'WORKLOCA_1',
    'workflow_1': 'WORKFLOW_1',
    'workfunc_1': 'WORKFUNC_1',
    'area_code': 'AREA_CODE',
    'shape_leng': 'SHAPE_Leng',
    'shape_area': 'SHAPE_Area',
    'lat': 'Lat',
    'long': 'Long',
    'geom': 'MULTIPOINT',
}

c2_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data','DS_Transformer_C2_Pro.shp'))
# print(c2_shp)

def run(verbose=True):
    
    lm = LayerMapping(Transformer_C2, c2_shp, transformer_c2_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)