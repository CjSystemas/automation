# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from streamlit.logger import get_logger
import plotly.express as px

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        #Icones: https://emojidb.org/streamlit-emojis
        page_icon="chart_with_upwards_trend",
    )

    st.write("### CJ SYSTEMAS! 👋")

  

    st.markdown(
        """
        Análise e Desenvolvimento de Sistemas.
        Data Science com Python e Machine Learning
    """
    )

    st.title("Preço da Cesta Básica por Cidades")
    #https://drlee.io/building-streamlit-data-web-apps-with-pandas-there-to-tell-the-story-afe03ab71c57
    df = pd.read_excel('gasto_cesta_basica_8_meses.xlsx')
    st.dataframe(df)
    #st.write(df['Curitiba'].describe())
    #df_aux = df.describe(include='all')
    #st.write(df_aux)
    #df = df.describe(include='all').fillna("").astype("str")
    #st.write(df)
    #st.dataframe(df.style.hide(axis="index"))
    #st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)
    #st.dataframe(df, hide_index=False)
    # Plot histogram
    #df = df.set_index()
    #st.bar_chart(df)
    # Create a drop-down menu
    # plotting the line chart
    # Loading the iris dataset
    #https://www.comet.com/site/blog/streamlit-app-for-data-science-projects/
    st.line_chart(df['Salvador'])
   

if __name__ == "__main__":
    run()
