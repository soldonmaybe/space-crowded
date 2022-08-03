import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='How Crowded Our Space? - soldonmaybe', 
                    page_icon = ':night_with_stars:', layout='wide', 
                    initial_sidebar_state="expanded",
                    menu_items={'About': "soldonmaybe.2022"})

st.markdown('# How Crowded is Our Space? :sparkles:')
st.write('We human beings have been venturing into space since October 4, 1957, when the Union of Soviet Socialist Republics (U.S.S.R.) launched Sputnik, the first artificial satellite to orbit Earth.')
st.write('From there on, thousands of objects and living creatures have been sent into space. Moreover, thousands of sky objects - asteroids are assembled near earth\'s orbit, along with man-made sky objects.')
st.markdown("---")

# Human in Space
st.title("Human in Space")
st.write('Banyak negara berlomba untuk mengirim manusia ke luar angkasa. United States (Amerika) menjadi negara paling produktif dalam mengirim manusia ke luar angkasa dengan 865 dari 1294 penerbangan ke angkasa.')
tab1, tab2, tab3 = st.tabs(['All Countries', 'Top Countries', 'Complete Database'])
with tab1:
    astro = pd.read_csv('astronout_database.csv')
    astro2 = astro.loc[:, ['Country','Total Flights']]
    import plotly.express as px
    fig = px.histogram(
                astro2, 
                x='Country',
                y='Total Flights',
                nbins=10)
    st.plotly_chart(fig)

with tab2:
    import plotly.graph_objects as go
    labels = ['Canada','China','France','Germany', 'Italy', 'Japan', 'Russia', 'Soviet Union', 'United States']
    values = [18, 14, 19, 15, 13, 21, 137, 136, 865]
    fig2 = go.Figure(data=[go.Pie(labels=labels, values=values)])
    st.plotly_chart(fig2)

with tab3:
    st.dataframe(data = astro)

st.metric(label= "Akumulasi Manusia di Angkasa", value="1294")

st.title('Budget for Space Exploration')
st.write('Butuh biaya yang tidak sedikit untuk mengirimkan manusia ataupun objek lain ke luar angkasa. Hal ini yang masih menjadi momok bagi negara berkembang seperti Indonesia untuk mulai memodali dalam penjelajahan angkasa')
st.write('Berikut histogram pembiayaan pemerintah Amerika untuk NASA dalam menjelajahi luar angkasa yang bisa jadi referensi jika pemerintah Indonesia ingin mengirimkan wakil ke angkasa.')
budget = pd.read_csv('nasa_budget.csv')
import plotly.express as px
fig3 = px.line(
                budget, 
                x='Year',
                y='Budget',
                title='NASA Budget for Space Exploration')
st.plotly_chart(fig3)
st.write('Data sudah dikonversi berdasarkan inflasi 2022')