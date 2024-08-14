# Text Summarization Model Documentation

## Overview
This document provides a comprehensive overview of the text summarization model designed to condense lengthy documents into concise summaries. The model leverages advanced natural language processing techniques to capture the core information and essence of the text.

## Project Workflow
The project is structured into multiple components, each responsible for a different stage of the machine learning pipeline:
- **Configuration Management**: Configuration files are managed under the `src/entity` folder. These configurations include document and variable types sourced from `config.yaml`, and training arguments derived from `param.yaml`.
- **Data Pipeline**:
  - **Data Ingestion**: The initial stage involves ingesting data which is handled by specific scripts within the `components` folder.
  - **Data Transformation**: Followed by data preprocessing and transformation to format the data suitably for training.
  - **Model Training**: The core algorithmic training happens in this stage, utilizing the processed data.
  - **Model Evaluation**: Post-training, the model's performance is evaluated through various metrics.
- **Artifacts Management**: All intermediate outputs and models are stored in the `artifacts` folder, which are then utilized across different stages of the pipeline.
- **Pipeline Execution**: The main pipeline execution is handled by `main.py`, which coordinates the flow from data ingestion to model evaluation.

## Application Interface
- **FastAPI Interface**: `app.py` is responsible for providing a user interface using FastAPI, allowing users to interact with the model through a web interface.

## Deployment
- **EC2 Deployment**: The model is deployed on an AWS EC2 instance, leveraging GitHub workflows for continuous integration and deployment processes.

## Folder Structure
- **src/**: Contains the source code for the model and pipeline.
  - **entity/**: Stores the configuration files generated with the help of (`config.yaml`, `param.yaml`).
  - **config/**: Uses entity info to return the correct configuration for further development purposes.
  - **components/**: Includes configuration functions for each stage.
  - **pipeline/**: Includes separate scripts for each pipeline stage.
- **artifacts/**: Directory for storing processed data and model artifacts.
- **main.py**: Main script for running the complete pipeline.
- **app.py**: Script for the FastAPI interface.

## Conclusion
This text summarization model is designed to efficiently process and summarize large volumes of text, providing a valuable tool for information management and decision-making.

## Additional Notes
- Ensure all dependencies are installed as per the requirements.txt file.
- Review the README.md for detailed instructions on setting up and running the project.

