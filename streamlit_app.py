import streamlit as st
import subprocess

# Replace with your actual API endpoint and API key
API_ENDPOINT = "https://generativelanguage.googleapis.com"
API_KEY = "AIzaSyDKcxALky8LiROaxb0RGMw8TLLOcujMRMY"


def get_user_profile():
  reading_level_options = ["Preschool", "Elementary (K-2)", "Elementary (3-5)"]
  selected_reading_level = st.selectbox("Select your child's reading level", reading_level_options)
  reading_level_map = {"Preschool": 5, "Elementary (K-2)": 7, "Elementary (3-5)": 9}
  user_profile = {"reading_level": reading_level_map[selected_reading_level]}
  interests = st.multiselect("What is your child interested in?", ["Animals", "Adventure", "Fantasy"])
  user_profile["interests"] = interests
  return user_profile


def generate_story(user_profile):
  reading_level = user_profile["reading_level"]
  interests = ",".join(user_profile["interests"])
  prompt = f"""
  Generate a story suitable for a {reading_level} year old child 
  who is interested in {interests}. The story should be interactive 
  and allow the child to make choices that affect the outcome.
  **[INSERT STORY SEGMENT HERE]** (This part will be replaced by the generated text)
  """
  command = f"""curl -X POST -H "Authorization: Bearer {API_KEY}" -H "Content-Type: application/json" -d '{{"prompt": "{prompt}"}}' "{API_ENDPOINT}" -o output.txt"""
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  output, error = process.communicate()
  if error:
    st.error(f"Error generating story: {error.decode('utf-8')}")
    return None
  with open("output.txt", "r") as f:
    story_segment = f.read()
  subprocess.run(["rm", "output.txt"])
  return story_segment


def main():
  user_profile = get_user_profile()
  st.title("Interactive Storytelling")
  st.write("Once upon a time, in a magical forest...")
  story_segment = generate_story(user_profile)
  if story_segment:
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
