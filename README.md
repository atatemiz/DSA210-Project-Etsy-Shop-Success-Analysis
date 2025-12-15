💰 DSA210 Project – Etsy Shop Success Analysis  
Spring 24–25 · DSA210 Term Project  

---

📝 Project Overview
This project studies Etsy shops and their products to understand what “success” looks like on the platform.

Using two publicly available datasets from Kaggle (one at shop level, one at item level), I:

- Clean and combine the data,
- Create new, more informative features,
- Explore distributions and relationships with visualizations,
- Test three concrete statistical hypotheses about shop success and price levels.

The final goal is to turn raw marketplace data into interpretable insights that could guide a small Etsy seller.

---

🎯 Motivation
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
- How high-price items differ from lower-price items in a statistically meaningful way.

---

📂 Datasets Used

1️⃣ **Etsy Shops (shop-level dataset)**  
- Source: Kaggle – “Etsy Shops Dataset” by Sepideh Doost  
- Approx. 20,000 shops opened in November–December 2019  
- Example information:  
  - Number of active listings per shop  
  - Total number of reviews  
  - Favourites, sales counts  
  - Shop location, creation date, and a shop identifier  

2️⃣ **Etsy Items Price (item-level dataset)**  
- Source: Kaggle – “Etsy Items Price” by dimakyn  
- Product-level records with:  
  - Product title  
  - Shop name  
  - Item price  
  - Number of favourites  

The shop dataset describes the “storefront”, while the item dataset focuses on individual products and their prices.  
They are used together to answer both shop-level and price-level questions.

---

🛠️ Feature Engineering (What I Built From the Raw Data)

From the **shop dataset**:

- **Shop size**  
  The number of active listings is used as a measure of how large a shop is.

- **Engagement per product**  
  For each shop, I divide the total number of reviews by the number of active listings.  
  This gives “reviews per listing”, which reflects how much attention each product receives on average.  
  Shops with zero listings are handled carefully to avoid meaningless divisions.

- **Success label for shops**  
  I mark a shop as “successful” if it has at least one review.  
  Shops with no reviews are treated as “non-successful”.  
  This simple rule allows a clear comparison between two groups.

From the **item dataset**:

- **Clean numeric prices**  
  Prices are converted into numeric values and rows with invalid or missing prices are removed.

- **Price-based segments**  
  I calculate the 75th percentile of the price distribution.  
  Items whose price is at or above this threshold are assigned to a “high-price” segment,  
  and the remaining items form a “low-price” segment.  
  This creates two meaningful groups for comparing price levels.

These engineered features are the building blocks for all later analysis and hypothesis tests.

---

📊 Exploratory Data Analysis

Key observations from the visual exploration:

- **Shop size and reviews are highly skewed**  
  Histograms show that most shops have very few listings and zero reviews,  
  while a small group of shops has many products and a lot of feedback.

- **Relationship between number of listings and reviews**  
  A scatter plot with logarithmic scales on both axes shows a clear positive relationship:  
  larger shops tend to accumulate more reviews, although there is still considerable spread.

- **Item price distribution**  
  A histogram of item prices (with extreme values clipped) reveals that most products  
  sit in a relatively low price range, with a thin but visible tail of higher-priced items.  
  This justifies creating “high-price” and “low-price” segments.

---

🧪 Hypothesis Tests and Findings

All three hypotheses are tested using two-sample t-tests that allow unequal variances  
(commonly known as Welch t-tests). The aim is to compare averages between two groups and  
decide whether the observed differences are statistically significant.

---

### Hypothesis 1 – Shop Size vs Success

**Question**  
Do shops that receive at least one review tend to list more products than shops with no reviews?

**Groups**

- Group A: shops marked as successful (at least one review)  
- Group B: shops with no reviews  

**Null hypothesis (H₀)**  
The average number of active listings is the same in both groups.

**Alternative hypothesis (H₁)**  
Successful shops differ in average shop size (and in practice we expect them to be larger).

**Result and interpretation**

- The test returns a large positive test statistic and a very small p-value (well below 0.05).  
- H₀ is rejected.  
- Successful shops have **significantly more active listings** on average.  
  In other words, being “larger” is strongly associated with receiving at least some feedback.

---

### Hypothesis 2 – Engagement per Listing vs Success

**Question**  
Do successful shops receive more reviews per listing than shops with no reviews?

**Groups**

- Same two groups as in Hypothesis 1,  
  but the comparison is now made on “reviews per listing”.

**Null hypothesis (H₀)**  
The average number of reviews per listing is the same for successful and non-successful shops.

**Alternative hypothesis (H₁)**  
Successful shops have a different (expected to be higher) average number of reviews per listing.

**Result and interpretation**

- Again, the test yields a large positive test statistic with a very small p-value.  
- H₀ is rejected.  
- Successful shops do not only have more products; each product also tends to receive **more engagement on average**.  
  This suggests that **quality, visibility or marketing of listings** are also important,  
  not just opening many products.

---

### Hypothesis 3 – High-Price vs Low-Price Items

**Question**  
Is the high-price segment (top 25% of items by price) truly different from the rest  
in terms of average price?

**Groups**

- Group A: items in the top quarter of the price distribution (high-price segment)  
- Group B: all remaining items (low-price segment)

**Null hypothesis (H₀)**  
Both segments have the same mean price (no meaningful separation).

**Alternative hypothesis (H₁)**  
The high-price segment has a different mean price than the low-price segment.

**Result and interpretation**

- The Welch t-test finds a very strong difference between the two groups,  
  again with a p-value far below 0.05.  
- H₀ is rejected.  
- The price-based segmentation is statistically meaningful:  
  high-price items form a clearly distinct group.  
  This separation can later be used to compare other characteristics of premium vs regular products.

---

📌 Overall Insights

From the combined shop-level and item-level analysis, the main conclusions are:

1. **Shop size matters**  
   Shops that receive at least one review tend to have **many more active listings**  
   compared to shops that never receive feedback.

2. **Engagement per product matters**  
   Successful shops also perform better in terms of **reviews per listing**.  
   They do not simply win by sheer volume; their products also attract more attention individually.

3. **Price tiers are clearly separated**  
   The high-price segment is statistically distinct from the low-price segment.  
   Price tiers therefore make sense as a basis for further analysis or later models.

Together, these findings suggest that a seller aiming for success on Etsy should work on:

- Expanding the catalog with a healthy number of listings,  
- Improving engagement for each product (photos, descriptions, tags, marketing),  
- Being aware of where their products sit in the price spectrum and  
  possibly treating premium and regular items differently.

---

🧰 Tools Used

- Python (for data cleaning, feature creation, plotting and statistical tests)  
- Jupyter Notebook / VS Code Jupyter (interactive environment)  
- Git and GitHub (for version control and project submission)

---

📁 Repository Contents

- Jupyter notebook with the full analysis  
- Shop-level dataset file  
- Item-level dataset file  
- This README explaining the project, methods and main results

---

🤝 AI Assistance Disclosure

The structure and wording of this README were prepared with the help of an AI assistant (OpenAI ChatGPT).  
All dataset choices, feature definitions, statistical tests and final interpretations  
were implemented and checked by the project owner.
