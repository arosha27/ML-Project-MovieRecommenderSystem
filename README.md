# 🎬 Movie Recommender System

A **Content-Based Movie Recommender System** built using **Python** and deployed with **Streamlit**. The system recommends 5 similar movies based on your selected movie, using movie metadata (cast, crew, keywords, genres, and overview).

---

## 📌 Table of Contents

- [🚀 Demo](#-demo)
- [📖 Project Overview](#-project-overview)
- [🛠️ Tech Stack](#-tech-stack)
- [🔁 Workflow](#-workflow)
- [💻 How to Run Locally](#-how-to-run-locally)
- [🖼️ Screenshots](#-screenshots)
- [🌱 Future Improvements](#-future-improvements)
- [🙏 Credits](#-credits)
- [📬 Contact](#-contact)

---

## 🚀 Demo

🎯 Try the live app here:  
👉 **[🌐 Movie Recommender System](https://ml-project-movierecommendersystem-6cm6wf6cejr5xxuav2bgfi.streamlit.app/)**

---

## 📖 Project Overview

This recommender system uses **cosine similarity** to find and suggest movies that are similar to the one selected by the user. It processes a movie's **overview, cast, crew, keywords**, and **genres** to create a meaningful recommendation system.

---

## 🛠️ Tech Stack

- **Python**
- **Pandas & NumPy**
- **NLTK (PorterStemmer)**
- **Scikit-learn** (`CountVectorizer`, `cosine_similarity`)
- **Streamlit** – Web UI
- **Pickle** – Save and load data objects
- **TMDB API** – Fetch movie posters
- **gdown** – Load large `similarity.pkl` file from Google Drive

---

## 🔁 Workflow

### 🔹 Data Processing (`main_logic.py` / `BookRecommenderSystemProject.ipynb`)
- Download TMDB 5000 Movie & Credits datasets using `kagglehub`
- Merge datasets and retain useful columns: `movie_id`, `title`, `overview`, `genres`, `cast`, `crew`, `keywords`
- Clean and process columns using:
  - JSON parsing (`ast.literal_eval`)
  - Keyword/Name extraction
  - Removing spaces from compound names (e.g., `Sam Worthington` → `SamWorthington`)
  - Stemming and lowercase transformation

### 🔹 Feature Engineering
- Combine all processed fields into a single column `tags`
- Vectorize the `tags` column using **Bag of Words (CountVectorizer)**
- Compute cosine similarity between all movie vectors

### 🔹 Export
- Save the movie metadata (`new_df`) to `movies.pkl`
- Save the cosine similarity matrix to `similarity.pkl`
- Upload `similarity.pkl` to **Google Drive**, then download in the app using `gdown`

---

### 🔹 Frontend (`app.py`)
- Load `movies.pkl` locally and `similarity.pkl` from Google Drive
- Display a Streamlit UI with:
  - Dropdown menu for movie selection
  - Button to trigger recommendation
  - Top 5 recommended movies with posters (fetched via TMDB API)

---

## 🖼️ Screenshot

Here’s a preview of the Movie Recommender System in action:

![Movie Recommender Streamlit App](screenshots/movie-app.png)


## 💻 How to Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/movie-recommender-system.git
cd movie-recommender-system

📬 Contact
If you have questions, feedback, or collaboration ideas:

📧 aroshaamin0@gmail.com
🔗 https://www.linkedin.com/in/arosha-amin
