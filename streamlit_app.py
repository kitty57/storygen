import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyDKcxALky8LiROaxb0RGMw8TLLOcujMRMY")
model = genai.GenerativeModel(model_name="gemini-pro")

def get_user_profile():
    reading_level_options = ["Preschool", "Elementary (K-2)", "Elementary (3-5)"]
    selected_reading_level = st.selectbox("Select your child's reading level:", reading_level_options)
    interests = st.text_input("What is your child interested in? (Separate interests with commas):")
    character = st.selectbox("Choose your favorite character:", ["Twinkle", "Maya", "Robin", "Trio"])
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
    who is interested in {interests} with a character named {character}.
    """
    story_segment = model.generate_content(prompt)
    return story_segment

def main():
    st.title("Come and listen to Amazing story about the character you choose!!!")
    user_profile = get_user_profile()
    if user_profile:
        while True:
            key_suffix = f"{user_profile['reading_level']}_{','.join(user_profile['interests'])}_{user_profile['character'].lower()}"
            generate_story_button_key = f"generate_story_button_{hash(key_suffix)}"
            choice_radio_key = f"choice_radio_{hash(key_suffix)}"
            if st.button("Give me a story!", key=generate_story_button_key):
                story_segment = generate_story(user_profile)
                st.write(story_segment.text)
                choice = st.radio("What would you like to do next?", ("I want to listen more!", "I'm bored, I want to quit"), key=choice_radio_key)
                if choice == "I want to listen more!":
                    continue 
                elif choice == "I'm bored, I want to quit":
                    st.write("You've chosen to stop listening to stories! Come back again to listen to more!")
                    break 
                else:
                    st.warning("Please select an option.")
    else:
        st.warning("Please enter all the values for the user profile.")

if __name__ == "__main__":
    main()
