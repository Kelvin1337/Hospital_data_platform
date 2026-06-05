WITH pacientes AS (
    -- Seleciona os pacientes de forma única primeiro
    SELECT DISTINCT pacientes 
    FROM {{ ref('stg_pacientes') }}
)

SELECT
    -- Gera o ID numérico sequencial (1, 2, 3...)
    ROW_NUMBER() OVER (ORDER BY pacientes) AS id_paciente,
    pacientes                              AS nome_paciente
FROM pacientes