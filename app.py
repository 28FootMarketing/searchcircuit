import streamlit as st
from utils.keyword_tools import fetch_related_keywords
from utils.serp_parser import get_serp_data
from utils.clustering import cluster_keywords
import pandas as pd

st.set_page_config(page_title="SearchCircuit – SEO Keyword Mapper", layout="wide")
st.title("🔌 SearchCircuit – Intelligent Keyword & SERP Clustering Tool")

query = st.text_input("Enter a seed keyword")
run_search = st.button("Generate Keyword Cluster")

if run_search and query:
    with st.spinner("Fetching keywords and SERP data..."):
        keywords = fetch_related_keywords(query)
        clusters = cluster_keywords(keywords)
        serp_results = get_serp_data(clusters)

    st.subheader("📊 Keyword Clusters")
    for label, kws in clusters.items():
        st.markdown(f"**Cluster: {label}**")
        st.write(kws)

    st.subheader("🔎 SERP Data Overview")
    df = pd.DataFrame(serp_results)
    st.dataframe(df)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download SERP Data", csv, "serp_data.csv", "text/csv")
