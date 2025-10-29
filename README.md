
# 🎬 Netflix Movie Recommendation System

A content-based movie recommendation system that suggests movies similar to a selected title using **TF-IDF vectorization** and **cosine similarity**.  
This project was developed as part of an AI and Big Data learning initiative, with the goal of understanding how text-based machine learning models can be used to personalize recommendations in entertainment platforms like Netflix.

---

## 🧠 Project Description

The **Netflix Recommendation System** uses natural language processing (NLP) techniques to analyze movie descriptions, genres, directors, and cast data from the Netflix dataset.  
By converting these text-based attributes into numerical representations using **TF-IDF (Term Frequency–Inverse Document Frequency)**, and then computing **cosine similarity**, the system finds movies that are most similar in content to a user-selected movie.

The project demonstrates how AI can be used to enhance user experience through personalized suggestions — the same concept that powers real-world platforms such as Netflix, YouTube, and Spotify.

---

## 🚀 Features
- Suggests **Top 5 similar movies** to any selected title.
- Built using **pandas**, **scikit-learn**, and **streamlit**.
- Fully deployable on **Streamlit Cloud** or local machine.
- Uses **TF-IDF Vectorization** and **Cosine Similarity** for recommendations.
- Easy-to-use interface built with **Streamlit**.

---

## 🧩 Project Structure
```
📁 netflix-recommender/
│
├── app.py                # Streamlit web app
├── train_model.py        # Script to train the recommender and save artifacts
├── requirements.txt      # Python dependencies
├── artifacts/            # Folder containing saved model artifacts (.joblib, .csv)
│   ├── netflix_data.csv
│   ├── tfidf_vectorizer.joblib
│   └── cosine_sim.joblib
└── README.md             # Project documentation
```

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/netflix-recommender.git
cd netflix-recommender
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Train the Model
Ensure that your Netflix dataset (`netflix_titles.csv`) is available in the same directory, then run:
```bash
python train_model.py
```
This will create an `artifacts/` folder with saved model files.

### 4️⃣ Run the Streamlit App
```bash
streamlit run app.py
```
Then open the displayed URL (usually http://localhost:8501) to use the app.

---

## ☁️ Deployment on Streamlit Cloud
1. Push all files (including the `artifacts` folder) to your **GitHub repository**.  
2. Visit [https://share.streamlit.io](https://share.streamlit.io) and sign in with your GitHub account.  
3. Click **“New app”**, select your repo, and set the **main file path** to `app.py`.  
4. Click **Deploy** 🎉

---

## 📦 Requirements
```
streamlit
pandas
scikit-learn
joblib
```

---

## 📊 Dataset
Dataset used: **Netflix Movies and TV Shows**  
Available publicly on [Kaggle](https://www.kaggle.com/shivamb/netflix-shows).

---

## 🧠 Tech Stack
- **Python**
- **Streamlit**
- **Pandas**
- **Scikit-learn**
- **Joblib**

---

## 👤 Author
**Nandakishore V R**  
🎓 MBA in Operations Management | Aspiring Data & AI Professional  
📧 Email: nandakishorevr@gmail.com  


---

## 🏁 Future Improvements
- Display movie posters and genres for recommendations  
- Integrate collaborative filtering for better personalization  
- Add a search bar and genre filters  
