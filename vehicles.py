import streamlit as st
import pandas as pd

# Load car data from the Excel file
@st.cache_data
def load_data():
    return pd.read_excel("all-vehicles-model.xlsx")

# Load the data
data = load_data()

def show_comparison():
    st.subheader("Compare Two Toyota Cars 🚗")

    # Sidebar for car selection
    st.sidebar.header("Compare Two Toyota Cars")

    # Dropdowns for car selection
    car_models = data["Model"].unique()
    car_1 = st.sidebar.selectbox("Choose the first car:", ["Select a car"] + list(car_models))
    car_2 = st.sidebar.selectbox("Choose the second car:", ["Select a car"] + list(car_models))

    # Display comparison if both cars are selected
    if car_1 != "Select a car" and car_2 != "Select a car" and car_1 != car_2:
        car_1_data = data[data["Model"] == car_1].iloc[0]
        car_2_data = data[data["Model"] == car_2].iloc[0]

        st.subheader(f"Comparison Between **{car_1}** and **{car_2}**")

        # Side-by-side comparison
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"### {car_1}")
            for feature, value in car_1_data.items():
                st.write(f"**{feature}:** {value}")
        with col2:
            st.markdown(f"### {car_2}")
            for feature, value in car_2_data.items():
                st.write(f"**{feature}:** {value}")

        # Display 3D model if Corolla is selected
        if car_1 == "Corolla" or car_2 == "Corolla":
            st.subheader("3D Model of Toyota Corolla")
            st.markdown(
                """
                <model-viewer 
                    src="static/corolla_model.gltf" 
                    alt="A 3D model of the Toyota Corolla" 
                    auto-rotate 
                    camera-controls 
                    style="width: 100%; height: 500px;">
                </model-viewer>
                """,
                unsafe_allow_html=True,
            )

    elif car_1 == car_2 and car_1 != "Select a car":
        st.warning("Please select two different cars for comparison.")
    else:
        st.write("Select two cars from the dropdowns to compare their features.")


# Add a section for asking questions about cars
st.subheader("Ask About Any Car")
st.markdown("Type a question to learn more about any car, and we'll get the answer for you!")

# Input box for question
user_question = st.text_input("What information would you like to find about any car?")

if user_question:
    with st.spinner("Fetching the answer..."):
        try:
            # Call the ask function (assuming you have it implemented in oldlangchain)
            import oldlangchain
            response = oldlangchain.ask(user_question)
            st.success("Here's the information you requested:")
            st.markdown(f"*Q:* {user_question}")
            st.markdown(f"*A:* {response}")
        except Exception as e:
            st.error("Sorry, something went wrong while fetching the information. Please try again.")
            st.write(f"*Debug Info:* {e}")  # Optional debug info