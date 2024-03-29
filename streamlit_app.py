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
        story_generated = False 
        iteration_count = 0 
        while True:
            if not story_generated:
                iteration_count += 1
                generate_story_button_key = f"generate_story_button_{iteration_count}"

                if st.button("Give me a story!", key=generate_story_button_key):
                    story_segment = generate_story(user_profile)
                    st.write(story_segment.text)
                    story_generated = True 

            if story_generated:
                choice_radio_key = f"choice_radio_{iteration_count}"
                choice = st.radio("What would you like to do next?", ("I want to listen more!", "I'm bored, I want to quit"), key=choice_radio_key)
                if choice == "I want to listen more!":
                    story_generated = False  
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
