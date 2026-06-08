# Hospital Data Platform

![GitHub repo size](https://img.shields.io/github/repo-size/Kelvin1337/hospital_data_platform)
![GitHub language count](https://img.shields.io/github/languages/count/Kelvin1337/hospital_data_platform)
![GitHub last commit](https://img.shields.io/github/last-commit/Kelvin1337/hospital_data_platform)

## Plataforma de Dados Hospitalares

Sistema de Engenharia de Dados desenvolvido para simular um ambiente corporativo de processamento e transformação de dados hospitalares utilizando **dbt**, **Snowflake** e **SQL**.

O projeto aplica conceitos modernos de **Data Engineering** e **Analytics Engineering**, transformando dados brutos em informações confiáveis para análises operacionais e estratégicas através da arquitetura em camadas **Bronze → Silver → Gold**.

---

## Objetivos do Projeto

* Construir uma arquitetura de dados escalável;
* Simular um ambiente real de Engenharia de Dados;
* Aplicar boas práticas de modelagem e governança de dados;
* Garantir qualidade e consistência das informações;
* Disponibilizar dados prontos para consumo analítico.

---

## Arquitetura de Dados

### 🥉 Bronze Layer

Camada responsável pelo armazenamento dos dados brutos recebidos das fontes de origem.

Principais características:

* Dados sem tratamento;
* Preservação da informação original;
* Histórico completo dos registros;
* Fonte para as próximas etapas do pipeline.

### Silver Layer

Camada de tratamento e padronização dos dados.

Principais atividades:

* Limpeza de dados;
* Remoção de duplicidades;
* Padronização de formatos;
* Tratamento de valores nulos;
* Aplicação de regras de negócio.

### Gold Layer

Camada analítica destinada ao consumo por dashboards e relatórios.

Principais entregas:

* Indicadores de negócio;
* Métricas consolidadas;
* Visões analíticas;
* Dados prontos para BI.

---

## Funcionalidades Implementadas

* Estruturação de projeto dbt;
* Ingestão de dados via Seeds;
* Organização em camadas Bronze, Silver e Gold;
* Transformações SQL com dbt;
* Versionamento utilizando Git e GitHub;
* Modelagem de dados para ambiente hospitalar;
* Aplicação de boas práticas de Engenharia de Dados.

---

## Tecnologias Utilizadas

### Engenharia de Dados

* dbt Core
* Snowflake
* SQL

### Versionamento

* Git
* GitHub

### Ambiente de Desenvolvimento

* Python
* Visual Studio Code

---

## 📁 Estrutura do Projeto

```text
hospital_data_platform/
│
├── analyses/
├── macros/
├── models/
│   ├── camada_bronze/
│   ├── camada_prata/
│   └── camada_bouro/
│
├── seeds/
├── snapshots/
├── tests/
│
├── dbt_project.yml
├── README.md
└── .gitignore
```

---

## Como Executar

### Clonar o Repositório

```bash
git clone https://github.com/Kelvin1337/hospital_data_platform.git
```

### Acessar o Projeto

```bash
cd hospital_data_platform
```

### Carregar os Seeds

```bash
dbt seed
```

### Executar os Modelos

```bash
dbt run
```

### Executar os Testes

```bash
dbt test
```

### Gerar Documentação

```bash
dbt docs generate
dbt docs serve
```

---

## Próximas Melhorias

* Data Quality Tests;
* Snapshots para histórico de alterações;
* Pipeline CI/CD com GitHub Actions;
* Monitoramento e observabilidade dos pipelines;
* Modelagem dimensional para Analytics.

---

## Autor

**Kelvin Silva**

Engenheiro de Dados em formação com foco em Engenharia de Dados, Analytics Engineering, Cloud Computing e soluções modernas de processamento de dados.

GitHub: https://github.com/Kelvin1337
