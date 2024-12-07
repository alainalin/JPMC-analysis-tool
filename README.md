# **JPMC6: Company Relationship Analysis Tool**

## **Project Overview**
The Company Relationship Analysis Tool is an AI-driven project that leverages historical stock price movements to uncover relationships between US companies. We experiment with clustering companies based on industry sectors and stock price correlations, for stock price movements predictions with the hope of improving accuracy and uncovering inter-company relationships.

### **Objectives and Goals**
- **Identify Intercompany Relationships**: Highlight partnerships, shared dependencies, or financial risks.
- **Enhance Stock Price Prediction**: Use advanced clustering and regression techniques to refine predictions.
- **Visualize Relationships**: Employ heatmaps and hierarchical clustering dendrograms to represent correlations and relationships.
- **Business Impact**:
  - **Investment Insights**: Detect partnerships and acquisition opportunities.
  - **Risk Mitigation**: Uncover vulnerabilities in shared dependencies.
  - **Market Expansion**: Facilitate partnerships or mergers.
  - **Customer Insights**: Identify shared customer bases for targeted marketing.
  - **Crisis Management**: Anticipate cascading effects during disruptions.

---

## **Methodology**
### **Data Collection and Preparation**
- **Data Source**: Historical stock price data from Yahoo Finance for all S&P 500 companies.
- **Time Period**: 4 years of data (September 2020 - September 2024).
- **Features**:
  - Daily percent returns calculated to capture relative price movements.
- **Preprocessing**:
  - Aggregated data into prices, volume, and daily returns.
  - Removed rows with NaNs to ensure data integrity.

### **Analysis Techniques**
1. **Heatmaps**:
   - Created absolute correlation heatmaps to visualize similarities between companies.
   - Generated dissimilarity heatmaps to explore distances between company clusters.

2. **Hierarchical Clustering**:
   - Used dissimilarity matrices and various linkage methods (e.g., single, complete, ward) to form clusters.
   - Visualized clusters with dendrograms to understand company relationships.

3. **Silhouette Analysis**:
   - Evaluated cluster quality by measuring cohesion and separation.
   - Experimented with different numbers of clusters and linkage methods for optimal results.

### **Modeling**
- **Baseline Model**: Predicts the mean of the training set.
- **XGBoost Models**:
  - 3 statregies:
    - Trained on all companies and all stock data.
    - Trained a model per cluster (companies clustered by their industry).
    - Trained a model per cluster (companies clustered by hierarchical clustering).  
  - Used Monday-Thursday data as features to predict Friday returns.

---

## **Results and Key Findings**
- **Heatmap Insights**:
  - Companies within the same sector (e.g., technology, healthcare) show higher correlations.
  - Cross-sector relationships highlight unique interdependencies.

- **Clustering Performance**:
  - **Hierarchical Clustering**:
    - Dendrograms provided a detailed view of intercompany relationships.
    - Optimal clusters identified using silhouette analysis.
  - **Industry-Based Clustering**:
    - Produced intuitive results but lacked predictive improvement.

- **Model Evaluation**:
  - **Baseline Model**:
    - RMSE: 4.605
  - **No Clustering**:
    - RMSE: 1.797, R²: 0.85
  - **Sector-Based Clustering**:
    - Average RMSE: 1.786, R²: 0.833
  - **Hierarchical Clustering**:
    - RMSE: 1.779, R²: 0.453

**Key Insight**: While clustering provided valuable insights into company relationships, it did not significantly improve predictive accuracy. The simplest model (no clustering) performed best overall.

---

## **Potential Next Steps**
1. **Model Improvements**:
   - Fine-tune and train the no-clustering model further.
   - Experiment with LightGBM and CatBoost for faster training and improved accuracy.
2. **Enhanced Data Integration**:
   - Incorporate news and social media sentiment analysis.
   - Implement dynamic retraining with updated data.
3. **User Interaction**:
   - Develop interactive interfaces for analysts, including "what-if" scenario tools and company relationship visualization.

---

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Methodology](#methodology)
3. [Results and Key Findings](#results-and-key-findings)
4. [Potential Next Steps](#potential-next-steps)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Contributing](#contributing)
8. [License](#license)
9. [Credits and Acknowledgments](#credits-and-acknowledgments)

---

## Installation

### Prerequisites

- Python 3.8+
- Jupyter Notebook
- Required libraries: 
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`
  - `xgboost`
  - `yfinance`

### Step-by-Step Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url.git
   cd your-repo-folder

2. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`

3. Install dependencies: 
   ```bash
   pip install -r requirements.txt

4. Launch Jupyter Notebook: 
   ```bash
   jupyter notebook

---

## Usage

### Preprocessing Data
1. Open `preprocess.ipynb` and follow the steps to preprocess stock price data.
2. Ensure you use Yahoo Finance or other APIs for downloading historical stock price data.

### Exploratory Analysis
1. Use `matrices_and_heatmaps.ipynb` for exploratory data analysis.
2. Visualize correlation matrices and hierarchical clusters.

### Model Training
1. Train models using:
   - `naive_xgboost.ipynb` for a single model on all data.
   - `task3a-linkage-silhouette.ipynb` to experiment with clustering methods and silhouette analysis.
2. Evaluate model performance using RMSE and R² metrics.

### Results Interpretation
1. Visualize and analyze results from clustering and XGBoost models in `task2_matrices_and_heatmaps_with_task3a.ipynb`.

---

## License

Apache License 2.0

---

## Credits and Acknowledgments

### Team Members
- **Sara Deshmukh** (Rutgers University - New Brunswick)  
- **Victoria Kim** (Virginia Tech)  
- **Alaina Lin** (Brown University)  
- **Chelsey Parker** (Georgia State University)  
- **Raj Rana** (Stevens Institute of Technology)  

### Advisors
- **Kassie Papasotiriou**  
- **Annita Vapsi**  
- **Antony Papadimitriou**  

### Teaching Assistants
- **Samy Lokanandi**  
- **Jesse Dylan Ward**  

### Tools and Libraries
- **Yahoo Finance API**: For retrieving historical stock price data.  
- **Python Libraries**:  
  - `pandas`: Data manipulation and analysis.  
  - `numpy`: Numerical computing.  
  - `scikit-learn`: Machine learning and data

---


   
