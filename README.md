# 💰 DSA210 Project – Etsy Shop Success Analysis  
Spring 24–25 · DSA210 Term Project  

---

## 📝 Project Overview

This project studies Etsy shops and their products to understand what “success” looks like on the platform.

Using two publicly available Etsy-related datasets from Kaggle (one at shop level, one at item level), I:

- Clean and preprocess raw marketplace data,
- Engineer informative features at both shop and item level,
- Explore distributions and relationships using visualizations,
- Investigate three concrete statistical hypotheses related to shop success and item pricing.

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

This project aims to answer:

- Whether larger shops tend to be more successful,
- Whether engagement quality differentiates successful shops,
- Whether item price can be linked to item popularity in a statistically meaningful way.

---

## 📂 Datasets Used

### 1️⃣ Etsy Shops (shop-level dataset)
- **Source:** Kaggle – *“Etsy Shops Dataset”* by Sepideh Doost  
- **Scope:** ~20,000 shops opened in November–December 2019  
- **Example attributes:**  
  - Number of active listings  
  - Total review count  
  - Sales and favourites  
  - Shop creation date and location  

**Link:**  
https://www.kaggle.com/datasets/sepidafs/etsy-shops  

---

### 2️⃣ Etsy Items (item-level dataset)
- **Source:** Kaggle – Etsy item listings dataset (scraped)  
- **Scope:** Individual product-level observations  
- **Key attributes used in this project:**  
  - `cost` (item price)  
  - `review` (number of reviews, used as a popularity proxy)  
  - Store and listing identifiers  

This dataset provides sufficient variability in item popularity, allowing
statistically valid analysis of price–popularity relationships.

---

## 🛠️ Feature Engineering

### Shop-level features

- **Shop size**  
  Defined as the number of active listings.

- **Engagement per product**  
  Computed as total reviews divided by active listings
  (*reviews per listing*). Zero-listing cases are handled safely.

- **Shop success label**  
  A shop is labeled *successful* if it has at least one review;
  otherwise it is labeled *non-successful*.

### Item-level features

- **Clean numeric prices**  
  Item prices (`cost`) are converted to numeric format and invalid
  entries are removed.

- **Item popularity measure**  
  The number of reviews (`review`) is used as a proxy for item popularity.

- **Popularity-based groups**  
  Items in the top 25% by review count are labeled as *popular items*,
  while the remaining items form the comparison group.

---

## 📊 Exploratory Data Analysis

Key observations include:

- **Strong skewness in shop activity**  
  Most shops have few listings and no reviews, while a small subset
  accumulates substantial engagement.

- **Positive relationship between shop size and reviews**  
  Log–log scatter plots show that larger shops tend to receive more reviews.

- **Item-level variation**  
  Item prices and review counts exhibit meaningful variability,
  supporting statistical analysis at the product level.

---

## 🧪 Hypothesis Tests and Findings

Three hypotheses are investigated.

Welch two-sample t-tests are used where group comparisons are appropriate.
For monotonic relationships, non-parametric correlation is applied.

---

### Hypothesis 1 – Shop Size vs Success

**Question**  
Do shops that receive at least one review tend to list more products?

**Result**  
The Welch t-test yields a very small p-value.  
The null hypothesis is rejected.

**Conclusion**  
Successful shops have significantly more active listings on average.

---

### Hypothesis 2 – Engagement per Listing vs Success

**Question**  
Do successful shops receive more reviews per listing?

**Result**  
The Welch t-test again yields a very small p-value.

**Conclusion**  
Successful shops not only have more products, but also higher engagement
per product on average.

---

### Hypothesis 3 – Item Price vs Popularity

**Question**  
Is item price associated with item popularity?

**Methodology**  
- Popularity is measured using item review count.
- Two complementary analyses are applied:
  - Spearman rank correlation between price and popularity,
  - Welch t-test comparing mean prices of popular (top 25%) vs non-popular items.

**Result**  
Both analyses indicate a statistically significant relationship between
item price and popularity.

**Conclusion**  
Item price is meaningfully associated with item popularity, suggesting
that pricing strategies may influence customer engagement at the product level.

---

## 📌 Overall Insights

1. **Shop size matters**  
   Larger shops are significantly more likely to receive reviews.

2. **Engagement quality matters**  
   Successful shops achieve higher engagement per product, not just higher volume.

3. **Item pricing relates to popularity**  
   At the item level, prices show a statistically significant relationship
   with product popularity, highlighting the importance of pricing decisions.

---

## 🧰 Tools Used

- Python (pandas, NumPy, SciPy, matplotlib)  
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

The structure and wording of this README were prepared with the assistance
of an AI tool (OpenAI ChatGPT). All dataset selection, feature engineering,
statistical testing, and interpretations were implemented and verified
by the project owner.
