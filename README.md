[![Deploy Application Docker Image to EC2 instance](https://github.com/ashaduzzaman-sarker/MLOps/actions/workflows/aws.yaml/badge.svg)](https://github.com/ashaduzzaman-sarker/MLOps/actions/workflows/aws.yaml)

# MLOps: Production-Ready Machine Learning Project 🚀

This repository presents a **comprehensive production-ready machine learning workflow** for predicting **US Visa Approval**. It implements cutting-edge **MLOps principles**, ensuring scalability, reproducibility, and efficient deployment. The project incorporates automated pipelines for data ingestion, validation, transformation, model training, and deployment, with robust CI/CD practices and cloud-native integrations.

---

## 🚀 Key Highlights

### End-to-End Workflow
- **Automated Data Pipelines**:
  - Seamless ingestion from AWS S3 and MongoDB.
  - Data validation with schema enforcement and transformation for downstream processes.
  - Data drift detection using EvidentlyAI for monitoring and maintaining model reliability.

- **Model Development**:
  - Comprehensive exploratory data analysis (EDA) and feature engineering.
  - Robust model training pipeline with integrated evaluation and hyperparameter optimization.
  - Drift analysis and periodic re-training mechanisms to mitigate performance degradation.

- **Cloud-Native Deployment**:
  - Dockerized ML application with efficient deployment to AWS EC2.
  - Continuous Integration and Continuous Deployment (CI/CD) using GitHub Actions.
  - Secure artifact storage and retrieval with AWS Elastic Container Registry (ECR).

- **Interactive Web Application**:
  - A user-friendly Flask application for real-time predictions.
  - Deployed on AWS EC2 with a fully responsive and visually appealing frontend.

---

## 🛠️ Tech Stack

- **Programming**: Python, Flask
- **Libraries**: Scikit-learn, EvidentlyAI, Pandas, NumPy
- **Tools**:
  - **Cloud**: AWS S3, ECR, EC2
  - **Database**: MongoDB
  - **Containerization**: Docker
  - **CI/CD**: GitHub Actions
  - **Version Control**: Git
- **Visualization**: Matplotlib, Seaborn

---

## 📂 Repository Structure

```
├── .github/workflows
│   └── aws.yaml           # CI/CD workflow configuration
├── notebooks              # EDA and feature engineering scripts
│   ├── 1_EDA_US_visa.ipynb
│   ├── 2_Feature_Engineering_and_Model_Training.ipynb
│   └── data_drift_demo_evidently.ipynb
├── us_visa                # Core machine learning components
│   ├── components         # Modular pipeline components
│   ├── configuration      # Cloud and database configurations
│   ├── entity             # Schema definitions and configuration entities
│   ├── logger             # Logging utilities
│   ├── pipeline           # Training and prediction pipeline logic
│   ├── utils              # Helper utilities and functions
├── static/css             # CSS for the Flask web app
├── templates              # HTML templates for the web app
├── Dockerfile             # Docker configuration file
├── requirements.txt       # Python dependency list
└── app.py                 # Flask application for serving predictions
```

---

## 📊 Workflow Breakdown

### Data Pipeline Overview
1. **Data Ingestion**:
   - Fetches data from cloud storage and MongoDB.
   - Handles missing values and raw data validation.

2. **Data Validation**:
   - Ensures data consistency and integrity using schema checks.

3. **Data Transformation**:
   - Prepares data for training with feature engineering.

4. **Model Training**:
   - Trains and validates the model using automated pipelines.

5. **Model Evaluation**:
   - Evaluates model performance using advanced metrics.

6. **Model Deployment**:
   - Deploys trained models with real-time monitoring.

### Deployment Workflow
1. **Dockerization**:
   - Builds a containerized version of the application.
   - Stores Docker images in AWS ECR.

2. **Cloud Deployment**:
   - Deploys the Dockerized application to an AWS EC2 instance.
   - Automated CI/CD with GitHub Actions ensures streamlined updates.

3. **Monitoring**:
   - EvidentlyAI integration provides drift detection and performance monitoring.

---

## 🔧 Setup Instructions

### Prerequisites
- Python 3.8 or later
- AWS account with S3, EC2, and ECR access
- MongoDB Atlas account

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/MLOps-Production-Ready-Project.git
   cd MLOps-Production-Ready-Project
   ```

2. **Create a Virtual Environment**:
   ```bash
   conda create -n visa python=3.8 -y
   conda activate visa
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**:
   ```bash
   export MONGODB_URL="mongodb+srv://<username>:<password>@cluster..."
   export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
   export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

---

## 🌐 Deployment

### AWS Deployment Steps
1. **Build Docker Image**:
   ```bash
   docker build -t usvisa-app .
   docker tag usvisa-app:latest <ECR_URI>
   docker push <ECR_URI>
   ```

2. **Launch EC2 Instance**:
   - Pull Docker image from ECR.
   - Run the application in a container.

3. **CI/CD with GitHub Actions**:
   - Automate builds and deployments with `aws.yaml`.
   - Configure secrets in GitHub for secure AWS integration.

---

## 🖼️ Visual Insights

### Workflow Diagrams
- **Data Ingestion**:
  ![Data Ingestion](flowcharts/Data%20Ingestion.png)
- **Model Training**:
  ![Model Training](flowcharts/Model%20Trainer.png)
- **Complete Folder Structure**:
  ![Folder Structure](flowcharts/folder%20structure.png)

---

## 🔍 References

- **Dataset**: [US Visa Dataset](https://www.kaggle.com/datasets/moro23/easyvisa-dataset)
- **Tools**:
  - [EvidentlyAI](https://www.evidentlyai.com/)
  - [MongoDB Atlas](https://account.mongodb.com/account/login)

---

## 🙌 Acknowledgments

This project demonstrates the power of **MLOps** for creating scalable and production-ready ML applications. Contributions, feedback, and collaborations are always welcome to enhance the robustness of the solution.

**Let's innovate together! 🚀**
