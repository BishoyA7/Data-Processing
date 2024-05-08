from pydub import AudioSegment
import os 

def convert_to_wav(input_file, output_file):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Create a new stereo audio with two channels
    stereo_audio = AudioSegment.silent(duration=len(audio))
    stereo_audio = stereo_audio.set_channels(2)

    # Set the first channel with the original audio
    stereo_audio = stereo_audio._spawn(audio.raw_data, overrides={
        "channels": 1,
        "sample_width": audio.sample_width,
        "frame_rate": audio.frame_rate,
    })

    # Set the second channel with the same content
    stereo_audio = stereo_audio._spawn(audio.raw_data, overrides={
        "channels": 1,
        "sample_width": audio.sample_width,
        "frame_rate": audio.frame_rate,
    })

    # Convert to 16-bit PCM format
    stereo_audio = stereo_audio.set_sample_width(2)

    # Export as WAV file
    stereo_audio.export(output_file, format="wav")
    print(f"Conversion successful: {output_file}")
          
source_dir = 'C:/Users/bisho/EmoV-db'

for foldername in os.listdir(source_dir):
    source_path = os.path.join(source_dir, foldername)
    folder_name = foldername
    number, gender = folder_name.split(' - ')
    os.chdir(source_path)

    for emotion in os.listdir():
        emotion_path = os.path.join(source_path, emotion)
        if os.path.isdir(emotion_path):
            new_name = number + '_' + emotion 
            os.chdir(emotion_path)
            for i, audio in enumerate(os.listdir()):
                audio_name = new_name + f'_000{i+1}.wav' 
                audio_path = os.path.join(emotion_path, audio)
                new_audio_path = os.path.join(emotion_path, audio_name)
                convert_to_wav(audio_path, new_audio_path)

