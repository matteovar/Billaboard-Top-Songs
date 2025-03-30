import streamlit as st


def create_cards(title: str, value: str, index:int):
    """Função responsável por criar o car em html"""

    card_html = f"""
    
    <style>
    
        .card {{
           border: 1px solid #373739 ;
           border-radius: 10px;
           text-align: left;
           height: 120px;
           padding-left: 10px;
           padding-top: 10px;
           background-color: #070707;
           margin-bottom: 50px;
        }}
        .card-title{{
            font-size: 16px;
        }}
        .card-value{{
            font-size: 30px;
            font-weight: 600;
        }}
        .card-index{{
            font-size: 16px;
        }}
    </style>
    <div class="card">
        <div class='card-title'>{title}</div>
        <div class = 'card-value'>{value}</div>
        <div class = 'card-index'>{index}</div>
    </div>
    
    """

    st.markdown(card_html, unsafe_allow_html=True)
