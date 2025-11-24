# 📊 DSA210 Project – Etsy Shop Success Analysis

· DSA210 Term Project  

---

## 🧩 Project Overview

This project analyzes **Etsy shops** using publicly available datasets (mainly from Kaggle) to understand what makes a shop **“successful”**.

We focus on **shop-level** and (optionally) **listing-level** attributes such as:

- Shop age  
- Number of listings  
- Ratings & reviews  
- Price levels  
- Digital vs physical / print-on-demand products  

Our goal is to uncover patterns that can help **independent creators** and **small businesses** make better strategic decisions when starting or growing an Etsy shop.

---

## 💡 Motivation

Etsy is a key platform for:

- Designers, artists, 3D-print makers  
- Digital product creators (posters, printables, templates)  
- Print-on-demand sellers  

But most new sellers have no clear idea **which factors actually matter** for success.

This project aims to:

- 🔍 Identify key attributes associated with higher sales / engagement  
- 🧬 Compare **niche-focused** vs **general** shops  
- 🤖 Build simple models that estimate a shop’s success likelihood based on its metadata  

---

## 🎯 Main Research Questions

### 1️⃣ Shop-Level Success

- Which features (shop age, number of listings, ratings, reviews, country, etc.) are most related to **high-performing** shops?
- Do **niche shops** (focused on a small set of categories) outperform **general shops**?

### 2️⃣ Products & Pricing

- How do **average product price** and **price range** relate to shop success?
- Are shops that mainly sell **digital / print-on-demand** products more successful than those focused on **physical** items?

### 3️⃣ Predictive Aspect

- Can we predict whether a shop will be **“successful”** (e.g., top X% by sales / favorites / reviews) using only basic shop metadata?
- Which features are most important in this prediction?

---

## 🧪 Hypotheses & Approach

**Null Hypothesis (H₀)**  
There is **no significant relationship** between shop-level features (e.g., age, listing count, digital share, ratings) and Etsy shop success metrics.

**Alternative Hypothesis (H₁)**  
Certain shop-level features have a **significant impact** on Etsy shop success.

**General Approach:**

1. **EDA (Exploratory Data Analysis)**  
   - Inspect distributions, outliers, missing values  
   - Compare feature distributions between successful vs non-successful shops  

2. **Statistical Testing**  
   - Use t-tests / non-parametric tests to check group differences  
   - Correlation analysis between numeric features and success metrics  

3. **Machine Learning**  
   - Train simple models to **classify** or **predict** success  
   - Interpret feature importance and connect back to real-world insights  

---

## 📂 Dataset Description

We plan to use one primary **shop-level** dataset and optionally a **listing-level** dataset from Kaggle, such as:

- **Etsy Shops (≈400K shops)** – large-scale dataset with shop metadata  
- **Etsy Shops (≈20K shops)** – smaller, cleaner version with detailed shop info  
- **Etsy Listings** – listing-level data (titles, descriptions, prices, reviews)  

> Exact dataset choice will be finalized at the implementation stage and clearly documented in the repo.

### 🏪 Example Shop-Level Features

- `shop_id` – unique shop identifier  
- `shop_name` – shop name  
- `shop_creation_date` – when the shop was opened  
- `shop_age_days / shop_age_years` – derived from creation date  
- `num_listings` – number of active listings  
- `avg_rating` – average rating (1–5)  
- `review_count` – total number of reviews  
- `sales` or `sales_proxy` – sales, favorites, or similar success indicator (dataset-dependent)  
- `country` / `location` – geographic info  
- `main_category` / `tags` – dominant product category or tags (if available)  

### 🧾 Example Listing-Level Features (Optional)

- `listing_id` – unique product identifier  
- `title`, `description` – textual info  
- `price`, `currency` – pricing  
- `favorites`, `listing_review_count` – engagement metrics  
- `is_digital` (derived) – digital / print-on-demand vs physical indicator  

---

## 🧮 Feature Engineering (Planned)

To make the models and analysis more informative, we plan to derive the following features:

- **Shop Age Bucket**  
  - e.g., `New` (< 1 year), `Growing` (1–3 years), `Established` (> 3 years)

- **Listing Intensity**  
  - `num_listings` normalized by shop age (listings per year)

- **Rating Segment**  
  - `High` (≥ 4.8), `Medium` (4.0–4.79), `Low` (< 4.0)

- **Digital Share** (if listing data used)  
  - Ratio of digital / print-on-demand listings to total listings

- **Category Focus Index**  
  - How specialized a shop is; e.g., entropy-based or share of top category

- **Price Statistics**  
  - Average price, median price, minimum, maximum, price range

- **Engagement Metrics**  
  - Reviews per listing, favorites per listing (where available)

---

## 📊 Statistical Analysis Plan

### 1️⃣ Group Comparison: Successful vs Non-Successful Shops

- Define **“successful shop”** (e.g., top 20–25% by sales / engagement metric)  
- Split dataset into:
  - **Group A:** Successful shops  
  - **Group B:** Other shops  

We will:

- Compare distributions of:
  - Shop age  
  - Number of listings  
  - Average rating & review count  
  - Digital share  
  - Category focus index  

- Use:
  - **t-test / Mann–Whitney U** for mean/median comparison  
  - **Pearson/Spearman correlation** for numeric relationships  

### 2️⃣ Visualizations

Planned plots include:

- Histograms / KDE plots for features split by success group  
- Boxplots for rating, review_count, and price statistics  
- Scatter plots (e.g., `num_listings` vs `sales_proxy`, colored by rating)  
- Correlation heatmaps for numeric features  

---

## 🤖 Machine Learning Component

### 🧩 Classification – Predicting Successful Shops

We will train simple models such as:

- **Logistic Regression**  
- **Random Forest Classifier**

**Target Variable (Example):**

- `successful_shop = 1` → shop is in top X% by sales/engagement  
- `successful_shop = 0` → otherwise  

**Input Features (Candidates):**

- Shop age & age bucket  
- Number of listings & listing intensity  
- Average rating, review_count  
- Price statistics  
- Category focus index  
- Digital share (if available)

**Evaluation Metrics:**

- Accuracy  
- Precision / Recall / F1-score  
- ROC–AUC  

---

### 📉 Optional: Regression – Predicting Sales / Engagement Score

As an extension, we may treat success as a **continuous** variable:

- Predict `sales` or a normalized engagement score using regression models  

**Metrics:**

- R² Score  
- MAE (Mean Absolute Error)  
- RMSE (Root Mean Squared Error)  

---

## 📈 Expected Outcomes

By the end of the project, we expect to:

- Identify which shop attributes are **most strongly associated** with success  
- Understand whether **niche focus** or **broad product range** tends to perform better  
- See if **digital / print-on-demand** oriented shops behave differently from physical-product shops  
- Provide a **baseline predictive model** that can estimate the success likelihood of a shop given its basic metadata  
- Summarize findings with clear **plots, tables, and explanations**  

---

## 🧰 Tech Stack

- 🐍 **Python**  
  - `pandas`, `numpy` – data handling  
  - `matplotlib`, `seaborn` – visualizations  
  - `scipy` – statistical tests  
  - `scikit-learn` – machine learning models  

- 📓 **Jupyter Notebook / Google Colab** – interactive analysis  
- 🧾 **Git & GitHub** – version control & documentation  

---

## 📦 Final Deliverables

- Cleaned and documented datasets (shop-level + optional listing-level)  
- EDA notebooks with plots and descriptive statistics  
- Statistical test results (with interpretation)  
- Machine learning models (classification and/or regression) with evaluation metrics  
- Final report / summary notebook  
- This GitHub repository with:
  - Code  
  - README  
  - Plots / figures  

---

## 🔮 Possible Future Work

- NLP on listing titles & descriptions (sentiment, keyword analysis, text length, etc.)  
- Time series analysis if temporal sales data is available  
- Advanced models (e.g., Gradient Boosting / XGBoost)  
- Interactive dashboard (e.g., **Streamlit** or **Plotly Dash**) where users can simulate hypothetical shops  

---

## 👥 Authors

Prepared by:  

- ✍️ **Şefik Ata Temiz**  


Sabancı University · DSA210 · 

---

## 🤝 AI Assistance Disclosure

Parts of this README (structure, formatting, and some wording) were created with the help of **OpenAI ChatGPT**.  
All analysis decisions, dataset selection, and implementation will be done and validated by the project team.
