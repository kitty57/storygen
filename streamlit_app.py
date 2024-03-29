import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyDKcxALky8LiROaxb0RGMw8TLLOcujMRMY")
model = genai.GenerativeModel(model_name="gemini-pro")

def get_user_profile():
    reading_level_options = ["Preschool", "Elementary (K-2)", "Elementary (3-5)"]
    selected_reading_level = st.selectbox("Select your child's reading level:", reading_level_options)
    interests = st.text_input("What is your child interested in? (Separate interests with commas):")
    characters = {
        "Twinkle":"https://th.bing.com/th/id/OIP.wO1fi5o9K_cuTqKoEkylKgAAAA?rs=1&pid=ImgDetMain",
        "Maya":"https://th.bing.com/th/id/OIP.3mHNwJMuJEd5O7UGv0HW5gHaNK?rs=1&pid=ImgDetMain",
        "Tia":"https://th.bing.com/th/id/OIP.aCDDfBfOVZ5ggZC5sgvd3wHaHa?rs=1&pid=ImgDetMain",
        "lily":"https://img.freepik.com/premium-photo/cute-girl-happy-cartoon-character_74102-2378.jpg"
    }
    
    character = st.selectbox("Choose your favorite character:", list(characters.keys()), format_func=lambda x: f'<img src="{characters[x]}" style="width:100px;"> {x}', help="Click on the character to select")
    if selected_reading_level and interests and character:
        return {"reading_level": selected_reading_level, "interests": interests.split(","), "character": character.lower()}
    else:
        return None

def generate_story(user_profile):
    reading_level = user_profile["reading_level"]
    interests = ",".join(user_profile["interests"])
    character = user_profile["character"]
    prompt = f"""
    Generate a story suitable for a {reading_level} year old child 
    who is interested in {interests} with the protoganist being a girl named {character}.
    """
    story_segment = model.generate_content(prompt)
    return story_segment

def main():
    st.title("Come and listen to Amazing story about the character you choose!!!")
    user_profile = get_user_profile()
    if user_profile:
        if st.button("Give me a story!"):
            story_segment = generate_story(user_profile)
            st.info(story_segment.text)
            st.write("What would you like to do next?")
            if st.button("Generate Another Story"):
                story_segment = generate_story(user_profile)
                st.info(story_segment.text)
            if st.button("Stop Listening"):
                st.write("You've chosen to stop listening to stories! Come back again to listen to more!")
    else:
        st.warning("Please enter all the values for the user profile.")

if __name__ == "__main__":
    main()
