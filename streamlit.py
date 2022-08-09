import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='How Crowded is Our Space? - soldonmaybe', 
                    page_icon = ':night_with_stars:', layout='wide', 
                    initial_sidebar_state="expanded",
                    menu_items={'About': "soldonmaybe.2022"})

st.markdown('# How Crowded is Our Space? :sparkles:')
st.write('We human beings have been venturing into space since October 4, 1957, when the Union of Soviet Socialist Republics (U.S.S.R.) launched Sputnik, the first artificial satellite to orbit Earth.')
st.write('From there on, thousands of objects and living creatures have been sent into space. Moreover, thousands of sky objects - asteroids are assembled near earth\'s orbit, along with man-made sky objects.')
st.markdown("---")

# Human in Space
st.title("Human in Space")
st.write('Banyak negara berlomba untuk mengirim manusia ke luar angkasa. United States (Amerika) menjadi negara paling produktif dalam mengirim manusia ke luar angkasa dengan 865 perjalanan dari 1294 penerbangan ke angkasa.')
tab1, tab2, tab3 = st.tabs(['All Countries', 'Top Countries', 'Complete Database'])
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.write('Perlombaan menuju angkasa dimulai pada tahun 1957 ketika perang dingin antara USA dan USSR berkecamuk. Kedua negara saling mengalahkan untuk menjadi bangsa yang terhebat dengan berlomba-lomba mencapai luar angkasa. Total Perjalan Soviet Union ditambah dengan Rusia masih kalah jauh dengan United States. Ditambah bergairahnya perusahaan amerika bernama SpaceX milik elonmusk yang membawa misi menghantarkan manusia menduduki mars.')
        st.metric(label= 'Akumulasi Manusia di Angkasa', value='569')
        st.metric(label= 'Akumulasi Perjalanan ke Angkasa', value='1294')    
    with col2:
        astro = pd.read_csv('astronout_database.csv')
        astro2 = astro.loc[:, ['Country','Total Flights']]
        import plotly.express as px
        fig = px.histogram(
                astro2, 
                x='Total Flights',
                y='Country',
                nbins=10,
                title='All Countries')
        st.plotly_chart(fig)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.write('Kemudian banyak negara berlomba untuk turut serta menjelajahi luar angkasa. Pada pie chart top countries dengan manusia terbanyak di angkasa dapat dilihat bahwa semua negara yang dapat ikut serta berlomba mengeksplorasi angkasa adalah negara maju seperti Amerika, Rusia, Jepang, Prancis dan sebagainya. Negara berkembang masih sulit untuk ikut berkompetisi karena masih harus fokus dalam membangun ekonomi negara tersebut.')
        st.metric(label= 'Akumulasi Manusia di Angkasa', value='569')
        st.metric(label= 'Akumulasi Perjalanan ke Angkasa', value='1294')  
    with col2:
        import plotly.graph_objects as go
        labels = ['Japan', 'Russia', 'Soviet Union', 'United States']
        values = [21, 137, 136, 865]
        fig2 = go.Figure(data=[go.Pie(labels=labels, values=values)])
        st.plotly_chart(fig2)

with tab3:
    st.dataframe(data = astro)

# Budget
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
st.write('Pada chart tersebut diketahui bahwa budget NASA untuk keseluruhan eksplorasi luar angkasa adalah sebesar USD 24 Billion atau 24 Miliar Dollar atau sebesar 370 Triliun Rupiah. Angka yang sangat fantastis bagi negara berkembang seperti Indonesia yang dapat digunakan untuk meningkatkan ekonomi warganya terlebih dahulu.')
st.write('Budget NASA relatif stabil pasca perang dingin dan pengeluaran tertinggi (dengan inflasi tahun 2022) adalah pada tahun 1965 sebesar USD 34 Billion atau sebesar 510 Triliun Rupiah. Ini membuktikan bahwa saat perang dingin, Amerika tidak mau kalah dengan pesaingnya untuk menuju angkasa.')

# Objects Launched
st.title('Object launched')
launch = pd.read_csv('object_launched.csv')
launch1 = launch.query("Entity=='World'")
import plotly.express as px
fig4 = px.line(
                launch1, 
                x='Year',
                y='yearly_launches',
                title='Object Launched Annually')
st.plotly_chart(fig4)
st.metric(label= 'Benda yang diterbangkan ke angkasa pada 2021', value='1807')
st.write('Sejak 1962, PBB telah mendata dan meregistrasi objek yang diluncurkan ke luar angkasa. Pada awalnya dilakukan untuk membantu komite PBB dalam masalah Penggunaan Luar Angkasa untuk Perdamaian dalam lingkup politik, hukum dan teknis luar angkasa yang mengakibatkan pendaftaran objek menjadi sarana untuk mengidentifikasi negara untuk memikul tanggung jawab dan kewajiban internasional untuk benda luar angkasa')
st.write('Objek yang didata adalah satelit, probe, roket, landers, pesawat ruang angkasa berawak dan stasiun luar angkasa internasional.')

#Tracked Objects
st.title('Tracked Objects in Near Earth Space')
st.write('Banyak objek yang diluncurkan dapat menjadi masalah ketika sudah tidak digunakan. Karena membutuhkan waktu yang tidak sebentar untuk objek tersebut masuk kembali ke atmosfer bumi. Bahkan beberapa objek sudah menjadi satelit tidak berguna yang hanya mengitari bumi tanpa melakukan fungsi apapun.')
st.write('Objek tersebut mulai dari serpihan hancurnya benda angkasa, badan roket hasil peluncuran atau bahkan barang bawaan untuk keperluan misi. Hal ini dapat menjadi masalah di kemudian hari dan pelacakan objek-objek tersebut menjadi sangat diperhatikan.')
track = pd.read_csv('tracked_objects.csv')
del track['Code']
tab4, tab5, tab6 = st.tabs(['Debris Tracked', 'Payload Tracked', 'Rocket Bodies Tracked'])
with tab4:
    track_debris = track.query("Entity=='Debris'")
    import plotly.express as px
    fig5 = px.line(
                track_debris, 
                x='Year',
                y='Number of objects',
                title='Debris Tracked')
    st.plotly_chart(fig5)
    st.metric(label= "Debries Tracked in 2021", value="14336")

with tab5:
    track_payload = track.query("Entity=='Payloads'")
    import plotly.express as px
    fig6 = px.line(
                track_payload, 
                x='Year',
                y='Number of objects',
                title='Payloads Tracked')
    st.plotly_chart(fig6)
    st.metric(label= "Payloads Tracked in 2021", value="5974")

with tab6:
    track_rocket = track.query("Entity=='Rocket bodies'")
    import plotly.express as px
    fig7 = px.line(
                track_rocket, 
                x='Year',
                y='Number of objects',
                title='Body of Rockets Tracked')
    st.plotly_chart(fig7)
    st.metric(label= "Rocket Bodies Tracked in 2021", value="1495")
st.write('Dari sekian banyaknya objek angkasa yang sudah dilacak oleh organisasi international, masih lebih banyak yang belum terlacak. European Space Agency menyebutkan bahwa pada tahun 2021 sekitar lebih dari 130 juta objek serpihan (debris) berukuran lebih besar dari 1 mm berada di angkasa')
st.metric(label = 'Perkiraan objek serpihan (debris) di angkasa', value = '130000000')

#NEA
st.title('Near Earth Asteroid')
st.write('Selain objek buatan manusia, banyak benda di sekitar angkasa bumi yang bersifat alami yang disebut dengan NEA atau Near Earth Asteroid atau Asteroid Dekat Bumi. Benda alami yang berupa asteroid ini adalah hasil dari banyak fenomena langit sejak terbentuknya luar angkasa seperti tubrukan antar planet, pecahan bintang dan sebagainya.')
nea = pd.read_csv('nea_discovered.csv')
nea2 = nea.loc[:, ['Date', 'NEA', 'NEA-140m', 'NEA-km']]
import plotly.express as px
fig8 = px.line(
                nea2, 
                x='Date',
                y=nea2.columns[1:4],
                title='NEA Discovered')
st.plotly_chart(fig8)
st.metric(label = 'Asteroid dekat bumi', value = '40000')
st.write('NEA-km adalah NEA yang berdiameter 1 km atau lebih, NEA-140m adalah NEA yang berdiameter 140 m atau lebih sedangkan Near Earth Asteroid berukuran kurang dari 140 m dituliskan dengan NEA.')
st.write('Jika ditotal, ada lebih dari 40000 asteroid dekat bumi yang meramaikan luar angkasa kita. Beberapa ada yang sempat masuk ke atmosfer bumi kemudian hilang menjadi abu karena panas yang ditimbulkan oleh kecepatan atmosfer menarik benda. Beberapa yang lain tetap mengelilingi bumi dan angkasa kita menjadi satelit alami yang bertumpuk dengan satelit buatan manusia')

st.markdown("---")
st.title('Remarks')
st.write('Jadi, ada ratusan, ribuan, bahkan berjuta-juta benda/objek yang mengitari bumi dan angkasa kita, baik objek alami maupun objek buatan. Walaupun secara kasat mata tidak terlihat tapi benda/objek tersebut ada disana, sedang mengitari dan menjadi satelit bumi dengan kecepatan dan porosnya masing-masing.')
st.write('Mungkin belum terlihat atau terasa akibatnya, tapi beberapa peneliti memprediksi, jika laju peluncuran objek ke angkasa dan kemunculan asteroid dekat bumi masih seperti ini atau bahkan lebih cepat dari sekarang, maka bumi dapat memiliki cincin seperti saturnus. Yang terbuat dari objek-objek buatan ditambah objek-objek alami tersebut.')
