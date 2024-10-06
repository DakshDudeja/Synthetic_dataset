import logging
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import pandas as pd
import random
import numpy as np
from datetime import timedelta, datetime

# Initialize the logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key="##")

# original dataset
reviews_df = pd.read_csv('/Users/daksh/Desktop/Synthetic/reviews_supplements.csv')
product_asin_df = pd.read_csv('/Users/daksh/Desktop/Synthetic/product_asin.csv')

# Merge the two datasets based on ASIN
combined_df = pd.merge(reviews_df, product_asin_df, left_on='asin', right_on='parent_asin', how='left')

#new dataset with the following columns
columns = ['pasin', 'user_id', 'rating', 'Product title', 'Categories', 'title_x', 'text', 'timestamp', 'helpful_vote']
synthetic_data = []

rating_distribution = combined_df['rating'].value_counts(normalize=True)

helpful_vote_mean = combined_df['helpful_vote'].mean()
helpful_vote_std = combined_df['helpful_vote'].std()

def extract_text(response):
    if isinstance(response, dict):
        return response.get('text', '') 
    return response.strip()  

# Function to generate a synthetic review title using LLM
def generate_synthetic_title(product_title, rating):
    prompt = f"Write a catchy and informative title for a {rating}-star review of a product called {product_title}."
    prompt_template = PromptTemplate.from_template(prompt)
    review_chain = LLMChain(prompt=prompt_template, llm=llm)
    synthetic_title = review_chain.invoke({})
    return extract_text(synthetic_title)  

# Function to generate synthetic review text based on rating and category
def generate_synthetic_review(product_title, rating, category):
    if rating >= 4:
        prompt = f"Write a detailed and positive {rating}-star review for a {category} product titled {product_title}. Describe its benefits and your experience."
    elif rating == 3:
        prompt = f"Write a balanced {rating}-star review for a {category} product titled {product_title}, mentioning both pros and cons."
    else:
        prompt = f"Write a critical {rating}-star review for a {category} product titled {product_title}, explaining what issues you faced and why you're dissatisfied."

    prompt_template = PromptTemplate.from_template(prompt)
    review_chain = LLMChain(prompt=prompt_template, llm=llm)
    synthetic_review = review_chain.invoke({})
    return extract_text(synthetic_review) 

def generate_random_timestamp():
    random_offset = random.randint(0, 365)
    random_date = datetime.now() - timedelta(days=random_offset)
    if random_date.month == 12:
        random_offset = random.randint(0, 50)  # More likely to occur in December
        random_date = datetime.now() - timedelta(days=random_offset)
    return random_date

# Generate a user ID based on product popularity
def generate_user_id(product_title):
    if "popular_product" in product_title.lower():
        return "user_" + str(random.randint(1000, 2000))
    else:
        return "user_" + str(random.randint(2001, 5000))

# Adjust helpful votes based on rating and review length
def calculate_helpful_vote(rating, review_length):
    if rating == 5:
        helpful_vote = int(np.random.normal(40, 15))
    elif rating == 3:
        helpful_vote = int(np.random.normal(20, 10))
    else:
        helpful_vote = int(np.random.normal(10, 5))

    helpful_vote += int(review_length / 100)  # Longer reviews get more votes
    return max(0, helpful_vote)

# Generate synthetic reviews for 10 rows
for index, row in combined_df.head(10).iterrows():
    logging.info(f"Generating synthetic data for row {index + 1}")
    
    pasin = row['parent_asin_x']  
    user_id = generate_user_id(row['title_y'])
    product_title = row['title_y']
    categories = row['categories']
    timestamp = generate_random_timestamp()

    rating = np.random.choice(rating_distribution.index, p=rating_distribution.values)
    
    logging.info(f"Generating review title and text for product: {product_title} with rating: {rating}")
    review_title = generate_synthetic_title(product_title, rating)
    review_text = generate_synthetic_review(product_title, rating, categories)
    review_length = len(review_text)
    helpful_vote = calculate_helpful_vote(rating, review_length)

    synthetic_data.append([pasin, user_id, rating, product_title, categories, review_title, review_text, timestamp, helpful_vote])

# Convert the synthetic data into a DataFrame
synthetic_df = pd.DataFrame(synthetic_data, columns=columns)
synthetic_df.to_csv('final_smart_synthetic_reviews.csv', index=False)

logging.info("Final synthetic dataset generated and saved!")





