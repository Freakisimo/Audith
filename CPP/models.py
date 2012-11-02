# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

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

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=240, unique=True)
    class Meta:
        db_table = u'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    content_type = models.ForeignKey(DjangoContentType)
    codename = models.CharField(max_length=300, unique=True)
    class Meta:
        db_table = u'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=90, unique=True)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=384)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = u'auth_user_user_permissions'

class BiologicosCasos(models.Model):
    folio = models.IntegerField(null=True, db_column='FOLIO', blank=True) # Field name made lowercase.
    id_unico = models.CharField(max_length=90, db_column='ID_UNICO', blank=True) # Field name made lowercase.
    tema = models.CharField(max_length=60, db_column='TEMA', blank=True) # Field name made lowercase.
    tema_cod = models.IntegerField(null=True, db_column='TEMA_COD', blank=True) # Field name made lowercase.
    fecha = models.DateField(null=True, db_column='FECHA', blank=True) # Field name made lowercase.
    medico_cod = models.CharField(max_length=60, db_column='MEDICO_COD', blank=True) # Field name made lowercase.
    medico_des = models.CharField(max_length=300, db_column='MEDICO_DES', blank=True) # Field name made lowercase.
    espe_des = models.CharField(max_length=60, db_column='ESPE_DES', blank=True) # Field name made lowercase.
    institucion = models.CharField(max_length=60, db_column='INSTITUCION', blank=True) # Field name made lowercase.
    hospital = models.CharField(max_length=765, db_column='HOSPITAL', blank=True) # Field name made lowercase.
    clue = models.CharField(max_length=135, db_column='CLUE', blank=True) # Field name made lowercase.
    estado = models.CharField(max_length=135, db_column='ESTADO', blank=True) # Field name made lowercase.
    num_pacientes = models.IntegerField(null=True, db_column='NUM_PACIENTES', blank=True) # Field name made lowercase.
    usuario = models.CharField(max_length=45, db_column='USUARIO', blank=True) # Field name made lowercase.
    tipo_medico = models.CharField(max_length=150, db_column='TIPO_MEDICO', blank=True) # Field name made lowercase.
    medico_adscrito = models.CharField(max_length=450, db_column='MEDICO_ADSCRITO', blank=True) # Field name made lowercase.
    num_pacientes_biologicos = models.CharField(max_length=135, db_column='NUM_PACIENTES_BIOLOGICOS', blank=True) # Field name made lowercase.
    n = models.IntegerField(null=True, db_column='N', blank=True) # Field name made lowercase.
    cup = models.CharField(max_length=9, db_column='CUP', blank=True) # Field name made lowercase.
    paciente = models.CharField(max_length=135, db_column='PACIENTE', blank=True) # Field name made lowercase.
    tipo_paciente = models.CharField(max_length=450, db_column='TIPO_PACIENTE', blank=True) # Field name made lowercase.
    linea_biologicos = models.CharField(max_length=135, db_column='LINEA_BIOLOGICOS', blank=True) # Field name made lowercase.
    entidad = models.CharField(max_length=600, db_column='ENTIDAD', blank=True) # Field name made lowercase.
    tipo_terapia = models.CharField(max_length=51, db_column='TIPO_TERAPIA') # Field name made lowercase.
    esquema_tx = models.TextField(db_column='ESQUEMA_TX', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'biologicos_casos'

class BiologicosProductos(models.Model):
    folio = models.IntegerField(null=True, db_column='FOLIO', blank=True) # Field name made lowercase.
    id_unico = models.CharField(max_length=90, db_column='ID_UNICO', blank=True) # Field name made lowercase.
    tema = models.CharField(max_length=60, db_column='TEMA', blank=True) # Field name made lowercase.
    tema_cod = models.IntegerField(null=True, db_column='TEMA_COD', blank=True) # Field name made lowercase.
    fecha = models.DateField(null=True, db_column='FECHA', blank=True) # Field name made lowercase.
    medico_cod = models.CharField(max_length=60, db_column='MEDICO_COD', blank=True) # Field name made lowercase.
    medico_des = models.CharField(max_length=300, db_column='MEDICO_DES', blank=True) # Field name made lowercase.
    espe_des = models.CharField(max_length=60, db_column='ESPE_DES', blank=True) # Field name made lowercase.
    institucion = models.CharField(max_length=60, db_column='INSTITUCION', blank=True) # Field name made lowercase.
    hospital = models.CharField(max_length=765, db_column='HOSPITAL', blank=True) # Field name made lowercase.
    clue = models.CharField(max_length=135, db_column='CLUE', blank=True) # Field name made lowercase.
    estado = models.CharField(max_length=135, db_column='ESTADO', blank=True) # Field name made lowercase.
    num_pacientes = models.IntegerField(null=True, db_column='NUM_PACIENTES', blank=True) # Field name made lowercase.
    usuario = models.CharField(max_length=45, db_column='USUARIO', blank=True) # Field name made lowercase.
    tipo_medico = models.CharField(max_length=150, db_column='TIPO_MEDICO', blank=True) # Field name made lowercase.
    medico_adscrito = models.CharField(max_length=450, db_column='MEDICO_ADSCRITO', blank=True) # Field name made lowercase.
    num_pacientes_biologicos = models.CharField(max_length=135, db_column='NUM_PACIENTES_BIOLOGICOS', blank=True) # Field name made lowercase.
    n = models.IntegerField(null=True, db_column='N', blank=True) # Field name made lowercase.
    cup = models.CharField(max_length=9, db_column='CUP', blank=True) # Field name made lowercase.
    paciente = models.CharField(max_length=135, db_column='PACIENTE', blank=True) # Field name made lowercase.
    tipo_paciente = models.CharField(max_length=450, db_column='TIPO_PACIENTE', blank=True) # Field name made lowercase.
    linea_biologicos = models.CharField(max_length=135, db_column='LINEA_BIOLOGICOS', blank=True) # Field name made lowercase.
    entidad = models.CharField(max_length=600, db_column='ENTIDAD', blank=True) # Field name made lowercase.
    prod_cod = models.CharField(max_length=135, db_column='PROD_COD', blank=True) # Field name made lowercase.
    prod_des = models.CharField(max_length=135, db_column='PROD_DES', blank=True) # Field name made lowercase.
    principio_cod = models.CharField(max_length=135, db_column='PRINCIPIO_COD', blank=True) # Field name made lowercase.
    principio_des = models.CharField(max_length=135, db_column='PRINCIPIO_DES', blank=True) # Field name made lowercase.
    manu_des = models.CharField(max_length=135, db_column='MANU_DES', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'biologicos_productos'

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

class CaLaboratorio(models.Model):
    id = models.IntegerField(primary_key=True)
    lab_cod = models.CharField(max_length=9)
    lab_des = models.CharField(max_length=150)
    class Meta:
        db_table = u'ca_laboratorio'

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

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey(DjangoContentType, null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=600)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    app_label = models.CharField(max_length=300, unique=True)
    model = models.CharField(max_length=300, unique=True)
    class Meta:
        db_table = u'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=120, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    class Meta:
        db_table = u'django_site'

class FormsField(models.Model):
    id = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=600)
    slug = models.CharField(max_length=300)
    field_type = models.IntegerField()
    required = models.IntegerField()
    visible = models.IntegerField()
    choices = models.CharField(max_length=3000)
    default = models.CharField(max_length=6000)
    placeholder_text = models.CharField(max_length=300, blank=True)
    help_text = models.CharField(max_length=300)
    form = models.ForeignKey(FormsForm)
    order = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'forms_field'

class FormsFieldentry(models.Model):
    id = models.IntegerField(primary_key=True)
    field_id = models.IntegerField()
    value = models.CharField(max_length=6000, blank=True)
    entry = models.ForeignKey(FormsFormentry)
    class Meta:
        db_table = u'forms_fieldentry'

class FormsForm(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=300, unique=True)
    intro = models.TextField()
    button_text = models.CharField(max_length=150)
    response = models.TextField()
    status = models.IntegerField()
    publish_date = models.DateTimeField(null=True, blank=True)
    expiry_date = models.DateTimeField(null=True, blank=True)
    login_required = models.IntegerField()
    send_email = models.IntegerField()
    email_from = models.CharField(max_length=225)
    email_copies = models.CharField(max_length=600)
    email_subject = models.CharField(max_length=600)
    email_message = models.TextField()
    class Meta:
        db_table = u'forms_form'

class FormsFormSites(models.Model):
    id = models.IntegerField(primary_key=True)
    form = models.ForeignKey(FormsForm)
    site = models.ForeignKey(DjangoSite)
    class Meta:
        db_table = u'forms_form_sites'

class FormsFormentry(models.Model):
    id = models.IntegerField(primary_key=True)
    entry_time = models.DateTimeField()
    form = models.ForeignKey(FormsForm)
    class Meta:
        db_table = u'forms_formentry'

class Generales(models.Model):
    id_principal = models.IntegerField(primary_key=True, db_column='ID_PRINCIPAL') # Field name made lowercase.
    id_unico = models.CharField(max_length=90, db_column='ID_UNICO') # Field name made lowercase.
    folio = models.IntegerField(null=True, db_column='FOLIO', blank=True) # Field name made lowercase.
    tema = models.CharField(max_length=60, db_column='TEMA', blank=True) # Field name made lowercase.
    tema_cod = models.IntegerField(null=True, db_column='TEMA_COD', blank=True) # Field name made lowercase.
    fecha = models.DateField(primary_key=True, db_column='FECHA') # Field name made lowercase.
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
    num_pacientes_biologicos = models.CharField(max_length=135, db_column='NUM_PACIENTES_BIOLOGICOS', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'generales'

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

class HematoCasos(models.Model):
    folio = models.IntegerField(null=True, db_column='FOLIO', blank=True) # Field name made lowercase.
    id_unico = models.CharField(max_length=90, db_column='ID_UNICO', blank=True) # Field name made lowercase.
    tema = models.CharField(max_length=60, db_column='TEMA', blank=True) # Field name made lowercase.
    tema_cod = models.IntegerField(null=True, db_column='TEMA_COD', blank=True) # Field name made lowercase.
    fecha = models.DateField(null=True, db_column='FECHA', blank=True) # Field name made lowercase.
    medico_cod = models.CharField(max_length=60, db_column='MEDICO_COD', blank=True) # Field name made lowercase.
    medico_des = models.CharField(max_length=300, db_column='MEDICO_DES', blank=True) # Field name made lowercase.
    espe_des = models.CharField(max_length=60, db_column='ESPE_DES', blank=True) # Field name made lowercase.
    institucion = models.CharField(max_length=60, db_column='INSTITUCION', blank=True) # Field name made lowercase.
    hospital = models.CharField(max_length=765, db_column='HOSPITAL', blank=True) # Field name made lowercase.
    clue = models.CharField(max_length=135, db_column='CLUE', blank=True) # Field name made lowercase.
    estado = models.CharField(max_length=135, db_column='ESTADO', blank=True) # Field name made lowercase.
    num_pacientes = models.IntegerField(null=True, db_column='NUM_PACIENTES', blank=True) # Field name made lowercase.
    usuario = models.CharField(max_length=45, db_column='USUARIO', blank=True) # Field name made lowercase.
    tipo_medico = models.CharField(max_length=150, db_column='TIPO_MEDICO', blank=True) # Field name made lowercase.
    medico_adscrito = models.CharField(max_length=450, db_column='MEDICO_ADSCRITO', blank=True) # Field name made lowercase.
    n = models.IntegerField(null=True, db_column='N', blank=True) # Field name made lowercase.
    cup = models.CharField(max_length=9, db_column='CUP', blank=True) # Field name made lowercase.
    paciente = models.CharField(max_length=135, db_column='PACIENTE', blank=True) # Field name made lowercase.
    tipo_paciente = models.CharField(max_length=450, db_column='TIPO_PACIENTE', blank=True) # Field name made lowercase.
    tipo_de_cancer = models.CharField(max_length=135, db_column='TIPO_DE_CANCER', blank=True) # Field name made lowercase.
    tipo_histologico = models.CharField(max_length=450, db_column='TIPO_HISTOLOGICO', blank=True) # Field name made lowercase.
    subtipo_histologico = models.CharField(max_length=450, db_column='SUBTIPO_HISTOLOGICO', blank=True) # Field name made lowercase.
    variedad_histologico = models.CharField(max_length=777, db_column='VARIEDAD_HISTOLOGICO', blank=True) # Field name made lowercase.
    esquema_tx = models.TextField(db_column='ESQUEMA_TX', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'hemato_casos'

class HematoProductos(models.Model):
    folio = models.IntegerField(null=True, db_column='FOLIO', blank=True) # Field name made lowercase.
    id_unico = models.CharField(max_length=90, db_column='ID_UNICO', blank=True) # Field name made lowercase.
    tema = models.CharField(max_length=60, db_column='TEMA', blank=True) # Field name made lowercase.
    tema_cod = models.IntegerField(null=True, db_column='TEMA_COD', blank=True) # Field name made lowercase.
    fecha = models.DateField(null=True, db_column='FECHA', blank=True) # Field name made lowercase.
    medico_cod = models.CharField(max_length=60, db_column='MEDICO_COD', blank=True) # Field name made lowercase.
    medico_des = models.CharField(max_length=300, db_column='MEDICO_DES', blank=True) # Field name made lowercase.
    espe_des = models.CharField(max_length=60, db_column='ESPE_DES', blank=True) # Field name made lowercase.
    institucion = models.CharField(max_length=60, db_column='INSTITUCION', blank=True) # Field name made lowercase.
    hospital = models.CharField(max_length=765, db_column='HOSPITAL', blank=True) # Field name made lowercase.
    clue = models.CharField(max_length=135, db_column='CLUE', blank=True) # Field name made lowercase.
    estado = models.CharField(max_length=135, db_column='ESTADO', blank=True) # Field name made lowercase.
    num_pacientes = models.IntegerField(null=True, db_column='NUM_PACIENTES', blank=True) # Field name made lowercase.
    usuario = models.CharField(max_length=45, db_column='USUARIO', blank=True) # Field name made lowercase.
    tipo_medico = models.CharField(max_length=150, db_column='TIPO_MEDICO', blank=True) # Field name made lowercase.
    medico_adscrito = models.CharField(max_length=450, db_column='MEDICO_ADSCRITO', blank=True) # Field name made lowercase.
    n = models.IntegerField(null=True, db_column='N', blank=True) # Field name made lowercase.
    cup = models.CharField(max_length=9, db_column='CUP', blank=True) # Field name made lowercase.
    paciente = models.CharField(max_length=135, db_column='PACIENTE', blank=True) # Field name made lowercase.
    tipo_paciente = models.CharField(max_length=450, db_column='TIPO_PACIENTE', blank=True) # Field name made lowercase.
    tipo_de_cancer = models.CharField(max_length=135, db_column='TIPO_DE_CANCER', blank=True) # Field name made lowercase.
    tipo_histologico = models.CharField(max_length=450, db_column='TIPO_HISTOLOGICO', blank=True) # Field name made lowercase.
    subtipo_histologico = models.CharField(max_length=450, db_column='SUBTIPO_HISTOLOGICO', blank=True) # Field name made lowercase.
    variedad_histologico = models.CharField(max_length=777, db_column='VARIEDAD_HISTOLOGICO', blank=True) # Field name made lowercase.
    prod_cod = models.CharField(max_length=135, db_column='PROD_COD', blank=True) # Field name made lowercase.
    prod_des = models.CharField(max_length=135, db_column='PROD_DES', blank=True) # Field name made lowercase.
    principio_cod = models.CharField(max_length=135, db_column='PRINCIPIO_COD', blank=True) # Field name made lowercase.
    principio_des = models.CharField(max_length=135, db_column='PRINCIPIO_DES', blank=True) # Field name made lowercase.
    manu_des = models.CharField(max_length=135, db_column='MANU_DES', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'hemato_productos'

class MedicosExcluir(models.Model):
    medico_des = models.CharField(max_length=765, db_column='MEDICO_DES', blank=True) # Field name made lowercase.
    hospital = models.CharField(max_length=765, db_column='HOSPITAL', blank=True) # Field name made lowercase.
    institucion = models.CharField(max_length=765, db_column='INSTITUCION', blank=True) # Field name made lowercase.
    estado = models.CharField(max_length=765, db_column='ESTADO', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'medicos_excluir'

class OncoCasos(models.Model):
