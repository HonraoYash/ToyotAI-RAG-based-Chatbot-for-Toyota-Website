import streamlit as st

def show_inventory():
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