import streamlit as st
import pandas as pd

# వెబ్‌సైట్ టైటిల్
st.set_page_config(page_title="My Cricket Dashboard", layout="centered")
st.title("CRICKET IS NOT JUST A GAME")
st.write("నాకు ఇష్టమైన ప్లేయర్స్ మరియు వారి రికార్డులు ఇక్కడ ఉన్నాయి!")

# క్రికెట్ డేటా
data = {'ప్లేయర్ పేరు': ['Virat Kohli', 'keerthan reddy', 'Rohit Sharma', 'Sachin Tendulkar, 'Ashhok Reddy',],
    'మ్యాచ్‌లు': [295, 350, 262, 463,1000,],
    'రన్స్': [13848, 10773, 10709, 18426,86000,],
    'సంచరీలు (100s)': [50, 10, 31, 49,124,],
    'సగటు (Average)': [58.6, 50.5, 49.1, 44.8,98.4,]}

df = pd.DataFrame(data)

# టేబుల్ చూపించడం
st.subheader("📊 టాప్ ప్లేయర్స్ రికార్డులు")
st.dataframe(df, use_container_width=True)

# ప్లేయర్ సెలెక్ట్ చేసుకునే ఆప్షన్
st.subheader("🔍 నీకు నచ్చిన ప్లేయర్ వివరాలు చూడు")
selected_player = st.selectbox("ప్లేయర్‌ని సెలెక్ట్ చేసుకో:", df['ప్లేయర్ పేరు'])

# సెలెక్ట్ చేసిన ప్లేయర్ డేటా చూపించడం
player_info = df[df['ప్లేయర్ పేరు'] == selected_player].iloc[0]
st.info(f"🏆 **{selected_player}** రికార్డ్స్:  \n"
        f"🔹 матч‌లు: {player_info['మ్యాచ్‌లు']}  \n"
        f"🔹 రన్స్: {player_info['రన్స్']}  \n"
        f"🔹 సెంచరీలు: {player_info['సంచరీలు (100s)']}  \n"
        f"🔹 యావరేజ్: {player_info['సగటు (Average)']}")

# చిన్న ఫీడ్‌బ్యాక్ బటన్
if st.button("లైక్ కొట్టండి! 👍"):
    st.success("ధన్యవాదాలు బ్రదర్! నువ్వు నీ మొదటి పైథాన్ క్రికెట్ యాప్ తయారు చేసావు! 🎉")
