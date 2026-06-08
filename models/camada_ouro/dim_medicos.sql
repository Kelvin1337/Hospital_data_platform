WITH medicos_unicos AS (
    SELECT DISTINCT medico_responsavel 
    FROM {{ ref('stg_pacientes') }}
),

medicos_posicionados AS (
    SELECT
        ROW_NUMBER() OVER (ORDER BY medico_responsavel) AS id_medico,
        medico_responsavel                             AS nome_medico
    FROM medicos_unicos
)

SELECT 
    id_medico,
    nome_medico
FROM medicos_posicionados
ORDER BY id_medico