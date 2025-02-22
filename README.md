# 🚀 CI/CD Pipeline Setup & Deployment  

This repository demonstrates a CI/CD pipeline for two services:  

1. **Versioning API** (basic-versioning/)  
2. **Sensor API** (sensor-api/)  



## 📌 Features  
✅ Linting with **flake8**  
✅ Unit Testing with **pytest**  
✅ Building & Pushing Docker Images to **DockerHub**  
✅ Managing Secrets (**GitHub Secrets** for API Keys & DockerHub)  
✅ Continuous Integration (**CI**) using **GitHub Actions**  



## 📌 1. Prerequisites  
Ensure you have:  

✅ **Git** installed  
✅ **Docker** installed & running  
✅ **Python 3.12+** installed  
✅ **GitHub repository** with Actions enabled  



## 🔐 2. Setting Up GitHub Secrets  
We use **GitHub Secrets** to store sensitive information like **DockerHub credentials** and the **OpenWeather API key**.  

### ➡️ Steps to Add Secrets:  
1. Go to your **GitHub repository**.  
2. Click on **Settings → Secrets and variables → Actions**.  
3. Click **New repository secret** and add the following:  

   - **DOCKER_USERNAME** → *(Your DockerHub username)*  
   - **DOCKER_PASSWORD** → *(Your DockerHub password or access token)*  
   - **OPENWEATHER_API_KEY** → *(Your OpenWeather API key)*  



## 📌 3. Project Setup  

➡️ **Clone the Repository**  
➡️ **Install Dependencies**  



## 📌 4. Docker Setup  
Each service has its own **Dockerfile**.  

➡️ **Create Dockerfile** for **Versioning API** (`basic-versioning/Dockerfile`)  
➡️ **Create Dockerfile** for **Sensor API** (`sensor-api/Dockerfile`)  



## 📌 5. CI/CD Workflow (GitHub Actions)  
The **CI pipeline** includes:  

✅ **Linting (flake8)** – Ensures code quality.  
✅ **Unit Testing (pytest)** – Runs automated tests.  
✅ **Building & Pushing Docker Images** – Deploys images to **DockerHub**.  



### ➡️ How to Trigger the Pipeline  
The pipeline **runs automatically** on every **push** or **pull request** to `main`.  
You can also **manually trigger** it from the **GitHub Actions tab**.  

### ➡️ How to Check CI/CD Status  
Go to **GitHub → Actions tab** to view the **pipeline logs** and **debug failures**.  
