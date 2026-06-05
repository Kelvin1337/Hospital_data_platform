WITH medicos_unicos AS (
    SELECT DISTINCT medico_responsavel 
    FROM {{ ref('stg_pacientes') }}
),     -- Seleciona os médicos de forma única e ordena alfabeticamente


medicos_posicionados AS (
    SELECT
        ROW_NUMBER() OVER (ORDER BY medico_responsavel) AS id_medico,
        medico_responsavel                              AS nome_medico
    FROM medicos_unicos         -- O ROW_NUMBER gera o ID sequencial baseado na ordem alfabética

)

SELECT 
    id_medico,
    nome_medico
FROM medicos_posicionados 
ORDER BY id_medico -- Garante que a saída final esteja ordenada pelo ID do médico para facilitar a leitura e conferência dos dados.