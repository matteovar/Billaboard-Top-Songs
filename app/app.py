import streamlit as st
import plotly.express as px
from millify import millify as mf
from src.utils.cards import create_cards
from src.main import read_data


st.set_page_config(page_title="Billaboard Top Songs", layout="wide")
(
    df,
    genero_mais_popular_stream,
    artist_mais_popular,
    artist_mais_popular_streams,
    genero_mais_popular,
    musica_mais_popular_streams,
    musica_mais_popular,
    virality_musica_tt,
    virality_musica,
    df_stream_by_genre,
    df_art_pop,
    df_week,
    df_art_peak,
    df_art_song,
) = read_data()

cols_card = st.columns(4)

with cols_card[0]:
    gps = mf(genero_mais_popular_stream)
    create_cards(
        "Gênero Mais Popular",
        genero_mais_popular,
        f"Total de Streams: {gps}",
    )
with cols_card[1]:
    aps = mf(artist_mais_popular_streams)
    create_cards(
        "Artista Mais Popular",
        artist_mais_popular,
        f"Numero de Streams: {aps}",
    )
with cols_card[2]:
    mps = mf(musica_mais_popular_streams)
    create_cards(
        "Musica Mais Popular",
        musica_mais_popular,
        f"Quantidade de Streams: {mps}",
    )
with cols_card[3]:
    create_cards(
        "Música Mais Viral no TikTok",
        virality_musica,
        f'Viral no TikTok: {virality_musica_tt}%',
    )


cols_charts = st.columns(2)
with cols_charts[0]:
    selected_genre = st.multiselect(
        "Select one or more genre:",
        options=df_stream_by_genre["Genre"].unique(),
        default=["Blues"],
    )

    df_filter = df_stream_by_genre[df_stream_by_genre["Genre"].isin(selected_genre)]
    fig_genre_year = px.line(
        df_filter,
        x="Release Year",
        y="Streams",
        color="Genre",
        title="Popularidade dos Gêneros ao Longo dos Anos",
    )

    st.plotly_chart(fig_genre_year)


with cols_charts[1]:

    select_art = st.multiselect(
        "Select one or more years",
        options=df_art_pop["Release Year"].unique(),
        default=df_art_pop["Release Year"].max(),
    )
    df_filter2 = df_art_pop[df_art_pop["Release Year"].isin(select_art)]
    fig_art = px.bar(
        df_filter2,
        x="Artist",
        y="Streams",
        color="Release Year",
        title="Popularidade dos Artistas ao Longo dos Anos",
    )

    st.plotly_chart(fig_art)


def weeks_on_char():
    st.markdown('''
        ### Musicas com maiores sequencias de semanas por genero musical
                ''')
    select_mult = st.multiselect(
        "Selecione um genero musical: ", options=df_week["Genre"].unique(), default=["Blues"]
    )

    filter_weeks = df_week[df_week["Genre"].isin(select_mult)]

    filted_weeks = filter_weeks.drop(columns=["Genre"])
    st.dataframe(filted_weeks, hide_index=True)


weeks_on_char()


cols_charts_2 = st.columns(2)

with cols_charts_2[0]:
    fig = px.imshow(
        df_art_peak,
        labels={"x": "Peak Position", "y": "Artista"},
        color_continuous_scale="Blues",
        title="Artistas vs. Posição Máxima",
    )

    fig.update_xaxes(title="Peak Position", tickangle=45)
    fig.update_yaxes(title="Artista")

    st.plotly_chart(fig)


with cols_charts_2[1]:
    st.markdown('''
        ### Músicas Mais Ouvidas por Artista
                ''')
    select_art = st.selectbox(
        "Selecione um Artista",
        options=df_art_song["Artist"].unique(),
        placeholder="Selecione",
    )
    filter_art = df_art_song[df_art_song["Artist"] == select_art]
    df_filtered = filter_art.drop(columns=["Artist"])

    st.dataframe(df_filtered, hide_index=True)
