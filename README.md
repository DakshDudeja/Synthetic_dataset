# Synthetic Amazon Product Reviews Dataset Generation

## Table of Contents
1. [Introduction](#introduction)
2. [Data Cleaning and Preparation](#data-cleaning-and-preparation)
3. [Experimentation and Methodology](#experimentation-and-methodology)
4. [Use Case Diagram](#use-case-diagram)
5. [Results](#results)
6. [Challenges and Solutions](#challenges-and-solutions)
7. [Efficacy of the Synthetic Dataset](#efficacy-of-the-synthetic-dataset)
8. [Ensuring Originality in the Dataset](#ensuring-originality-in-the-dataset)
9. [Future Improvements](#future-improvements)

---

## 1. Introduction
The goal of this project was to generate a **synthetic dataset** of product reviews for supplements and vitamins using an existing Amazon reviews dataset. This synthetic dataset will simulate real-world user reviews while ensuring that it is **not a direct replica** of the original dataset. The synthetic data will serve for various purposes, including training machine learning models, enhancing datasets, and testing recommendation systems.

### Key Features of the Synthetic Dataset:
- **Diverse Ratings**: from 1-star to 5-star reviews.
- **Varied Review Content**: generated dynamically using GPT-3.5-turbo via LangChain.
- **Realistic User Behavior**: simulated through review length, helpful votes, and random user IDs.

---

## 2. Data Cleaning and Preparation

### **Original Dataset**:
We merged two datasets: product metadata (`parent_asin_x`, `title_y`, etc.) and the actual reviews (`asin`, `text`, `rating`, `user_id`, etc.). The merged dataset contained columns such as `asin`, `parent_asin_x`, `title_x`, `text`, `rating`, and more.

### **Cleaning Steps**:
- **Removed Duplicates**: We removed any duplicate reviews to ensure that the dataset didn't contain redundant information.
- **Missing Values**: Handled missing review text and product titles, ensuring every row in the dataset had sufficient information for review generation.

### **Columns in the Final Dataset**:
- **`pasin`**: Product's parent ASIN, directly derived from `parent_asin_x`.
- **`user_id`**: Generated as random unique IDs.
- **`rating`**: Based on a random selection of ratings from 1 to 5, following the original rating distribution.
- **`Product title`**: Extracted from the `title_y` column (product metadata).
- **`Categories`**: Extracted from the `categories` column.
- **`title_x` (review title)**: Dynamically generated based on the product name and rating using GPT-based prompts.
- **`text` (review text)**: Synthetic review text generated using a language model with varying focus points (e.g., product quality, user experience).
- **`timestamp`**: Random timestamps generated to simulate the review submission time.
- **`helpful_vote`**: Modeled using a formula that factors in review length and rating.

---

## 3. Experimentation and Methodology

### Why We Used LangChain:
LangChain was employed to orchestrate the process of review generation because of its flexibility to manage complex prompts and chain tasks, offering a structured way to call GPT models (GPT-3.5-turbo). It helped in dynamically building prompts based on review ratings and generating diverse and personalized reviews.

### Experimentation:
1. **Model**: We used GPT-3.5-turbo, accessed via LangChain, to generate both review titles and review text.
2. **Factors** considered while generating synthetic data:
   - **Review Length**: Varied to ensure the dataset contained both short and detailed reviews.
   - **Topic Diversity**: The reviews focused on different product features (e.g., effectiveness, ingredients, packaging).
   - **Sentiment Variety**: Ensured by generating distinct positive, neutral, and negative reviews.

### Prompt Design:
For each product and rating, we designed a dynamic prompt. For example:
```plaintext
"Write a detailed positive review for a product titled 'BComplex 50' in the 'Health & Household' category. Highlight its benefits, ease of use, and overall user satisfaction."



4. Use Case Diagram
The use case diagram below illustrates the interactions between the different components involved in the synthetic dataset generation process:

User: Inputs the original dataset and defines the parameters for generating synthetic reviews.
LangChain: Handles the dynamic prompt generation and orchestrates the interaction between the user inputs and GPT-3.5-turbo.
GPT Model: Generates the actual synthetic review text based on the prompts provided by LangChain.
Output: The final synthetic dataset containing reviews, ratings, and other metadata, which is saved in CSV format.

5. Results
The final synthetic dataset, synthetic_reviews.csv, consists of 10 rows, each representing a unique review generated by GPT-3.5-turbo. Here are some of the key insights:

Rating Distribution: The synthetic dataset closely matches the rating distribution found in the original dataset, with realistic variations in the number of 1-star to 5-star reviews.
Diversity in Reviews: The generated reviews contain diverse content, with some focusing on product quality, packaging, user experience, and effectiveness.
Helpful Votes: The number of helpful votes was modeled based on review length and rating to simulate real user behavior.
Sample Output
bash
Copy code
| pasin       | user_id  | rating | Product title | Categories           | title_x                                | text                                     | timestamp | helpful_vote |
|-------------|----------|--------|---------------|----------------------|----------------------------------------|------------------------------------------|-----------|--------------|
| B00012ND5G  | user_2850 | 5      | BComplex 50   | ['Health & Household'] | "Boost Your Energy and Nervous System" | "I recently started taking BComplex 50..."| 30:58.4   | 51           |
| B00013Z0ZQ  | user_4609 | 1      | Twinlab Ultra | ['Health & Household'] | "Disappointing Results"               | "I am extremely dissatisfied with..."     | 31:03.2   | 15           |
6. Challenges and Solutions
Key Challenges:
Ensuring Diversity: Ensuring that the generated reviews didn't sound repetitive while maintaining relevance to the product.

Solution: Introduced randomized sentence structures and personalized review content based on product categories and ratings.
Balancing Review Length: Some reviews needed to be detailed, while others concise, to reflect real-world user behavior.

Solution: Varied the length of the generated review content based on the rating (longer for higher ratings).
Managing the Rating Distribution: Ensuring that the rating distribution in the synthetic dataset resembled the original dataset without being an exact match.

Solution: Modeled rating generation based on the original distribution but added randomness to simulate more realistic user behavior.
7. Efficacy of the Synthetic Dataset
How We Measured Success:
Cosine Similarity: We calculated the cosine similarity between the original and synthetic reviews, ensuring they were distinct (with an average similarity score < 0.5).

Lexical Diversity: The synthetic dataset showed higher lexical diversity, ensuring varied vocabulary and non-repetitive text.

Rating and Helpful Vote Distributions: Visual comparisons of rating distributions confirmed that the synthetic dataset follows similar patterns without being identical.

8. Ensuring Originality in the Dataset
We took multiple steps to ensure the synthetic dataset was inspired by but not a replica of the original dataset:

Dynamic Prompting: Generated unique reviews using prompts tailored to product titles and categories.
Randomization: Introduced randomness in review structure, sentiment intensity, and vocabulary to ensure originality.
Perplexity Checks: Ensured that the GPT model was not simply repeating patterns by measuring the model's perplexity across generated reviews.
9. Future Improvements
Areas to Enhance:
Improving Review Diversity: Incorporating more personalized stories and anecdotes to make reviews feel more human.
Sentiment Analysis: Fine-tune the model to generate more nuanced emotions in reviews.
Aspect-Based Reviews: Generating reviews that focus on specific product aspects like price, packaging, and delivery, in addition to product performance.
