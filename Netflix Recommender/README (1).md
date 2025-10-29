# 🎬 Netflix Recommendation System

A content-based movie recommender that suggests similar titles using TF-IDF and cosine similarity.
Built with Streamlit, Scikit-learn, and Pandas.

## 💡 How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Download the Netflix dataset and place it as `netflix_titles.csv` in the project directory

3. Train the model:
   ```bash
   python train_model.py
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py --server.port 8501
   ```

## 📊 Dataset

You need the Netflix titles dataset (CSV format) with columns:
- title
- listed_in
- description
- director
- cast
- country
- release_year

## 🚀 Features

- Content-based filtering using TF-IDF
- Cosine similarity for recommendations
- Interactive Streamlit interface
- Adjustable number of recommendations
