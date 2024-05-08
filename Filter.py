import os
from pydub import AudioSegment

def keep_3_second_clips(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each audio file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".wav"):
            file_path = os.path.join(input_folder, filename)

            try:
                # Load the audio file
                audio = AudioSegment.from_file(file_path)

                # Check if the audio duration is between 2.7 and 3 seconds
                if 2700 <= len(audio) <= 3000:
                    output_path = os.path.join(output_folder, filename)

                    # Save the 3-second clips
                    audio.export(output_path, format="mp3")

                else:
                    print(f"Skipped {filename}: Invalid duration ({len(audio)} ms)")

            except Exception as e:
                print(f"Skipped {filename}: Error loading file - {str(e)}")

    print("Processing complete.")

source_dir = 'C:/Users/bisho/ESD & RAVDESS - Copy'

for foldername in os.listdir(source_dir):
    source_path = os.path.join(source_dir, foldername)
    folder_name = foldername 
    os.chdir(source_path)
     
    for emotion in os.listdir():
        emotion_path = os.path.join(source_path, emotion)
        if os.path.isdir(emotion_path):
            concat = emotion + '_trimmed'
            new_emotion_path = os.path.join(source_path, concat)
            keep_3_second_clips(emotion_path, new_emotion_path)