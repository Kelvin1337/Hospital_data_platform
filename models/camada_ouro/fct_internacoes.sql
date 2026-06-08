WITH prata_pacientes AS (
    SELECT *
    FROM {{ ref('stg_pacientes') }}
),

pacientes AS (
    SELECT
        id_paciente,
        nome_paciente,
        idade_paciente,
        sexo_paciente,
        tipo_sanguineo
    FROM {{ ref('dim_pacientes') }}
),

medicos AS (
    SELECT
        id_medico,
        nome_medico
    FROM {{ ref('dim_medicos') }}
),

hospitais AS (
    SELECT
        id_hospital,
        nome_hospital
    FROM {{ ref('dim_hospitais') }}
),

medicamentos AS (
    SELECT
        id_medicamento,
        nome_medicamento
    FROM {{ ref('dim_medicamentos') }}
),

seguradoras AS (
    SELECT
        id_seguradora,
        nome_seguradora
    FROM {{ ref('dim_seguradoras') }}
)

SELECT

    -- Chaves Estrangeiras
    pac.id_paciente      AS fk_paciente,
    m.id_medico          AS fk_medico,
    h.id_hospital        AS fk_hospital,
    med.id_medicamento   AS fk_medicamento,
    seg.id_seguradora    AS fk_seguradora,

    -- Dados da internação
    p.numero_quarto,
    p.tipo_admissao,
    p.condicoes_medicas,
    p.resultado_testes,

    -- Datas
    p.data_admissao,
    p.data_alta,

    -- Métricas
    p.dias_internado,
    p.valor_faturamento

FROM prata_pacientes p

LEFT JOIN pacientes pac
    ON p.nome_paciente = pac.nome_paciente
   AND p.idade_paciente = pac.idade_paciente
   AND p.sexo_paciente = pac.sexo_paciente
   AND p.tipo_sanguineo = pac.tipo_sanguineo

LEFT JOIN medicos m
    ON p.medico_responsavel = m.nome_medico

LEFT JOIN hospitais h
    ON p.hospital = h.nome_hospital

LEFT JOIN medicamentos med
    ON p.medicacao = med.nome_medicamento

LEFT JOIN seguradoras seg
    ON p.seguradora = seg.nome_seguradora