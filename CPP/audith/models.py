# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models


class CaLaboratorio(models.Model):
    id = models.IntegerField(primary_key=True)
    lab_cod = models.CharField(max_length=9)
    lab_des = models.CharField(max_length=150)
    class Meta:
        db_table = u'ca_laboratorio'

class CaDiagnosticos(models.Model):
    id = models.IntegerField(primary_key=True)
    lab_cod = models.ForeignKey(CaLaboratorio, db_column='lab_cod')
    dx_1_cod = models.IntegerField()
    dx_1 = models.CharField(max_length=150)
    class Meta:
        db_table = u'ca_diagnosticos'

class CaGerentes(models.Model):
    id_gerente = models.IntegerField(primary_key=True)
    lab_cod = models.ForeignKey(CaLaboratorio, db_column='lab_cod')
    fv = models.CharField(max_length=15)
    nombre_gerente = models.CharField(max_length=300)
    class Meta:
        db_table = u'ca_gerentes'

class CaProdLab(models.Model):
    id = models.IntegerField(primary_key=True)
    lab_cod = models.ForeignKey(CaLaboratorio, db_column='lab_cod')
    principio_cod = models.IntegerField()
    principio_des = models.CharField(max_length=360)
    prod_cod = models.CharField(max_length=30)
    prod_des = models.CharField(max_length=360)
    tipo_prod = models.CharField(max_length=45)
    class Meta:
        db_table = u'ca_prod_lab'

class CaRepresentantes(models.Model):
    id_representante = models.IntegerField(unique=True)
    gerente = models.ForeignKey(CaGerentes)
    territorio = models.CharField(max_length=180)
    nombre_repre = models.CharField(max_length=450)
    class Meta:
        db_table = u'ca_representantes'

class CaZona(models.Model):
    estado_2 = models.CharField(max_length=150, blank=True)
    zona = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'ca_zona'

class Generales(models.Model):
    id_principal = models.IntegerField(primary_key=True, db_column='ID_PRINCIPAL') # Field name made lowercase.
    id_unico = models.CharField(max_length=255, db_column='ID_UNICO') # Field name made lowercase.
    folio = models.IntegerField(null=True, db_column='FOLIO', blank=True) # Field name made lowercase.
    tema = models.CharField(max_length=60, db_column='TEMA', blank=True) # Field name made lowercase.
    tema_cod = models.IntegerField(null=True, db_column='TEMA_COD', blank=True) # Field name made lowercase.
    fecha = models.DateField(primary_key=False, db_column='FECHA') # Field name made lowercase.
    medico_cod = models.CharField(max_length=60, db_column='MEDICO_COD', blank=True) # Field name made lowercase.
    medico_des = models.CharField(max_length=255, db_column='MEDICO_DES', blank=True) # Field name made lowercase.
    espe_des = models.CharField(max_length=60, db_column='ESPE_DES', blank=True) # Field name made lowercase.
    institucion = models.CharField(max_length=60, db_column='INSTITUCION', blank=True) # Field name made lowercase.
    sector = models.CharField(max_length=135, db_column='SECTOR', blank=True) # Field name made lowercase.
    hospital = models.CharField(max_length=255, db_column='HOSPITAL', blank=True) # Field name made lowercase.
    clue = models.CharField(max_length=135, db_column='CLUE', blank=True) # Field name made lowercase.
    estado = models.CharField(max_length=135, db_column='ESTADO', blank=True) # Field name made lowercase.
    zona = models.CharField(max_length=135, db_column='ZONA', blank=True) # Field name made lowercase.
    num_pacientes = models.IntegerField(null=True, db_column='NUM_PACIENTES', blank=True) # Field name made lowercase.
    usuario = models.CharField(max_length=45, db_column='USUARIO', blank=True) # Field name made lowercase.
    tipo_medico = models.CharField(max_length=150, db_column='TIPO_MEDICO', blank=True) # Field name made lowercase.
    medico_adscrito = models.CharField(max_length=255, db_column='MEDICO_ADSCRITO', blank=True) # Field name made lowercase.
    num_pacientes_biologicos = models.CharField(max_length=135, db_column='NUM_PACIENTES_BIOLOGICOS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'generales'

class Ar(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    id_general = models.ForeignKey(Generales, db_column='ID_GENERAL') # Field name made lowercase.
    n = models.IntegerField(null=True, db_column='N', blank=True) # Field name made lowercase.
    cup = models.CharField(max_length=9, db_column='CUP', blank=True) # Field name made lowercase.
    paciente = models.CharField(max_length=135, db_column='PACIENTE', blank=True) # Field name made lowercase.
    tipo_paciente = models.CharField(max_length=450, db_column='TIPO_PACIENTE', blank=True) # Field name made lowercase.
    linea_biologicos = models.CharField(max_length=135, db_column='LINEA_BIOLOGICOS', blank=True) # Field name made lowercase.
    entidad = models.CharField(max_length=600, db_column='ENTIDAD', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ar'

class Dhepatitis(models.Model):
    id_pac = models.IntegerField(primary_key=True)
    id_general = models.ForeignKey(Generales, db_column='id_general')
    num_pac = models.IntegerField()
    px_nom = models.CharField(max_length=135)
    tip_pac = models.CharField(max_length=135)
    nom_ltra = models.CharField(max_length=135)
    nom_hep = models.CharField(max_length=120)
    nom_gen = models.CharField(max_length=120)
    class Meta:
        db_table = u'dhepatitis'

class Hemato(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    id_general = models.ForeignKey(Generales, db_column='ID_GENERAL') # Field name made lowercase.
    n = models.IntegerField(null=True, db_column='N', blank=True) # Field name made lowercase.
    cup = models.CharField(max_length=9, db_column='CUP', blank=True) # Field name made lowercase.
    paciente = models.CharField(max_length=135, db_column='PACIENTE', blank=True) # Field name made lowercase.
    tipo_paciente = models.CharField(max_length=450, db_column='TIPO_PACIENTE', blank=True) # Field name made lowercase.
    tipo_de_cancer = models.CharField(max_length=135, db_column='TIPO_DE_CANCER', blank=True) # Field name made lowercase.
    tipo_histologico = models.CharField(max_length=450, db_column='TIPO_HISTOLOGICO', blank=True) # Field name made lowercase.
    subtipo_histologico = models.CharField(max_length=450, db_column='SUBTIPO_HISTOLOGICO', blank=True) # Field name made lowercase.
    variedad_histo = models.CharField(max_length=777, db_column='VARIEDAD_HISTO', blank=True) # Field name made lowercase.
    cod_enf = models.CharField(max_length=12, db_column='COD_ENF', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'hemato'

class Oncologia(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    id_general = models.ForeignKey(Generales, db_column='ID_GENERAL', related_name='onco') # Field name made lowercase.    
    n = models.IntegerField(null=True, db_column='N', blank=True) # Field name made lowercase.
    cup = models.CharField(max_length=75, db_column='CUP', blank=True) # Field name made lowercase.
    paciente = models.CharField(max_length=75, db_column='PACIENTE', blank=True) # Field name made lowercase.
    tipo_paciente = models.CharField(max_length=250, db_column='TIPO_PACIENTE', blank=True) # Field name made lowercase.
    dx_1 = models.CharField(max_length=135, db_column='DX_1', blank=True) # Field name made lowercase.
    dx_1_cod = models.CharField(max_length=30, db_column='DX_1_COD', blank=True) # Field name made lowercase.
    dx_2 = models.CharField(max_length=135, db_column='DX_2', blank=True) # Field name made lowercase.
    dx_2_cod = models.CharField(max_length=30, db_column='DX_2_COD', blank=True) # Field name made lowercase.
    tratamiento = models.CharField(max_length=75, db_column='TRATAMIENTO', blank=True) # Field name made lowercase.
    estadio = models.CharField(max_length=75, db_column='ESTADIO', blank=True) # Field name made lowercase.
    sub_etapa = models.CharField(max_length=75, db_column='SUB_ETAPA', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'oncologia'

class ProdAr(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    id_paciente_ar = models.ForeignKey(Ar, db_column='ID_PACIENTE_AR') # Field name made lowercase.
    prod_cod = models.CharField(max_length=135, db_column='PROD_COD', blank=True) # Field name made lowercase.
    prod_des = models.CharField(max_length=135, db_column='PROD_DES', blank=True) # Field name made lowercase.
    principio_cod = models.CharField(max_length=135, db_column='PRINCIPIO_COD', blank=True) # Field name made lowercase.
    principio_des = models.CharField(max_length=135, db_column='PRINCIPIO_DES', blank=True) # Field name made lowercase.
    manu_des = models.CharField(max_length=135, db_column='MANU_DES', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'prod_ar'

class ProdHemato(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    id_paciente_hemato = models.ForeignKey(Hemato, db_column='ID_PACIENTE_HEMATO') # Field name made lowercase.
    prod_cod = models.CharField(max_length=135, db_column='PROD_COD', blank=True) # Field name made lowercase.
    prod_des = models.CharField(max_length=135, db_column='PROD_DES', blank=True) # Field name made lowercase.
    principio_cod = models.CharField(max_length=135, db_column='PRINCIPIO_COD', blank=True) # Field name made lowercase.
    principio_des = models.CharField(max_length=135, db_column='PRINCIPIO_DES', blank=True) # Field name made lowercase.
    manu_des = models.CharField(max_length=135, db_column='MANU_DES', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'prod_hemato'

class ProdHepa(models.Model):
    id_pro = models.IntegerField(primary_key=True)
    id_pac = models.ForeignKey(Dhepatitis, db_column='id_pac')
    prod_cod = models.CharField(max_length=135)
    prod_des = models.CharField(max_length=135)
    principio_cod = models.CharField(max_length=135)
    principio_des = models.CharField(max_length=135)
    manu_des = models.CharField(max_length=135)
    class Meta:
        db_table = u'prod_hepa'

class ProdOnco(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    id_paciente = models.ForeignKey(Oncologia, db_column='ID_PACIENTE') # Field name made lowercase.
    prod_cod = models.CharField(max_length=255, db_column='PROD_COD', blank=True) # Field name made lowercase.
    prod_des = models.CharField(max_length=150, db_column='PROD_DES', blank=True) # Field name made lowercase.
    principio_cod = models.CharField(max_length=90, db_column='PRINCIPIO_COD', blank=True) # Field name made lowercase.
    principio_des = models.CharField(max_length=150, db_column='PRINCIPIO_DES', blank=True) # Field name made lowercase.
    manu_des = models.CharField(max_length=90, db_column='MANU_DES', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'prod_onco'

class RepreMedico(models.Model):
    id_repre_med = models.IntegerField(unique=True)
    representante = models.ForeignKey(CaRepresentantes)
    nombre_repre = models.CharField(max_length=450)
    cod_med = models.CharField(max_length=30, unique=True)
    nombre_medico = models.CharField(max_length=450)
    class Meta:
        db_table = u'repre_medico'

class OncoCasos(models.Model):
    folio = models.IntegerField(null=True, db_column='FOLIO', blank=True) # Field name made lowercase.
    id_unico = models.CharField(max_length=90, db_column='ID_UNICO', blank=True) # Field name made lowercase.
    tema = models.CharField(max_length=60, db_column='TEMA', blank=True) # Field name made lowercase.
    tema_cod = models.IntegerField(null=True, db_column='TEMA_COD', blank=True) # Field name made lowercase.
    fecha = models.DateField(null=True, db_column='FECHA', blank=True) # Field name made lowercase.
    medico_cod = models.CharField(max_length=60, db_column='MEDICO_COD', blank=True) # Field name made lowercase.
    medico_des = models.CharField(max_length=300, db_column='MEDICO_DES', blank=True) # Field name made lowercase.
    espe_des = models.CharField(max_length=60, db_column='ESPE_DES', blank=True) # Field name made lowercase.
    institucion = models.CharField(max_length=60, db_column='INSTITUCION', blank=True) # Field name made lowercase.
    sector = models.CharField(max_length=135, db_column='SECTOR', blank=True) # Field name made lowercase.
    hospital = models.CharField(max_length=765, db_column='HOSPITAL', blank=True) # Field name made lowercase.
    clue = models.CharField(max_length=135, db_column='CLUE', blank=True) # Field name made lowercase.
    estado = models.CharField(max_length=135, db_column='ESTADO', blank=True) # Field name made lowercase.
    zona = models.CharField(max_length=135, db_column='ZONA', blank=True) # Field name made lowercase.
    num_pacientes = models.IntegerField(null=True, db_column='NUM_PACIENTES', blank=True) # Field name made lowercase.
    usuario = models.CharField(max_length=45, db_column='USUARIO', blank=True) # Field name made lowercase.
    tipo_medico = models.CharField(max_length=150, db_column='TIPO_MEDICO', blank=True) # Field name made lowercase.
    medico_adscrito = models.CharField(max_length=450, db_column='MEDICO_ADSCRITO', blank=True) # Field name made lowercase.
    n = models.IntegerField(null=True, db_column='N', blank=True) # Field name made lowercase.
    cup = models.CharField(max_length=75, db_column='CUP', blank=True) # Field name made lowercase.
    paciente = models.CharField(max_length=75, db_column='PACIENTE', blank=True) # Field name made lowercase.
    tipo_paciente = models.CharField(max_length=450, db_column='TIPO_PACIENTE', blank=True) # Field name made lowercase.
    dx_1 = models.CharField(max_length=135, db_column='DX_1', blank=True) # Field name made lowercase.
    dx_1_cod = models.CharField(max_length=30, db_column='DX_1_COD', blank=True) # Field name made lowercase.
    dx_2 = models.CharField(max_length=135, db_column='DX_2', blank=True) # Field name made lowercase.
    dx_2_cod = models.CharField(max_length=30, db_column='DX_2_COD', blank=True) # Field name made lowercase.
    tratamiento = models.CharField(max_length=75, db_column='TRATAMIENTO', blank=True) # Field name made lowercase.
    estadio = models.CharField(max_length=75, db_column='ESTADIO', blank=True) # Field name made lowercase.
    sub_etapa = models.CharField(max_length=75, db_column='SUB_ETAPA', blank=True) # Field name made lowercase.
    esquema_tx = models.TextField(db_column='ESQUEMA_TX', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'onco_casos'

class OncoProductos(models.Model):
    folio = models.IntegerField(null=True, db_column='FOLIO', blank=True) # Field name made lowercase.
    id_unico = models.CharField(max_length=90, db_column='ID_UNICO', blank=True) # Field name made lowercase.
    tema = models.CharField(max_length=60, db_column='TEMA', blank=True) # Field name made lowercase.
    tema_cod = models.IntegerField(null=True, db_column='TEMA_COD', blank=True) # Field name made lowercase.
    fecha = models.DateField(null=True, db_column='FECHA', blank=True) # Field name made lowercase.
    medico_cod = models.CharField(max_length=60, db_column='MEDICO_COD', blank=True) # Field name made lowercase.
    medico_des = models.CharField(max_length=300, db_column='MEDICO_DES', blank=True) # Field name made lowercase.
    espe_des = models.CharField(max_length=60, db_column='ESPE_DES', blank=True) # Field name made lowercase.
    institucion = models.CharField(max_length=60, db_column='INSTITUCION', blank=True) # Field name made lowercase.
    sector = models.CharField(max_length=135, db_column='SECTOR', blank=True) # Field name made lowercase.
    hospital = models.CharField(max_length=765, db_column='HOSPITAL', blank=True) # Field name made lowercase.
    clue = models.CharField(max_length=135, db_column='CLUE', blank=True) # Field name made lowercase.
    estado = models.CharField(max_length=135, db_column='ESTADO', blank=True) # Field name made lowercase.
    zona = models.CharField(max_length=135, db_column='ZONA', blank=True) # Field name made lowercase.
    num_pacientes = models.IntegerField(null=True, db_column='NUM_PACIENTES', blank=True) # Field name made lowercase.
    usuario = models.CharField(max_length=45, db_column='USUARIO', blank=True) # Field name made lowercase.
    tipo_medico = models.CharField(max_length=150, db_column='TIPO_MEDICO', blank=True) # Field name made lowercase.
    medico_adscrito = models.CharField(max_length=450, db_column='MEDICO_ADSCRITO', blank=True) # Field name made lowercase.
    fecha_general = models.DateField(null=True, db_column='FECHA_GENERAL', blank=True) # Field name made lowercase.
    n = models.IntegerField(null=True, db_column='N', blank=True) # Field name made lowercase.
    cup = models.CharField(max_length=75, db_column='CUP', blank=True) # Field name made lowercase.
    paciente = models.CharField(max_length=75, db_column='PACIENTE', blank=True) # Field name made lowercase.
    tipo_paciente = models.CharField(max_length=450, db_column='TIPO_PACIENTE', blank=True) # Field name made lowercase.
    dx_1 = models.CharField(max_length=135, db_column='DX_1', blank=True) # Field name made lowercase.
    dx_1_cod = models.CharField(max_length=30, db_column='DX_1_COD', blank=True) # Field name made lowercase.
    dx_2 = models.CharField(max_length=135, db_column='DX_2', blank=True) # Field name made lowercase.
    dx_2_cod = models.CharField(max_length=30, db_column='DX_2_COD', blank=True) # Field name made lowercase.
    tratamiento = models.CharField(max_length=75, db_column='TRATAMIENTO', blank=True) # Field name made lowercase.
    estadio = models.CharField(max_length=75, db_column='ESTADIO', blank=True) # Field name made lowercase.
    sub_etapa = models.CharField(max_length=75, db_column='SUB_ETAPA', blank=True) # Field name made lowercase.
    prod_cod = models.CharField(max_length=90, db_column='PROD_COD', blank=True) # Field name made lowercase.
    prod_des = models.CharField(max_length=150, db_column='PROD_DES', blank=True) # Field name made lowercase.
    principio_cod = models.CharField(max_length=90, db_column='PRINCIPIO_COD', blank=True) # Field name made lowercase.
    principio_des = models.CharField(max_length=150, db_column='PRINCIPIO_DES', blank=True) # Field name made lowercase.
    manu_des = models.CharField(max_length=90, db_column='MANU_DES', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'onco_productos'