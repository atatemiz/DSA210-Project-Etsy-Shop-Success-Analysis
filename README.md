# 💰 DSA210 Project – Etsy Shop Success Analysis  
Spring 24–25 · DSA210 Term Project  - Şefik Ata Temiz

---

## 📝 Project Overview

This project studies Etsy shops and their products to understand what “success” looks like on the platform.

Using two publicly available Etsy-related datasets from Kaggle (one at **shop level**, one at **item level**), I:

- Clean and preprocess raw marketplace data,
- Engineer informative features at both shop and item level,
- Explore distributions and relationships using visualizations,
- Investigate three concrete statistical hypotheses related to shop success and item pricing,
- Train supervised ML models to predict shop success from **leak-free shop features**.

The final goal is to transform raw Etsy marketplace data into interpretable insights that could guide small and independent Etsy sellers.

---

## 🎯 Motivation

Etsy is widely used by:

- Designers and artists  
- 3D-print and handmade product makers  
- Digital product and print-on-demand sellers  

New sellers commonly ask:

- How many products should I list?
- Does engagement per product matter as much as total shop size?
- Is there a relationship between item prices and product popularity?
- Can we predict whether a shop will be “successful” using only early, non-leaky shop signals?

This project aims to answer:

- Whether larger shops tend to be more successful,
- Whether engagement quality differentiates successful shops,
- Whether item price can be linked to item popularity in a statistically meaningful way,
- How well ML models can classify successful vs non-successful shops.

---

## 📂 Datasets Used

### 1️⃣ Etsy Shops (shop-level dataset)
- **Source:** Kaggle – *“Etsy Shops Dataset”* by Sepideh Doost  
- **Scope:** ~20,000 shops opened in November–December 2019  
- **Example attributes:**  
  - `listing_active_count` (active listings)  
  - `review_count`  
  - `sales_count`  
  - `num_favorers`  
  - `is_shop_us_based`  
  - `creation_date`, `shop_location`, etc.

**Link:**  
https://www.kaggle.com/datasets/sepidafs/etsy-shops  

---

### 2️⃣ Etsy Items (item-level dataset)
- **Source:** Kaggle – Etsy item listings dataset (scraped)  
- **Scope:** Individual product-level observations  
- **Columns used in this project:**  
  - `cost` (item price)  
  - `crowd` (item popularity proxy)  
  - `store`, `listing` identifiers  
  - (`review` may exist in some versions, but this project uses the columns above)

> Note: The item dataset used in this repository includes the columns:
> `listing`, `cost`, `store`, `review`, `crowd`.  
> For Hypothesis 3, **popularity is represented by `crowd`**.

---

## 🛠️ Feature Engineering

### Shop-level features

- **Shop size**  
  Defined as the number of active listings (`listing_active_count`).

- **Engagement per product (EDA / stats only)**  
  Computed as `review_count / listing_active_count` (reviews per listing), with safe handling of zeros.

- **Shop success label**  
  A shop is labeled **successful** if it has at least one review (`review_count > 0`), otherwise **non-successful**.

### Item-level features

- **Clean numeric prices**  
  Item prices (`cost`) are converted to numeric format and invalid entries are removed.

- **Popularity measure**  
  Item popularity is measured using `crowd`.

---

## 📊 Exploratory Data Analysis

Key observations include:

- **Strong skewness in shop activity**  
  Most shops have few listings and no reviews, while a small subset accumulates substantial engagement.

- **Shop size vs reviews**  
  Log–log scatter plots show that larger shops tend to receive more reviews.

- **Item-level variation**  
  Item prices (`cost`) and popularity (`crowd`) exhibit meaningful variability, supporting valid statistical analysis.

---

## 🧪 Hypothesis Tests and Findings

Three hypotheses are investigated.

Welch two-sample t-tests are used where group comparisons are appropriate.  
For monotonic relationships, non-parametric correlation is applied.

---

### Hypothesis 1 – Shop Size vs Success

**Question**  
Do shops that receive at least one review tend to list more products?

**Method**  
Welch two-sample t-test on `listing_active_count` between:
- successful shops (`review_count > 0`)  
- non-successful shops (`review_count == 0`)

**Result**  
The Welch t-test yields a very small p-value. The null hypothesis is rejected.

**Conclusion**  
Successful shops have significantly more active listings on average.

---

### Hypothesis 2 – Engagement per Listing vs Success

**Question**  
Do successful shops receive more reviews per listing?

**Method**  
Welch two-sample t-test on `reviews_per_listing` between:
- successful vs non-successful shops

**Result**  
The Welch t-test again yields a very small p-value.

**Conclusion**  
Successful shops not only have more products, but also higher engagement per product on average.

---

### Hypothesis 3 – Item Cost vs Popularity (Crowd)

**Question**  
Is item price associated with item popularity?

**Method**  
Spearman rank correlation between:
- `cost` (price)
- `crowd` (popularity proxy)

**Result (from the notebook output)**  
- Spearman correlation ≈ **-0.028**
- p-value ≈ **0.169**
- Decision: **Fail to reject H₀** at α = 0.05

**Conclusion**  
Using this item dataset and popularity proxy (`crowd`), there is **no statistically significant monotonic association** between item cost and popularity.

---

## 🤖 Machine Learning Methods (Shop Success Prediction)

In addition to hypothesis testing, supervised ML models are trained to predict **shop success**.

### Target (Label)
- `success_label = 1` if `review_count > 0`, else `0`.

### Leak-Free Feature Set (used for ML)
To avoid target leakage, the ML models use only non-leaky shop features:
- `listing_active_count` (shop size)
- `sales_count` (if available)
- `num_favorers` (if available)
- `is_shop_us_based` (if available)

> Important: Features derived from reviews (e.g., `review_count`, `reviews_per_listing`) are **not used** as ML inputs, since they directly define or strongly encode the target.

### Training & Evaluation
- Stratified train/test split (e.g., 75/25) due to class imbalance.
- Baseline: `DummyClassifier(most_frequent)`
- Models trained (balanced class weights where applicable):
  - Logistic Regression
  - SVM (RBF kernel)
  - Decision Tree
  - Random Forest

### Metrics Reported
Because the dataset is imbalanced, evaluation includes:
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

### Observed Performance (example)
The baseline classifier achieves high accuracy by predicting the majority class, but **F1 and recall are poor** for the minority (successful) class.  
Class-weighted models improve minority-class detection and yield stronger ROC-AUC, demonstrating that success prediction is feasible beyond the trivial baseline.

---

## 📌 Overall Insights

1. **Shop size matters**  
   Larger shops are significantly more likely to receive reviews.

2. **Engagement quality matters**  
   Successful shops achieve higher engagement per product, not just higher volume.

3. **Item cost vs popularity is not significant (with `crowd`)**  
   In this dataset, item cost does not show a statistically significant association with popularity.

4. **ML can predict shop success beyond baseline**  
   When evaluated with imbalance-aware metrics (F1, ROC-AUC), trained models perform meaningfully better than the “most frequent” baseline.

---

## 🧰 Tools Used

- Python (pandas, NumPy, SciPy, matplotlib, scikit-learn)  
- Jupyter Notebook / VS Code Jupyter  
- Git and GitHub  

---

## 📁 Repository Contents

- Jupyter notebook with the full analysis and outputs  
- Shop-level Etsy dataset  
- Item-level Etsy dataset  
- This README file  

---

## 🤝 AI Assistance Disclosure

The structure and wording of this README were prepared with the assistance of an AI tool (OpenAI ChatGPT).  
All dataset selection, feature engineering, statistical testing, model training, and interpretations were implemented and verified by the project owner.
