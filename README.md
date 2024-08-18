
## Movie Recommendation System

A movie recommendation system using basic machine learning techniques, including Count Vectorization for feature extraction and Cosine Similarity for computing movie similarities. The system recommends movies similar to a given one based on these techniques.

### Features
- **Movie Recommendations**: Provides suggestions for movies similar to a selected movie.

### Components

#### Jupyter Notebook
The Jupyter Notebook handles data preprocessing and model training. Key components include:

- **Data Loading**: Reads movie and credits data.
- **Data Preprocessing**: Cleans and formats data.
- **Feature Extraction**: Converts text data into numerical vectors using CountVectorizer.
- **Similarity Calculation**: Computes cosine similarity between movie vectors.
- **Model Saving**: Saves the processed movie data and similarity matrix for use in the Streamlit app.

**Notebook File**:
- `movie_recommender_notebook.ipynb`: Contains the code for data preprocessing and generating recommendations.

#### Streamlit Application
The Streamlit app provides an interactive interface for movie recommendations, allowing users to select a movie and view recommendations along with posters.

**App File**:
- `app.py`: The main script for the Streamlit application.

**Supporting Files**:
- `setup.sh`: Configures Streamlit settings.
- `Procfile`: Configuration file for deployment.
- `movies.pkl`: Pickled movie data.
- `movies_dict.pkl`: Pickled dictionary of movie data.
- `similarity.pkl`: Pickled similarity matrix.

### Installation

To set up and run the Streamlit application, follow these steps:

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

3. **Open Browser**:
   Navigate to `http://localhost:8501` to interact with the app.

### How It Works

#### Jupyter Notebook Processing:
- **Data Merging**: Combines movie and credits datasets.
- **Preprocessing**: Cleans and formats data for analysis.
- **Feature Extraction**: Converts textual data into numerical features using Count Vectorizer.
- **Model Training**: Computes the similarity matrix and saves the model for the Streamlit app.

#### Streamlit Application:
- **Movie Input**: Users select a movie from a dropdown menu.
- **Recommendation Generation**: Finds similar movies using the precomputed similarity matrix.
- **Display**: Shows recommended movies along with their posters.
