SELECT
    Name                AS nome_paciente,
    Age                 AS idade_paciente,
    Gender              AS sexo_paciente,
    Blood_Type          AS tipo_sanguineo,
    Medical_Condition   AS condicoes_medicas,
    Date_of_Admission   AS data_admissao,
    Doctor              AS medico_responsavel,
    Hospital            AS hospital,
    Insurance_Provider  AS seguradora,
    Billing_Amount      AS valor_faturamento,
    Room_Number         AS numero_quarto,
    Admission_Type      AS tipo_admissao,
    Discharge_Date      AS data_alta,
    Medication          AS medicacao,
    Test_Results        AS resultados_testes
FROM {{ ref('healthcare_dataset') }}