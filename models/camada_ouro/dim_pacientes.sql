WITH pacientes_unicos AS (
    SELECT 
        nome_paciente,
        idade_paciente,
        sexo_paciente,
        tipo_sanguineo
    FROM {{ ref('stg_pacientes') }}
    GROUP BY nome_paciente, idade_paciente, sexo_paciente, tipo_sanguineo
),

pacientes_posicionados AS (
    SELECT
        ROW_NUMBER() OVER (ORDER BY nome_paciente) AS id_paciente,
        nome_paciente,
        idade_paciente,
        sexo_paciente,
        tipo_sanguineo
    FROM pacientes_unicos
)

SELECT 
    id_paciente,
    nome_paciente,
    idade_paciente,
    sexo_paciente,
    tipo_sanguineo,
    -- Chamando a macro de forma limpa:
    {{ categorizar_grupo_idade('idade_paciente') }} AS faixa_etaria
FROM pacientes_posicionados
ORDER BY id_paciente