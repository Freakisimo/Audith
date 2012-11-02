from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CPP.views.home', name='home'),
    # url(r'^CPP/', include('CPP.foo.urls')),

    # Aplicacion audith
    url(r'^mezcla_institucion/$','audith.views.mezcla_institucion'),
    url(r'^dx_1/$','audith.views.dx_1'),
    url(r'^dx_2/$','audith.views.dx_2'),
    url(r'^numero_pacientes/$','audith.views.numero_pacientes'),
    url(r'^paciente/$','audith.views.paciente'),
    url(r'^esquemas/$','audith.views.esquemas'),
    url(r'^folio_paciente/$','audith.views.folio_paciente'),
    url(r'^medicos_residentes/$','audith.views.medicos_residentes'),
    url(r'^inicio/$','audith.views.inicio'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
