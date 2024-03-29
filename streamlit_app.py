import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyDKcxALky8LiROaxb0RGMw8TLLOcujMRMY")
model = genai.GenerativeModel(model_name="gemini-pro")

def get_user_profile():
    # Function to collect user profile information
    reading_level_options = ["Preschool", "Elementary (K-2)", "Elementary (3-5)"]
    selected_reading_level = st.selectbox("Select your child's reading level:", reading_level_options)
    interests = st.text_input("What is your child interested in? (Separate interests with commas):")
    character = st.selectbox("Choose your favorite character:", ["Twinkle", "Maya", "Robin", "Trio"])
    return {"reading_level": selected_reading_level, "interests": interests.split(","), "character": character.lower()}

def generate_story(user_profile):
    # Generate a story based on the user profile
    reading_level = user_profile["reading_level"]
    interests = ",".join(user_profile["interests"])
    character = user_profile["character"]
    prompt = f"""
    Generate a story suitable for a {reading_level} year old child 
    who is interested in {interests} with a character named {character}.
    """
    story_segment = model.generate_content(prompt)
    return story_segment

def main():
    st.title("Interactive Storytelling")
    st.write("Once upon a time, in a magical forest...")

    if st.button("Give me a story!"):
        user_profile = get_user_profile()
        story_segment = generate_story(user_profile)
        st.write(story_segment.text)

        choice = st.radio("Do you want to continue listening to stories?", ("Yes", "No"))
        while choice == "Yes":
            st.write("You've chosen to listen to another story!")
            story_segment = generate_story(user_profile)
            st.write(story_segment.text)
            choice = st.radio("Do you want to continue listening to stories?", ("Yes", "No"))

        if choice == "No":
            st.write("You've chosen to stop listening to stories! Come back again to listen to more!")

if __name__ == "__main__":
    main()
