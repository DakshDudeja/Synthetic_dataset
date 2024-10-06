import pandas as pd

reviews_df = pd.read_csv('/Users/daksh/Desktop/Synthetic/reviews_supplements.csv') 
product_asin_df = pd.read_csv('/Users/daksh/Desktop/Synthetic/product_asin.csv')     

print("Columns in product_asin.csv:", reviews_df.columns)
print("Columns in reviews_supplements.csv:", product_asin_df.columns)

combined_df = pd.merge(reviews_df, product_asin_df, left_on='asin', right_on='parent_asin', how='left')

# print("Combined Dataset Preview:")
# print(combined_df.head())

# combined_df.to_csv('combined_reviews_metadata.csv', index=False)

print("Columns in the combined dataset:", combined_df.columns)

combined_df_cleaned = combined_df.dropna(subset=['text', 'title_x'])

combined_df_cleaned = combined_df_cleaned.drop_duplicates()







