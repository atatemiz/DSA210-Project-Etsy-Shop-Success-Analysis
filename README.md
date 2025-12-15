# 💰 DSA210 Project – Etsy Shop Success Analysis  
Spring 24–25 · DSA210 Term Project  

---

## 📝 Project Overview

This project studies Etsy shops and their products to understand what “success” looks like on the platform.

Using two publicly available datasets from Kaggle (one at shop level, one at item level), I:

- Clean and combine the data,
- Create new, more informative features,
- Explore distributions and relationships with visualizations,
- Investigate three concrete statistical hypotheses about shop success and price levels.

The final goal is to turn raw marketplace data into interpretable insights that could guide a small Etsy seller.

---

## 🎯 Motivation

Etsy is widely used by:

- Designers and artists  
- 3D-print and handmade product makers  
- Digital product and print-on-demand sellers  

New sellers usually have questions such as:

- How many products should I list?
- Do reviews and engagement per product matter as much as the total number of products?
- How do my price levels relate to performance?

This project aims to answer:

- Whether larger shops really perform better,
- Whether engagement quality (reviews per product) differentiates successful shops,
- Whether item price can be linked to product popularity in a statistically meaningful way.

---

## 📂 Datasets Used

### 1️⃣ Etsy Shops (shop-level dataset)
- Source: Kaggle – “Etsy Shops Dataset” by Sepideh Doost  
- Approx. 20,000 shops opened in November–December 2019  
- Example information:  
  - Number of active listings per shop  
  - Total number of reviews  
  - Favourites, sales counts  
  - Shop location, creation date, and a shop identifier  

### 2️⃣ Etsy Items Price (item-level dataset)
- Source: Kaggle – “Etsy Items Price” by dimakyn  
- Product-level records with:  
  - Product title  
  - Shop name  
  - Item price  
  - Number of favourites  

The shop dataset describes the “storefront”, while the item dataset focuses on individual products and their prices.  
They are used together to answer both shop-level and price-level questions.

**Etsy Shops Dataset** – Kaggle  
Author: Sepideh Doost  
Link: https://www.kaggle.com/datasets/sepidafs/etsy-shops  

**Etsy Items Price** – Kaggle  
Author: dimakyn  
Link: https://www.kaggle.com/datasets/dimakyn/etsy-items-price  

---

## 🛠️ Feature Engineering (What I Built From the Raw Data)

### From the shop dataset:

- **Shop size**  
  The number of active listings is used as a measure of how large a shop is.

- **Engagement per product**  
  For each shop, the total number of reviews is divided by the number of active listings,  
  resulting in “reviews per listing”. Shops with zero listings are handled carefully to avoid
  invalid divisions.

- **Success label for shops**  
  A shop is marked as “successful” if it has at least one review.  
  Shops with no reviews are treated as “non-successful”.

### From the item dataset:

- **Clean numeric prices**  
  Prices are converted into numeric values and rows with invalid or missing prices are removed.

- **Price-based segments**  
  The 75th percentile of the price distribution is used to define a “high-price” segment,  
  while the remaining items form a “low-price” segment.  
  This segmentation is used to explore price-level differences.

---

## 📊 Exploratory Data Analysis

Key observations from the visual exploration include:

- **Highly skewed shop characteristics**  
  Most shops have very few listings and zero reviews, while a small fraction of shops
  accumulates many products and substantial feedback.

- **Relationship between listings and reviews**  
  A log–log scatter plot shows a clear positive association between shop size and total
  reviews, although variability remains high.

- **Item price distribution**  
  Item prices are concentrated in a lower range with a long tail of higher-priced items,
  motivating the use of price-based segmentation.

---

## 🧪 Hypothesis Tests and Findings

Three hypotheses are investigated using statistical analysis.  
For the first two hypotheses, two-sample Welch t-tests are applied.  
For the third hypothesis, exploratory analysis revealed limitations in the item-level
popularity variable, which affected the choice of statistical testing.

---

### Hypothesis 1 – Shop Size vs Success

**Question**  
Do shops that receive at least one review tend to list more products than shops with no reviews?

**Result**  
The Welch t-test produces a very small p-value, leading to rejection of the null hypothesis.  
Successful shops have significantly more active listings on average.

---

### Hypothesis 2 – Engagement per Listing vs Success

**Question**  
Do successful shops receive more reviews per listing than shops with no reviews?

**Result**  
The Welch t-test again yields a very small p-value.  
Successful shops not only have more products, but also receive higher engagement per product.

---

### Hypothesis 3 – Item Price vs Popularity

**Question**  
Is item price associated with item popularity?

**Data limitation**  
Exploratory analysis revealed that the *favourite* variable in the item-level dataset has
**zero variance across all items**. Because the popularity metric is constant, it does not
carry usable information.

**Conclusion**  
Due to insufficient variability in the popularity metric, it is not statistically valid
to perform group-based hypothesis testing or correlation analysis.  
Therefore, **Hypothesis 3 is rejected**, as no meaningful relationship between item price and
popularity can be evaluated using this dataset.

---

## 📌 Overall Insights

1. **Shop size matters**  
   Shops that receive at least one review tend to have many more active listings.

2. **Engagement per product matters**  
   Successful shops achieve higher reviews per listing, indicating that visibility,
   quality, or marketing of products is important in addition to sheer volume.

3. **Item popularity could not be evaluated**  
   Although item prices show a clear distribution, the available popularity indicator
   (favourites) lacks variability. As a result, no statistically valid conclusion can be
   drawn about the relationship between item price and popularity.

---

## 🧰 Tools Used

- Python (data cleaning, feature engineering, visualization, statistics)  
- Jupyter Notebook / VS Code Jupyter  
- Git and GitHub  

---

## 📁 Repository Contents

- Jupyter notebook containing the full analysis  
- Shop-level dataset file  
- Item-level dataset file  
- This README explaining the project, methods, and findings  

---

## 🤝 AI Assistance Disclosure

The structure and wording of this README were prepared with the help of an AI assistant
(OpenAI ChatGPT). All dataset choices, feature definitions, statistical tests, and final
interpretations were implemented and verified by the project owner.
