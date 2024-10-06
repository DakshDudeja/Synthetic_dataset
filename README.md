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
