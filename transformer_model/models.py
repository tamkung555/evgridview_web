# from django.db import models
# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class Transformer_PBA(models.Model):
    tag = models.CharField(null=True, blank=True, max_length=15)
    subtypecod = models.BigIntegerField(null=True, blank=True)
    op_volt = models.CharField(null=True, blank=True, max_length=2)
    facilityid = models.CharField(null=True, blank=True, max_length=13)
    phasedesig = models.BigIntegerField(null=True, blank=True)
    ratekva = models.FloatField(null=True, blank=True)
    circuitcou = models.IntegerField(null=True, blank=True)
    configurat = models.CharField(null=True, blank=True, max_length=2)
    owner = models.CharField(null=True, blank=True, max_length=1)
    presenttap = models.CharField(null=True, blank=True, max_length=1)
    customerty = models.CharField(null=True, blank=True, max_length=1)
    loadstatus = models.IntegerField(null=True, blank=True)
    phasea_kva = models.FloatField(null=True, blank=True)
    phaseb_kva = models.FloatField(null=True, blank=True)
    phasec_kva = models.FloatField(null=True, blank=True)
    capnum = models.IntegerField(null=True, blank=True)
    totalkvar = models.IntegerField(null=True, blank=True)
    lanum = models.IntegerField(null=True, blank=True)
    constructi = models.CharField(null=True, blank=True, max_length=1)
    location = models.CharField(null=True, blank=True, max_length=50)
    angle = models.FloatField(null=True, blank=True)
    labeltext = models.CharField(null=True, blank=True, max_length=60)
    transforme = models.IntegerField(null=True, blank=True)
    installati = models.IntegerField(null=True, blank=True)
    creationus = models.CharField(null=True, blank=True, max_length=50)
    datecreate = models.DateField(null=True, blank=True)
    lastuser = models.CharField(null=True, blank=True, max_length=50)
    datemodifi = models.DateField(null=True, blank=True)
    feederid = models.CharField(null=True, blank=True, max_length=7)
    feederid2 = models.CharField(null=True, blank=True, max_length=7)
    feederinfo = models.BigIntegerField(null=True, blank=True)
    electrictr = models.BigIntegerField(null=True, blank=True)
    enabled = models.IntegerField(null=True, blank=True)
    wbs = models.CharField(null=True, blank=True, max_length=55)
    existingkw = models.FloatField(null=True, blank=True)
    existingkv = models.FloatField(null=True, blank=True)
    existing_1 = models.FloatField(null=True, blank=True)
    workreques = models.CharField(null=True, blank=True, max_length=20)
    designid = models.CharField(null=True, blank=True, max_length=20)
    worklocati = models.CharField(null=True, blank=True, max_length=20)
    workflowst = models.BigIntegerField(null=True, blank=True)
    workfuncti = models.BigIntegerField(null=True, blank=True)
    designtext = models.CharField(null=True, blank=True, max_length=100)
    graphicdes = models.CharField(null=True, blank=True, max_length=10)
    numberofus = models.BigIntegerField(null=True, blank=True)
    attachment = models.CharField(null=True, blank=True, max_length=254)
    matrefno = models.CharField(null=True, blank=True, max_length=30)
    impact = models.CharField(null=True, blank=True, max_length=500)
    flag =  models.BooleanField(default=False)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
    geom = models.MultiPointField(srid=4326)
    
    def __str__(self):
        return self.facilityid

class Transformer_C2(models.Model):
    fid_1 = models.IntegerField(null=True, blank=True)
    objectid = models.BigIntegerField(null=True, blank=True)
    tag = models.CharField(null=True, blank=True, max_length=15)
    subtypecod = models.BigIntegerField(null=True, blank=True)
    op_volt = models.CharField(null=True, blank=True, max_length=2)
    facilityid = models.CharField(null=True, blank=True, max_length=13)
    phasedesig = models.BigIntegerField(null=True, blank=True)
    ratekva = models.FloatField(null=True, blank=True)
    circuitcou = models.IntegerField(null=True, blank=True)
    configurat = models.CharField(null=True, blank=True, max_length=2)
    owner = models.CharField(null=True, blank=True, max_length=1)
    presenttap = models.CharField(null=True, blank=True, max_length=1)
    customerty = models.CharField(null=True, blank=True, max_length=1)
    loadstatus = models.IntegerField(null=True, blank=True)
    phasea_kva = models.FloatField(null=True, blank=True)
    phaseb_kva = models.FloatField(null=True, blank=True)
    phasec_kva = models.FloatField(null=True, blank=True)
    capnum = models.IntegerField(null=True, blank=True)
    totalkvar = models.IntegerField(null=True, blank=True)
    lanum = models.IntegerField(null=True, blank=True)
    constructi = models.CharField(null=True, blank=True, max_length=1)
    location = models.CharField(null=True, blank=True, max_length=50)
    angle = models.FloatField(null=True, blank=True)
    labeltext = models.CharField(null=True, blank=True, max_length=60)
    transforme = models.IntegerField(null=True, blank=True)
    installati = models.IntegerField(null=True, blank=True)
    creationus = models.CharField(null=True, blank=True, max_length=50)
    datecreate = models.DateField(null=True, blank=True)
    lastuser = models.CharField(null=True, blank=True, max_length=50)
    datemodifi = models.DateField(null=True, blank=True)
    feederid = models.CharField(null=True, blank=True, max_length=7)
    feederid2 = models.CharField(null=True, blank=True, max_length=7)
    feederinfo = models.BigIntegerField(null=True, blank=True)
    electrictr = models.BigIntegerField(null=True, blank=True)
    enabled = models.IntegerField(null=True, blank=True)
    wbs = models.CharField(null=True, blank=True, max_length=55)
    existingkw = models.FloatField(null=True, blank=True)
    existingkv = models.FloatField(null=True, blank=True)
    existing_1 = models.FloatField(null=True, blank=True)
    workreques = models.CharField(null=True, blank=True, max_length=20)
    designid = models.CharField(null=True, blank=True, max_length=20)
    worklocati = models.CharField(null=True, blank=True, max_length=20)
    workflowst = models.BigIntegerField(null=True, blank=True)
    workfuncti = models.BigIntegerField(null=True, blank=True)
    designtext = models.CharField(null=True, blank=True, max_length=100)
    graphicdes = models.CharField(null=True, blank=True, max_length=10)
    numberofus = models.BigIntegerField(null=True, blank=True)
    attachment = models.CharField(null=True, blank=True, max_length=254)
    matrefno = models.CharField(null=True, blank=True, max_length=30)
    globalid = models.CharField(null=True, blank=True, max_length=38)
    opvoltint = models.BigIntegerField(null=True, blank=True)
    objectid_1 = models.IntegerField(null=True, blank=True)
    name = models.CharField(null=True, blank=True, max_length=45)
    code = models.CharField(null=True, blank=True, max_length=14)
    creation_1 = models.CharField(null=True, blank=True, max_length=50)
    datecrea_1 = models.DateField(null=True, blank=True)
    lastuser_1 = models.CharField(null=True, blank=True, max_length=50)
    datemodi_1 = models.DateField(null=True, blank=True)
    workrequ_1 = models.CharField(null=True, blank=True, max_length=20)
    designid_1 = models.CharField(null=True, blank=True, max_length=20)
    workloca_1 = models.CharField(null=True, blank=True, max_length=20)
    workflow_1 = models.IntegerField(null=True, blank=True)
    workfunc_1 = models.IntegerField(null=True, blank=True)
    area_code = models.CharField(null=True, blank=True, max_length=2)
    shape_leng = models.FloatField(null=True, blank=True)
    shape_area = models.FloatField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
    
    loadProfile_base = models.CharField(null=True, blank=True, max_length=800)
    loadProfile_ev = models.CharField(null=True, blank=True, max_length=800)
    impact = models.CharField(null=True, blank=True, max_length=800)
    flag =  models.BooleanField(default=False)
    numberOfCustomer = models.IntegerField(null=True, blank=True)
    geom = models.MultiPointField(srid=4326)
    
    def __str__(self):
        return self.facilityid


# Auto-generated `LayerMapping` dictionary for Transformer_C2 model
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

# Auto-generated `LayerMapping` dictionary for TransformerPBA model
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
