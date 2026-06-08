WITH hospitais_unicos AS (
    SELECT DISTINCT hospital 
    FROM {{ ref('stg_pacientes') }}
),

hospitais_posicionados AS (
    SELECT
        ROW_NUMBER() OVER (ORDER BY hospital) AS id_hospital,
        hospital                              AS nome_hospital
    FROM hospitais_unicos
)

SELECT 
    id_hospital,
    nome_hospital
FROM hospitais_posicionados
ORDER BY id_hospital