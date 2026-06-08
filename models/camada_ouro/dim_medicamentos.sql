WITH medicamentos_unicos AS (
    SELECT DISTINCT medicacao 
    FROM {{ ref('stg_pacientes') }}
    WHERE medicacao IS NOT NULL
),

medicamentos_posicionados AS (
    SELECT
        ROW_NUMBER() OVER (ORDER BY medicacao) AS id_medicamento,
        medicacao                              AS nome_medicamento
    FROM medicamentos_unicos
)

SELECT 
    id_medicamento,
    nome_medicamento
FROM medicamentos_posicionados
ORDER BY id_medicamento