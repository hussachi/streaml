import streamlit as st
import leafmap.foliumap as leafmap
from streamlit_folium import folium_static

# Configurer la première page avec un grand titre
st.set_page_config(page_title="Mon Application", page_icon="🌍", layout="wide")

# Fonction pour définir l'image de fond et le style
def set_bg_hack_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("https://img.freepik.com/photos-gratuite/fond-papier-peint_53876-25250.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        
        .text-container {{
            position: absolute;
            top: 80%;
            left: 5%;
            transform: translate(0%,0%);
            color: white;
            text-align: right;
        }}
        </style>
        <div class="text-container">
            <h1></h1>
            <p></p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Appeler la fonction pour définir l'image de fond
set_bg_hack_url()

# Fonction pour créer Leafmap et afficher la carte pour le premier bouton
def display_single_image():
    st.title("Affichez votre image classifiée")

    date = st.selectbox("Choisissez l'année de votre image:", ["2017", "2022"], key="date")
    classification = st.selectbox("Choisissez la classification de votre image:", ["nearest neighbor", "pixel", "arbre de décision", "à base de règles", "réseau de neurones"], key="class")

    # Construire le nom du fichier en fonction des choix de l'utilisateur
    url = f'C:\\Users\\hp\\Desktop\\webm\\tiff\\{date}-{classification}.tif'

    # Créer une carte Leafmap avec le fichier GeoTIFF choisi
    m = leafmap.Map(height=600, center=[39.4948, -108.5492], zoom=12)
    m.add_raster(url)

    # Afficher la carte Leafmap dans l'application Streamlit
    folium_static(m)

# Fonction pour créer Leafmap et afficher la carte pour le deuxième bouton
def display_compare_images():
    st.title("Configurez Votre SplitMap")

    date1 = st.selectbox("Choisissez l'année de votre 1ère image:", ["2017", "2022"], key="date1")
    date2 = st.selectbox("Choisissez l'année de votre 2ème image:", ["2017", "2022"], key="date2")

    class1 = st.selectbox("Choisissez la classification de votre 1ère image:", ["nearest neighbor", "pixel", "arbre de décision", "à base de règles", "réseau de neurones", "random forest"], key="class1")
    class2 = st.selectbox("Choisissez la classification de votre 2ème image:", ["nearest neighbor", "pixel", "arbre de décision", "à base de règles", "réseau de neurones", "random forest"], key="class2")

    # Construire les noms de fichiers en fonction des choix de l'utilisateur
    url1 = f'C:\\Users\\hp\\Desktop\\webm\\tiff\\{date1}-{class1}.tif'
    url2 = f'C:\\Users\\hp\\Desktop\\webm\\tiff\\{date2}-{class2}.tif'

    # Créer une carte Leafmap avec les deux fichiers GeoTIFF choisis
    m = leafmap.Map(height=600, center=[39.4948, -108.5492], zoom=12)
    m.split_map(url1, url2)

    # Afficher la carte Leafmap dans l'application Streamlit
    folium_static(m)

# Ajouter un grand titre à la première page
st.title("Suivi du barrage bin El Ouidane")
st.markdown("Ce site est crée pour faciliter la visualisation des résultats issus de diverses classifications réalisées lors de notre projet en utilisant Ecognition, Envi et GEE.")
st.markdown("")


# Ajouter du texte supplémentaire à la barre latérale
st.sidebar.markdown("## Sélectionnez une option ci-dessous :")

# Barre latérale avec deux options
selected_option = st.sidebar.radio("", ["Image Classifiée 🗺️", "SplitMap ✨"])

st.sidebar.markdown("## Réalisé par :")
st.sidebar.markdown("-Benchelha Nouhaila")
st.sidebar.markdown("-Oudaha Hatim")
st.sidebar.markdown("-Sellak Fatima-ezzahrae")
st.sidebar.markdown("-Zrhalla Houssam")

# Utiliser l'option sélectionnée pour afficher la page appropriée
if selected_option == "Image Classifiée 🗺️":
    display_single_image()
elif selected_option == "SplitMap ✨":
    display_compare_images()
