import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('streamlit simple app')
page=st.sidebar.radio("pilih halaman",["dataset","visualisasi"])

if page == "dataset":
    st.header("Halaman dataset")
    data= pd.read_csv("pddikti_example.csv")
    st.write(data)




elif page == "visualisasi":
    st.header("halaman visualisasi")  
    st.set_option('deprecation.showPyplotGlobalUse',False)
    data= pd.read_csv("pddikti_example.csv")
    selected_uni=st.selectbox('pilih universitas',data['universitas'].unique())
    filtered_data= data[data['universitas']==selected_uni]

    plt.figure(figsize=(12, 6))
    for prog_studi in filtered_data['program_studi'].unique():
        subset=filtered_data[filtered_data['program_studi'] == prog_studi]

        subset=subset.sort_values(by="id", ascending=False)

        plt.plot(subset['semester'],subset['jumlah'],label=prog_studi)
    plt.title(f"Visualisasi data untuk{selected_uni}")
    plt.xlabel("semester")
    plt.xticks(rotation=90)
    plt.ylabel("jumlah")
    plt.legend()
    st.pyplot()