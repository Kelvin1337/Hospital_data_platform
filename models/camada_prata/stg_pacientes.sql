SELECT
    UPPER(TRIM(NAME))               AS nome_paciente,
    AGE                              AS idade_paciente,

    CASE 
        WHEN UPPER(TRIM(GENDER)) = 'MALE' THEN 'M'  
        WHEN UPPER(TRIM(GENDER)) = 'FEMALE' THEN 'F' -- Converte gênero para formato mais simplificado
        ELSE 'Não Informado'
    END                               AS sexo_paciente,

    UPPER(TRIM(BLOOD_TYPE))          AS tipo_sanguineo,
    
    case 

        when UPPER(TRIM(MEDICAL_CONDITION)) = 'ARTHRITIS' then 'ARTRITE'
        when UPPER(TRIM(MEDICAL_CONDITION)) = 'ASTHMA' then 'ASMA'
        when UPPER(TRIM(MEDICAL_CONDITION)) = 'CANCER' then 'CÂNCER'
        when UPPER(TRIM(MEDICAL_CONDITION)) = 'DIABETES' then 'DIABETES'
        when UPPER(TRIM(MEDICAL_CONDITION)) = 'HYPERTENSION' then 'HIPERTENSÃO'
        when UPPER(TRIM(MEDICAL_CONDITION)) = 'OBESITY' then 'OBESIDADE'

        else 'OUTRAS CONDIÇÕES'                      -- Agrupa condições médicas em categorias mais amplas para facilitar análises futuras
    end AS condicoes_medicas,
    
    
    DATE_OF_ADMISSION               AS data_admissao,
    UPPER(TRIM(DOCTOR))             AS medico_responsavel,
    UPPER(TRIM(HOSPITAL))           AS hospital,
    UPPER(TRIM(INSURANCE_PROVIDER)) AS seguradora,
    BILLING_AMOUNT                  AS valor_faturamento,
    ROOM_NUMBER                    AS numero_quarto,
    
    CASE 
        WHEN UPPER(TRIM(ADMISSION_TYPE)) = 'EMERGENCY' THEN 'EMERGÊNCIA' 
        WHEN UPPER(TRIM(ADMISSION_TYPE)) = 'ELECTIVE' THEN 'ELETIVA'     
        WHEN UPPER(TRIM(ADMISSION_TYPE)) = 'URGENT' THEN 'URGENTE'       -- Padroniza o tipo de admissão para português
        ELSE 'NÃO INFORMADO'
    END                               AS tipo_admissao,
      
    DISCHARGE_DATE                 AS data_alta,
    
    CASE
        WHEN UPPER(TRIM(MEDICATION)) = 'IBUPROFEN' THEN 'IBUPROFENO'     
        WHEN UPPER(TRIM(MEDICATION)) = 'PARACETAMOL' THEN 'PARACETAMOL'  
        WHEN UPPER(TRIM(MEDICATION)) = 'PENICILLIN' THEN 'PENICILINA'    
        WHEN UPPER(TRIM(MEDICATION)) = 'ASPIRIN' THEN 'ASPIRINA'         
        when UPPER(TRIM(MEDICATION)) = 'LIPITOR' THEN 'LIPITOR'          -- Padroniza o nome do medicamento para português para evitar incosistências
        ELSE 'NÃO INFORMADO'
    END                               AS medicacao,   
    
    CASE 
        WHEN UPPER(TRIM(TEST_RESULTS)) = 'INCONCLUSIVE' THEN 'INCONCLUSIVO'
        WHEN UPPER(TRIM(TEST_RESULTS)) = 'ABNORMAL' THEN 'ANORMAL'
        WHEN UPPER(TRIM(TEST_RESULTS)) = 'NORMAL' THEN 'NORMAL'          -- Padroniza o resultado dos testes para português para evitar incosistências
        ELSE 'NÃO INFORMADO'
    END AS resultado_testes,

    DATEDIFF(day, DATE_OF_ADMISSION, DISCHARGE_DATE) AS dias_internado

FROM {{ ref('healthcare_dataset') }}