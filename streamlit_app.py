import streamlit as st
import requests  # For making API requests to Gemini

# Placeholder for storing user profile (replace with database or other storage)
user_profile = {"reading_level": None, "interests": []}

def get_user_profile():
  # Simulate reading level assessment (replace with actual assessment logic)
  reading_level_options = ["Preschool", "Elementary (K-2)", "Elementary (3-5)"]
  selected_reading_level = st.selectbox("Select your child's reading level", reading_level_options)
  reading_level_map = {"Preschool": 5, "Elementary (K-2)": 7, "Elementary (3-5)": 9}
  user_profile["reading_level"] = reading_level_map[selected_reading_level]

  # Simulate interest selection (replace with interactive options)
  interests = st.multiselect("What is your child interested in?", ["Animals", "Adventure", "Fantasy"])
  user_profile["interests"] = interests

def generate_story(user_profile):
  reading_level = user_profile["reading_level"]
  interests = ",".join(user_profile["interests"])
  prompt = f"""
  Generate a story suitable for a {reading_level} year old child 
  who is interested in {interests}. The story should be interactive 
  and allow the child to make choices that affect the outcome.

  **[INSERT STORY SEGMENT HERE]** (This part will be replaced by the generated text)
  """
  response = requests.post("AIzaSyDKcxALky8LiROaxb0RGMw8TLLOcujMRMY", data={"prompt": prompt})
  story_segment = response.json()["text"]
  return story_segment

def main():
  # Get user profile
  if user_profile["reading_level"] is None:
    get_user_profile()

  # Display story introduction
  st.title("Interactive Storytelling")
  st.write("Once upon a time, in a magical forest...")
  story_segment = generate_story(user_profile)
  st.write(story_segment)
  choice1 = st.button("Go left")
  choice2 = st.button("Go right")
  if choice1:
    pass
  elif choice2:
    pass
  else:
    st.write("Please make a choice.")

if __name__ == "__main__":
  main()
