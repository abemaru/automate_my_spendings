import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from src.my_spending_dict import generate_category_dict

def _any_in(usage: str, category: dict) -> str:
    # if 
    pass


def create_category_df(df: pd.DataFrame):
    category_dict = generate_category_dict()
    


def writer(df: pd.DataFrame):
    st.write("""
    # My first app
    Hello *world!*
    """)
    
    

    AgGrid(df)
