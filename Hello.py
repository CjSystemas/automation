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
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        #Icones: https://emojidb.org/streamlit-emojis
        page_icon="chart_with_upwards_trend",
    )

    st.write("# CJ SYSTEMAS! 👋")

  

    st.markdown(
        """
        Análise e Desenvolvimento de Sistemas.
        Data Science com Python e Machine Learning
    """
    )

    st.title("Preço da Sexta Básica por Cidades")
    df= pd.read_excel('gasto_cesta_basica_8_meses.xlsx')
    st.write(df)
   

if __name__ == "__main__":
    run()
