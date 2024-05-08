import os 
from pydub import AudioSegment

def pad_audio_to_4_seconds(audio_path, output_path):
    # Load the audio clip
    audio = AudioSegment.from_file(audio_path)

    # Calculate the duration of the audio clip 
    current_duration = len(audio) / 1000.0  # Convert milliseconds to seconds 

    # Desired duration (4 seconds)
    target_duration = 4.0 

    # Calculate the amount of silent padding needed 
    padding_duration = target_duration - current_duration

    # Generate silent audio segment for padding 
    silent_padding = AudioSegment.silent(duration=int(padding_duration * 1000))  # Convert seconds to milliseconds 

    # Concatenate the original audio with the silent padding 
    padded_audio = audio + silent_padding 

    # Export the padded audio to the output path 
    padded_audio.export(output_path, format="wav")

    print(f"Audio clip at '{audio_path}' padded to 4 seconds and saved to '{output_path}'.")

source_dir = 'C:/Users/bisho/RAVDESS'
output_dir = 'C:/Users/bisho/RAVDESS_padded'
os.makedirs(output_dir, exist_ok=True)

for folder in os.listdir(source_dir):
    folder_path = os.path.join(source_dir, folder)
    new_folder_path = os.path.join(output_dir, folder)
    os.makedirs(new_folder_path, exist_ok=True)
    for emotion in os.listdir(folder_path):
        emotion_path = os.path.join(folder_path, emotion)
        new_emotion_path = os.path.join(new_folder_path, emotion)
        os.makedirs(new_emotion_path, exist_ok=True)
        for audio in os.listdir(emotion_path):
            audio_path = os.path.join(emotion_path, audio)
            new_audio_path = os.path.join(new_emotion_path, audio)
            pad_audio_to_4_seconds(audio_path, new_audio_path)
