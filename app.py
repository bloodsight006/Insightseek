import streamlit as st
from crawler import crawl_webpages
from search_engine import SearchEngine


st.set_page_config(page_title="InsightSeek", layout="wide")


st.markdown("""
<style>

body {
background-color:#0e1117;
}

.big-title{
font-size:42px;
font-weight:bold;
text-align:center;
}

.subtitle{
text-align:center;
font-size:18px;
color:gray;
margin-bottom:30px;
}

.result-card{
padding:20px;
border-radius:12px;
background-color:#1c1f26;
margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)



st.markdown('<p class="big-title">InsightSeek 🔎</p>', unsafe_allow_html=True)

st.markdown('<p class="subtitle">Intelligent Web Knowledge Search Engine</p>', unsafe_allow_html=True)



start_urls = [
"https://en.wikipedia.org/wiki/Data_science"
]


with st.spinner("Crawling web pages and building search index..."):

    documents, titles, urls = crawl_webpages(start_urls, max_pages=20)

    engine = SearchEngine(documents)



st.sidebar.title("System Statistics")

st.sidebar.write("Indexed Pages:", len(documents))

st.sidebar.write("Vocabulary Size:", len(engine.vectorizer.vocabulary_))

st.sidebar.write("Documents Indexed:", len(documents))



query = st.text_input("Search AI / Machine Learning topics")



if query:

    scores = engine.search(query)

    ranked = sorted(
        list(enumerate(scores)),
        key=lambda x: x[1],
        reverse=True
    )

    st.write("### Search Results")

    for i, score in ranked[:8]:

        if score > 0:

            st.markdown(f"""
            <div class="result-card">
            <h4>{titles[i]}</h4>
            <p><b>Relevance Score:</b> {round(score,3)}</p>
            <a href="{urls[i]}" target="_blank">{urls[i]}</a>
            </div>
            """, unsafe_allow_html=True)



st.sidebar.markdown("---")

st.sidebar.markdown("### How InsightSeek Works")

st.sidebar.markdown("""
1️⃣ Web Crawling  
2️⃣ Text Extraction  
3️⃣ TF-IDF Vectorization  
4️⃣ Cosine Similarity Ranking  
""")
