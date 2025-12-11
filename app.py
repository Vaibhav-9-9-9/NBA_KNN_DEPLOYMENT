import pandas as pd 
import numpy as np 
import streamlit as st 
import pickle


with open("knn_nba.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Basketball Win Percentage Prediction")

Team_Name = st.selectbox("Team Name", ['Wizards', 'Cavaliers', 'Heat', 'Celtics', 'Lakers', 'Mavericks',
       'Raptors', 'Pacers', 'Nuggets', '76ers', 'Rockets', 'Pistons',
       'Kings', 'Bulls', 'Hornets', 'Spurs', 'Jazz', 'Warriors', 'Suns',
       'Grizzlies', 'Clippers', 'Trail Blazers', 'Knicks', 'Nets',
       'Thunder', 'Bobcats', 'Magic', 'Bucks', 'Hawks', 'Timberwolves',
       'Pelicans'])

Team_City = st.selectbox("Team City", ['Washington', 'Cleveland', 'Miami', 'Boston', 'Los Angeles',
       'Dallas', 'Toronto', 'Indiana', 'Denver', 'Philadelphia',
       'Houston', 'Detroit', 'Sacramento', 'Chicago', 'New Orleans',
       'San Antonio', 'Utah', 'Golden State', 'Phoenix', 'Memphis',
       'Portland', 'New York', 'Brooklyn', 'Oklahoma City', 'Charlotte',
       'Orlando', 'Milwaukee', 'Atlanta', 'Minnesota', 'LA'])

Home_Team = st.selectbox("Home Team", ['Cavaliers', 'Heat', 'Lakers', 'Raptors', '76ers', 'Pistons',
       'Bulls', 'Hornets', 'Jazz', 'Suns', 'Clippers', 'Trail Blazers',
       'Nets', 'Spurs', 'Bobcats', 'Magic', 'Celtics', 'Hawks', 'Knicks',
       'Thunder', 'Timberwolves', 'Warriors', 'Wizards', 'Pacers',
       'Rockets', 'Bucks', 'Mavericks', 'Grizzlies', 'Kings', 'Nuggets',
       'Pelicans'])

FG_PCT  = st.number_input("FG PCT", value=0.0, format="%.3f")
FG3_PCT = st.number_input("FG3 PCT", value=0.0, format="%.3f")
FT_PCT  = st.number_input("FT PCT", value=0.0, format="%.3f")
EFG_PCT = st.number_input("EFG PCT", value=0.0, format="%.3f")
PIE     = st.number_input("PIE", value=0.0, format="%.3f")
if st.button("Predict Win %"):
    input_df = pd.DataFrame([{
            "TEAM_NAME" : Team_Name,
            "TEAM_CITY" : Team_City,
            "HOME_TEAM" : Home_Team,
            "FG_PCT" : FG_PCT,
            "FG3_PCT" : FG3_PCT,
            "FT_PCT" : FT_PCT,
            "EFG_PCT" : EFG_PCT,
            "PIE" : PIE
            }])

    result = model.predict(input_df)[0]
    st.success(f"Predicted WIN % : {result:.2f}")