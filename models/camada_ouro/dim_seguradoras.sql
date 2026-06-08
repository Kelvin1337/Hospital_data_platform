WITH seguradoras_unicas AS (
    SELECT DISTINCT seguradora 
    FROM {{ ref('stg_pacientes') }}
    WHERE seguradora IS NOT NULL
),

seguradoras_posicionados AS (
    SELECT
        ROW_NUMBER() OVER (ORDER BY seguradora) AS id_seguradora,
        seguradora                              AS nome_seguradora
    FROM seguradoras_unicas
)

SELECT 
    id_seguradora,
    nome_seguradora
FROM seguradoras_posicionados
ORDER BY id_seguradora