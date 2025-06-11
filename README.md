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
End-To-End-DSProject/
│
├── .github/
│   └── workflows/
│       └── .gitkeep             # Placeholder to keep directory in Git
│
├── config/
│   └── config.yaml              # Main configuration file
│
├── params.yaml                  # Hyperparameters/config
├── schema.yaml                  # Schema for validation or target column info
│
├── main.py                      # Entry point to run the pipeline
├── Dockerfile                   # For Docker containerization
├── setup.py                     # For packaging the project
│
├── research/
│   └── reasearch.ipynb          # For EDA / experimentation
│
├── templates/
│   └── index.html               # Template for web interface (Flask/FastAPI)
│
├── src/
│   └── datascience/
│       ├── __init__.py
│       │
│       ├── components/          # Data ingestion, transformation, etc.
│       │   └── __init__.py
│       │
│       ├── utils/               # Helper functions
│       │   ├── __init__.py
│       │   └── common.py
│       │
│       ├── config/              # Config management logic
│       │   ├── __init__.py
│       │   └── configuration.py
│       │
│       ├── pipeline/            # Stage-wise pipeline execution
│       │   └── __init__.py
│       │
│       ├── entity/              # Configuration data classes
│       │   ├── __init__.py
│       │   └── config_entity.py
│       │
│       └── constants/           # Constants (e.g., schema paths)
│           └── __init__.py
