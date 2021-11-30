import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
import webbrowser


im = Image.open('./fifa20.png')
st.image(im,width = 700,caption = "Fifa 2021")
# loading in the model to predict on the data
pickle_in = open('model.pkl', 'rb')
classifier = pickle.load(pickle_in)

def welcome():
    return 'Home Of Fifa'

# defining the function which will make the prediction using our model

def prediction(movement_reactions,dribbling,passing,	attacking_short_passing,potential ,power_shot_power,mentality_composure,mentality_vision):

    prediction = classifier.predict(
        [[movement_reactions,dribbling,passing,	attacking_short_passing,potential ,power_shot_power,mentality_composure,mentality_vision]])
    print(prediction)
    return prediction
    

    # this is the main function in which we define our webpage
def main():
    # giving the webpage a title
    #st.title("Fifa Overall Player Rating Prediction")
    
    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:orange;padding:13px">
    <h1 style ="color:black;text-align:center;">Fifa Player Overall Rating Prediction </h1>
    </div>
    """
    
    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
    
    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    st.sidebar.title("please enter the parameters")  # get input values
    movement_reactions = st.sidebar.slider('movement_reactions')
    mentality_composure = st.sidebar.slider("mentality_composure")
    potential = st.sidebar.slider("potential")
    passing = st.sidebar.slider("passing")
    power_shot_power = st.sidebar.slider("power_shot_power")
    dribbling = st.sidebar.slider("dribbling")
    mentality_vision = st.sidebar.slider("mentality_vision")
    attacking_short_passing = st.sidebar.slider("attacking_short_passing")
    result =""
    
    
    #predict button
    if st.button("Predict"):
        result = prediction(movement_reactions,dribbling,passing,attacking_short_passing,potential ,power_shot_power,mentality_composure,mentality_vision)
    st.success('The output is {}'.format(result))

    #source code button
    url = 'https://colab.research.google.com/drive/1sjLiOT-MnVYYxpPjrABIufNOAWqmivBd?usp=sharing'

    if st.button('Video'):
        webbrowser.open_new_tab(url)


url = url = 'https://colab.research.google.com/drive/1sjLiOT-MnVYYxpPjrABIufNOAWqmivBd?usp=sharing'

if st.button('Source Code'):
    webbrowser.open_new_tab(url)



    
if __name__=='__main__':
    main()
