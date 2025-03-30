import pandas as pd
import plotly.express as px


def read_data():

    df = pd.read_csv(
        "/Users/matteovarnier/Documents/Projetos/Python/streamlit/pandas/app/data/input/music_dataset.csv"
    )

    df.groupby(["Release Year"])[
        "Song"
    ].count()  # Numero totais de musicas feitas nos anos

    # Artistas com maiores streamings
    df_art = (
        df.groupby(["Artist"])["Streams"]
        .sum()
        .reset_index()
        .sort_values("Streams", ascending=False)
    )
    artist_mais_popular = df_art.iloc[0]["Artist"]
    artist_mais_popular_streams = df_art.iloc[0]["Streams"]
    

    # Estilo Musical mais popular
    df_genre = (
        df.groupby(["Genre"])["Streams"]
        .sum()
        .reset_index()
        .sort_values("Streams", ascending=False)
    )
    genero_mais_popular = df_genre.iloc[0]["Genre"]
    genero_mais_popular_stream = df_genre.iloc[0]["Streams"]

    df_song = (
        df.groupby(["Song"])["Streams"]
        .sum()
        .reset_index()
        .sort_values("Streams", ascending=False)
    )
    musica_mais_popular = df_song.iloc[0]["Song"]
    musica_mais_popular_streams = df_song.iloc[0]["Streams"]

    df_song_tiktok = (
        df.groupby(["Song","TikTok Virality"])["Streams"]
        .mean()
        .reset_index()
        .sort_values(["TikTok Virality", "Streams"], ascending=False)
    )
    virality_musica = df_song_tiktok.iloc[0]["Song"]
    virality_musica_tt = df_song_tiktok.iloc[0]["TikTok Virality"]
    
    df_stream_by_genre = (
        df.groupby(["Genre", "Release Year"])["Streams"].sum().reset_index()
    )

    df_art_pop = (
        df.groupby(["Artist", "Release Year"])["Streams"]
        .sum()
        .reset_index()
        .sort_values("Streams", ascending=False)
    )
    df_top10_por_ano = (
        df_art_pop.sort_values(["Release Year", "Streams"], ascending=[True, False])
        .groupby("Release Year")
        .head(10)
    )

    df_week = (
        df.groupby(["Song", "Genre"])["Weeks on Chart"]
        .sum()
        .reset_index()
        .sort_values("Weeks on Chart", ascending=False)
    )

    df_art_peak = df.groupby(["Artist", "Peak Position"]).size().unstack(fill_value=0)

    df_art_song = (
        df.groupby(["Artist", "Song", "Genre", "Peak Position", "Weeks on Chart"])[
            "Streams"
        ]
        .sum()
        .reset_index()
        .sort_values("Streams", ascending=False)
    )

    return (
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
        df_top10_por_ano,
        df_week,
        df_art_peak,
        df_art_song,
    )
