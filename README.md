# Sustainable Crop Recommendation Using Hybrid ML-XAI Techniques in Precision Agriculture 🌱

This repository presents a Smart Crop Recommendation System that integrates Machine Learning (ML) with Explainable Artificial Intelligence (XAI) for sustainable and precision-driven agriculture. By combining robust ML models with model-agnostic interpretability techniques, this project aims to assist farmers, agronomists, and agricultural planners in making accurate, data-driven crop choices—especially critical under changing climatic conditions.

---

## 🚀 Project Highlights

- **Hybrid ML-XAI Model**: Combines supervised ML algorithms with Permutation Feature Importance (PFI) for interpretability.
- **Feature Reduction**: Input features reduced from 22 to 7 without compromising accuracy.
- **High Accuracy**: Gaussian Naïve Bayes (GNB) model achieved 99.55% accuracy on test data.
- **Web App Deployment**: A Flask-based web interface that provides real-time crop recommendations with visual explanations.
- **Explainability First**: Integrates interpretable outputs to foster trust among non-technical users.

---

## 📌 Problem Statement

Traditional crop selection relies heavily on intuition, past experience, or limited agronomic advice. This often results in:

- Suboptimal yields
- Inefficient resource use
- Economic losses for farmers

The proposed Smart Crop Recommendation System (SCRS) overcomes these limitations by using data-driven decisions with transparent, explainable logic.

---

## 📊 Dataset

- **Source**: Kaggle Smart Farming Data 2024 (SF24)
- **Records**: 2,200 instances
- **Features**: 22 soil, climate, and agricultural parameters including:
  - Nitrogen, Phosphorus, Potassium
  - Temperature, Rainfall, Humidity
  - pH, Soil Moisture, Sunlight, Wind Speed
  - Fertilizer Use, Pest Pressure, Irrigation Frequency

---

## 🔍 Methodology

1. **Data Preprocessing**: Label encoding, Min-Max normalization, and train-test split (80/20).
2. **XAI Feature Selection**:
   - Used **Permutation Feature Importance** to select top 7 impactful features.
3. **Model Training**:
   - Six classifiers: Logistic Regression, Naïve Bayes, SVC, KNN, Decision Tree, Random Forest.
   - Performance compared with and without feature selection.
4. **Evaluation Metrics**:
   - Accuracy, Precision, Recall, F1-Score, Confusion Matrix
5. **Deployment**:
   - Flask-based application for easy accessibility.

---

## 🧠 Model Performance

### 🔹 Without XAI (All 22 Features)

| Model               | Accuracy | Precision | Recall | F1-Score |
|---------------------|----------|-----------|--------|----------|
| Naïve Bayes         | 99.09%   | 99.20%    | 99.09% | 99.10%   |
| Random Forest       | 99.09%   | 99.20%    | 99.09% | 99.10%   |
| Decision Tree       | 98.86%   | 98.90%    | 98.86% | 98.86%   |
| Logistic Regression | 84.32%   | 86.49%    | 84.32% | 83.81%   |
| SVC                 | 80.23%   | 81.44%    | 80.23% | 80.18%   |
| KNN                 | 32.95%   | 37.64%    | 32.95% | 33.14%   |

### 🔹 With XAI (Top 7 Features via PFI)

| Model               | Accuracy | Precision | Recall | F1-Score |
|---------------------|----------|-----------|--------|----------|
| **Naïve Bayes**     | **99.55%** | 99.58%  | 99.55% | 99.54%   |
| Random Forest       | 99.32%   | 99.37%    | 99.32% | 99.32%   |
| Decision Tree       | 98.18%   | 98.24%    | 98.18% | 98.18%   |
| Logistic Regression | 91.82%   | 93.44%    | 91.82% | 91.72%   |
| SVC                 | 96.82%   | 97.30%    | 96.82% | 96.82%   |
| KNN                 | 97.05%   | 97.44%    | 97.05% | 97.05%   |

---

## 🌐 Web Application

- Built using Flask
- Users input 7 optimized features
- Returns crop prediction with visual explanation
- Designed for ease-of-use by farmers and agriculture officers

---

