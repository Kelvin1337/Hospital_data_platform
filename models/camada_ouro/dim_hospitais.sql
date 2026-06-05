WITH hospitais_unicos AS (
    -- Seleciona os hospitais de forma única primeiro
    SELECT DISTINCT hospital 
    FROM {{ ref('stg_pacientes') }}
)

SELECT
    -- Gera o ID numérico sequencial (1, 2, 3...)
    ROW_NUMBER() OVER (ORDER BY hospital) AS id_hospital,
    hospital                              AS nome_hospital
FROM hospitais_unicos