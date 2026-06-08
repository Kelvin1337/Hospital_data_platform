{% macro categorizar_grupo_idade(column_name) %}
    CASE 
        WHEN {{ column_name }} < 12 THEN 'Criança'
        WHEN {{ column_name }} BETWEEN 12 AND 59 THEN 'Adulto'
        WHEN {{ column_name }} >= 60 THEN 'Idoso'
        ELSE 'Não Informado'
    END
{% endmacro %}