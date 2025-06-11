# End-To-End Data Science Project

# Workflows- MLPipeline
1.DataIngestion
2.Data Validation
2.Data Transformation
3.Model Training
4.Model Evaluation

# Workflows
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration ins rc config
6. Update th ecomponents
7. Update the pipeline
8. Update  the main.py



Project-Architecture
```
End-To-End-DSProject/
│
├── .github/
│   └── workflows/
│       └── .gitkeep
│
├── config/
│   └── config.yaml
│
├── params.yaml
├── schema.yaml
├── main.py
├── Dockerfile
├── setup.py
│
├── research/
│   └── reasearch.ipynb
│
├── templates/
│   └── index.html
│
└── src/
    └── datascience/
        ├── __init__.py
        │
        ├── components/
        │   └── __init__.py
        │
        ├── utils/
        │   ├── __init__.py
        │   └── common.py
        │
        ├── config/
        │   ├── __init__.py
        │   └── configuration.py
        │
        ├── pipeline/
        │   └── __init__.py
        │
        ├── entity/
        │   ├── __init__.py
        │   └── config_entity.py
        │
        └── constants/
            └── __init__.py

```
