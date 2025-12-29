# Kidney Disease Classification: End-to-End Deep Learning Project

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)
![DVC](https://img.shields.io/badge/DVC-945DD6?style=for-the-badge&logo=dvc&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

## Project Overview
This project is an industry-standard **Kidney Disease Classification** system that uses Deep Learning (CNNs) to analyze CT scan images and classify them as either **Normal** or **Tumor**. 

The primary goal of this repository is to demonstrate a complete **MLOps** lifecycle, ensuring that the model is not just a notebook script but a production-ready application that is versioned, tracked, and automatically deployed to the cloud.



## Key Features
- **Modular Coding:** Transitioned from Jupyter Notebook experiments to a structured Python package.
- **Data Versioning (DVC):** Tracked large datasets and model artifacts without bloating the Git repository.
- **Experiment Tracking (MLflow):** Logged all hyperparameters, metrics (accuracy/loss), and model versions for full reproducibility.
- **CI/CD Pipeline:** Automated deployment using GitHub Actions. Every "push" to the main branch builds a Docker image, pushes it to **AWS ECR**, and deploys it to an **AWS EC2** instance.
- **Containerization:** Wrapped the entire environment in **Docker** to ensure "it works on my machine" translates to "it works in production."

## Technical Stack
* **Deep Learning:** TensorFlow, Keras, CNN.
* **MLOps:** DVC, MLflow.
* **Backend:** Flask (for Web API).
* **Cloud:** AWS (EC2, ECR, S3).
* **DevOps:** Docker, GitHub Actions.

## Project Workflow
1.  **Data Ingestion:** Automatically download and unzip data.
2.  **Base Model Preparation:** Initialize VGG16 architectures with custom head layers.
3.  **Model Training:** Train on CT scan images with checkpointing.
4.  **Evaluation:** Log performance metrics to MLflow.
5.  **Deployment:** Serve the model via a Flask web app.



## Installation & Usage

### 1. Clone the repository
```bash
git clone [https://github.com/Arghya-Tech99/Kidney-Disease-Classification.git](https://github.com/Arghya-Tech99/Kidney-Disease-Classification.git)
cd kidney-disease-classification
```

### 2. Environment Setup
```bash
python -m venv venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Pipeline & Application
```bash
# To run the DVC pipeline
dvc repro

# To start the web application
python app.py
```

## Future Roadmap (Improvements)
To evolve this project into a more robust medical tool, the following enhancements are planned:
- **Explainable AI (XAI):** Integrate Grad-CAM or SHAP to generate heatmaps on CT scans. This allows doctors to see why the model predicted a tumor, increasing transparency.
- **Multi-Class Expansion:** Move beyond binary classification to identify specific types of kidney issues (Cysts, Stones, or different tumor stages).
- **Vision Transformers (ViT):** Benchmark the current CNN performance against a Vision Transformer architecture to potentially increase accuracy on complex textures.
- **Model Quantization:** Optimize the model using TensorFlow Lite or ONNX to allow for faster inference on low-power medical devices.
- **Secure API:** Implement JWT authentication to ensure only authorized medical personnel can access the prediction endpoints.
