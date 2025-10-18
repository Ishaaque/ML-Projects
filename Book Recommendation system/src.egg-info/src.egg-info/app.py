import pickle
import streamlit as st 
import numpy as np
st.header("Books Recommendation System using Machine Learning")
model = pickle.load(open('../artifacts/model.pkl','rb'))
books_name = pickle.load(open('../artifacts/books_name.pkl','rb'))
final_rating=pickle.load(open('../artifacts/final_rating.pkl','rb'))
book_pivot=pickle.load(open('../artifacts/book_pivot.pkl','rb'))
def fetch_poster(suggestion):
    # suggestion from kneighbors can be 2D (1, n); flatten to 1D indices
    book_names = []
    poster_url = []
    indices = np.array(suggestion).ravel()
    for idx in indices:
        # get book title by pivot index
        book_names.append(book_pivot.index[int(idx)])
    for name in book_names:
        try:
            ids = np.where(final_rating['title'] == name)[0][0]
            poster_url.append(final_rating.iloc[ids]['img_url'])
        except Exception:
            # fallback empty string if not found
            poster_url.append("")
    return poster_url
def recommend_books(book_name):
    books_list=[]
    poster_url=[]
    book_id=np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion=model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1),n_neighbors=6)
    
    poster_url=fetch_poster(suggestion)
    for i in range(len(suggestion)):
        books=book_pivot.index[suggestion[i]]
        for j in books:
            books_list.append(j)
    # return both lists so caller can unpack
    return books_list, poster_url
selected_books= st.selectbox("Select the Book Name",books_name)
st.set_page_config(
    page_title="Books Recommender System",
    page_icon="📕"
)


if st.button("Recommend Books"):
    recommendation_books,poster_url= recommend_books(selected_books) 
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.text(recommendation_books[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommendation_books[2])
        st.image(poster_url[2])
    with col3:
        st.text(recommendation_books[3])
        st.image(poster_url[3])
    with col4:
        st.text(recommendation_books[4])
        st.image(poster_url[4])
    with col5:
        st.text(recommendation_books[5])
        st.image(poster_url[5])


