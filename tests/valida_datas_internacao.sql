-- Este teste busca linhas onde a data de alta aconteceu ANTES da data de admissão.
-- Se retornar qualquer registro, o teste vai falhar (o que é o correto para pegar erros no dado).

SELECT *
FROM {{ ref('fct_internacoes') }}
WHERE data_alta < data_admissao