import streamlit as st
from pathlib import Path
import uuid

from utils import voice_clone, face_animator
from config import VOICE_CLONING_API, FACE_ANIMATOR_API

st.set_page_config(
    page_title="My Talking Clone"
)

st.title("MTC Video Generation")
# st.image(res, width = 800)

st.markdown("**Please fill the below form :**")
with st.form(key="Form :", clear_on_submit = True):
    name = st.text_input("Video Title : ").replace(" ", "")
    Sentance = st.text_input("Paragraph : ")
    image_File = st.file_uploader(label = "Upload Image file", type=["png","jpg", "jpeg"])
    audio_File = st.file_uploader(label = "Upload Audio file", type=["wav"])
    Submit = st.form_submit_button(label='Submit')
    

if Submit :
    st.markdown("**File Uploaded Sucessfully.**")

    save_folder = 'Uploaded'
    save_img_path = Path(save_folder, image_File.name)
    with open(save_img_path, mode='wb') as w:
        w.write(image_File.getvalue())

    if save_img_path.exists():
        st.success(f'File {image_File.name} is successfully saved!')

    save_audio_path = Path(save_folder, audio_File.name)
    with open(save_audio_path, mode='wb') as w:
        w.write(audio_File.getvalue())
    if save_audio_path.exists():
        st.success(f'File {audio_File.name} is successfully saved!')

    output_folder = "Output"
    file_name = name + "_" + str(uuid.uuid4()) + ".wav"
    audio_file_name = Path(output_folder, file_name)
    audio_data = None
    with st.spinner("Voice Cloning..."):
        data = voice_clone(VOICE_CLONING_API, name = name, sentance = Sentance, voice_path1=save_audio_path, voice_path2 = save_audio_path)
        audio_data = data
        with open(audio_file_name, "wb") as f:
            f.write(data)
        f.close()
    if audio_file_name.exists():
        st.success("Voice Cloned.")
        st.audio(audio_data)
    
    file_name = name + "_" + str(uuid.uuid4()) + ".mp4"
    video_data = None
    video_file_name = Path(output_folder, file_name)
    with st.spinner("Generating Video..."):
        video_data = face_animator(FACE_ANIMATOR_API, name, save_img_path, audio_file_name)
        with open(video_file_name, 'wb') as f:
            f.write(video_data)
        f.close()
    
    if video_file_name.exists():
        st.success("Video Generated.")
        st.video(video_data)
    



