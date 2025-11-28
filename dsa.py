import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

plt.style.use("default")
plt.rcParams["figure.figsize"] = (8, 5)

df = pd.read_csv("etsy_shops_data.csv")

print("First 5 rows:")
print(df.head(), "\n")

print("Columns:")
print(df.columns.tolist(), "\n")

print("Info:")
print(df.info(), "\n")

print("Statistical summary:")
print(df.describe().T, "\n")

if "sales_count" in df.columns:
    df["sales_count"] = df["sales_count"].replace(-99, np.nan)
if "review_count" in df.columns:
    df["review_count"] = df["review_count"].replace(-99, np.nan)

critical_cols = ["listing_active_count", "review_count"]
for c in critical_cols:
    if c in df.columns:
        df = df[df[c].notna()]

print("Shape after cleaning:", df.shape, "\n")

df["num_listings"] = df["listing_active_count"]
df["num_listings_safe"] = df["num_listings"].replace(0, np.nan)
df["reviews_per_listing"] = df["review_count"] / df["num_listings_safe"]

print("First 5 rows with engineered features:")
print(df[["num_listings", "review_count", "reviews_per_listing"]].head(), "\n")


def show_hist(series, title, xlabel):
    s = series.dropna()
    s_clip = s.clip(upper=s.quantile(0.99))
    plt.hist(s_clip, bins=30)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


show_hist(df["num_listings"], "Number of Listings (clipped 99th percentile)", "num_listings")
show_hist(df["review_count"], "Review Count (clipped 99th percentile)", "review_count")
show_hist(df["reviews_per_listing"], "Reviews per Listing (clipped 99th percentile)", "reviews_per_listing")

plt.scatter(
    df["num_listings"],
    df["review_count"],
    alpha=0.3
)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Number of Listings (log)")
plt.ylabel("Review Count (log)")
plt.title("Listings vs Reviews (log-log)")
plt.tight_layout()
plt.show()

df["successful_shop"] = (df["review_count"] > 0).astype(int)

print("Successful shop flag (review_count > 0):")
print(df["successful_shop"].value_counts(), "\n")

success = df[df["successful_shop"] == 1]
non_success = df[df["successful_shop"] == 0]

print("Success group shape:", success.shape)
print("Non-success group shape:", non_success.shape, "\n")

success_listings = success["num_listings"].dropna()
non_success_listings = non_success["num_listings"].dropna()

t_stat1, p_val1 = stats.ttest_ind(
    success_listings,
    non_success_listings,
    equal_var=False
)

print("=== Hypothesis 1: num_listings (successful vs non-successful) ===")
print("T-statistic:", t_stat1)
print("p-value:", p_val1, "\n")

success_rpl = success["reviews_per_listing"].dropna()
non_success_rpl = non_success["reviews_per_listing"].dropna()

t_stat2, p_val2 = stats.ttest_ind(
    success_rpl,
    non_success_rpl,
    equal_var=False
)

print("=== Hypothesis 2: reviews_per_listing (successful vs non-successful) ===")
print("T-statistic:", t_stat2)
print("p-value:", p_val2, "\n")

print("Done.")
