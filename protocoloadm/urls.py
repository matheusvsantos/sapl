from django.conf.urls import include, url

from protocoloadm.views import (AnularProtocoloAdmView,
                                DetailDocumentoAdministrativo,
                                DocumentoAcessorioAdministrativoView,
                                get_autor,
                                PesquisarDocumentoAdministrativo,
                                ProposicaoReceberView, ProposicaoView,
                                ProposicoesIncorporadasView,
                                ProposicoesNaoIncorporadasView,
                                ProposicoesNaoRecebidasView,
                                ProtocoloDocumentoView, ProtocoloListView,
                                ProtocoloMateriaView, ProtocoloPesquisaView,
                                TramitacaoAdmDeleteView, TramitacaoAdmEditView,
                                TramitacaoAdmIncluirView, TramitacaoAdmView,
                                documento_acessorio_administrativo_crud,
                                documento_administrativo_crud,
                                protocolo_documento_crud,
                                protocolo_materia_crud,
                                status_tramitacao_administrativo_crud,
                                tipo_documento_administrativo_crud,
                                tramitacao_administrativo_crud)

urlpatterns = [
    url(r'^protocoloadm/docadm/', include(documento_administrativo_crud.urls)),
    url(r'^protocoloadm/tipo-documento-adm/',
        include(tipo_documento_administrativo_crud.urls)),
    url(r'^protocoloadm/doc-acessorio/',
        include(documento_acessorio_administrativo_crud.urls)),
    url(r'^protocoloadm/status-tramitacao-adm/',
        include(status_tramitacao_administrativo_crud.urls)),
    url(r'^protocoloadm/tramitacao-adm/',
        include(tramitacao_administrativo_crud.urls)),
    url(r'^protocoloadm/protocolo-doc/',
        include(protocolo_documento_crud.urls)),
    url(r'^protocoloadm/protocolo-mat/',
        include(protocolo_materia_crud.urls), name='protocolomat'),

    url(r'^protocoloadm/get_autor$',
        get_autor, name='get_autor'),
    url(r'^protocoloadm/protocolo$',
        ProtocoloPesquisaView.as_view(), name='protocolo'),
    # url(r'^protocoloadm/anular-protocolo/',
    #     include(anular_protocolo_crud.urls), name='anular_protocolo'),
    url(r'^protocoloadm/protocolo_list$',
        ProtocoloListView.as_view(), name='protocolo_list'),
    url(r'^protocoloadm/anular-protocolo',
        AnularProtocoloAdmView.as_view(), name='anular_protocolo'),
    url(r'^protocoloadm/protocolar-doc',
        ProtocoloDocumentoView.as_view(), name='protocolar_doc'),
    url(r'^protocoloadm/protocolar-mat',
        ProtocoloMateriaView.as_view(), name='protocolar_mat'),
    url(r'^protocoloadm/pesq-doc-adm',
        PesquisarDocumentoAdministrativo.as_view(), name='pesq_doc_adm'),
    url(r'^protocoloadm/doc-adm/(?P<pk>\d+)',
        DetailDocumentoAdministrativo.as_view(), name='detail_doc_adm'),
    url(r'^protocoloadm/doc-ace-adm/(?P<pk>\d+)',
        DocumentoAcessorioAdministrativoView.as_view(), name='doc_ace_adm'),

    url(r'^protocoloadm/(?P<pk>\d+)/tramitacao$',
        TramitacaoAdmView.as_view(), name='tramitacao'),
    url(r'^protocoloadm/(?P<pk>\d+)/tramitacao_incluir',
        TramitacaoAdmIncluirView.as_view(), name='tramitacao_incluir'),
    url(r'^protocoloadm/(?P<pk>\d+)/tramitacao_edit',
        TramitacaoAdmEditView.as_view(), name='tramitacao_edit'),
    url(r'^protocoloadm/(?P<pk>\d+)/tramitacao_delete/(?P<oid>\d+)',
        TramitacaoAdmDeleteView.as_view(), name='tramitacao_delete'),    

    # TODO: move to Proposicoes app
    url(r'^protocoloadm/proposicao-receber',
        ProposicaoReceberView.as_view(), name='proposicao_receber'),
    url(r'^protocoloadm/proposicoes-naorecebidas',
        ProposicoesNaoRecebidasView.as_view(),
        name='proposicoes_naorecebidas'),
    url(r'^protocoloadm/proposicoes-naoincorporadas',
        ProposicoesNaoIncorporadasView.as_view(),
        name='proposicoes_naoincorporadas'),
    url(r'^protocoloadm/proposicoes-incorporadas',
        ProposicoesIncorporadasView.as_view(),
        name='proposicoes_incorporadas'),
    url(r'^protocoloadm/(?P<pk>\d+)/proposicao',
        ProposicaoView.as_view(), name='proposicao_view'),
]
