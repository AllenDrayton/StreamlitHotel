import joblib
import pickle

import streamlit as st

# Load the model
loaded_model = joblib.load('Superhost.pkl')

def main():
    st.title("AirBnB Classification")
    st.write("Enter Your Inputs!!!!")

    st.write("Amsterdam: 0, Athens: 1, Barcelona: 2, Berlin: 3, Budapest: 4, Lisbon: 5, Paris: 6, Rome: 7, Vienna: 8")
    city = st.slider("Choose Your Desire City", 0, 8, 4)

    price = st.number_input("Enter Your Desire Price : ",step = 0.1, format="%.2f")

    st.write("Private room : 0, Entire home/apt : 1, Shared room : 2")
    RoomType = st.slider("Choose Room Type", 0, 2, 0)

    PersonCapacity = st.slider("Choose Your Desire Person Capacity", 0, 10, 5 )


    CleanlinessRating = st.slider("Rate The Cleanliness", 0, 10, 8 )

    GuestSatisfaction = st.slider("Rate Your Satisfaction ", 0, 100, 88 )

    Bedroom = st.slider("Enter Your Desire Bedroom ", 0, 10, 3 )

    if st.button("Predict Income"):
        input_data = [[city, price, RoomType, PersonCapacity, CleanlinessRating, GuestSatisfaction, Bedroom]]
        result = loaded_model.predict(input_data)
        if result == 0 :
            st.warning(f"You have Got a Non-Superhost Hotel!!!")
        elif result == 1:
            st.success(f"Congratulations!! You have Got a Superhost Hotel!!!")


if __name__ == "__main__":
    main()