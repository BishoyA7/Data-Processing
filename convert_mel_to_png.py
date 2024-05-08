import numpy as np 
import librosa
import os 
import matplotlib.pyplot as plt


def audio_to_mel(file_path, image_file):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

    y, sr = librosa.load(file_path)
    ms = librosa.feature.melspectrogram(y=y, sr=sr)
    log_ms = librosa.power_to_db(ms, ref=np.max)
    librosa.display.specshow(log_ms, sr=sr)
    
    fig.savefig(image_file)
    plt.close(fig)

def create_pngs_from_wavs(input_path, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    dir = os.listdir(input_path)

    for i, file in enumerate(dir):
        input_file = os.path.join(input_path, file)
        output_file = os.path.join(output_path, file.replace('.wav', '.png'))
        audio_to_mel(input_file, output_file)

# def wav_to_mel_spectrogram(wav_file):
#     y, sr = librosa.load(wav_file)
#     mel_spec = librosa.feature.melspectrogram(y=y, sr=sr)
#     return mel_spec

# Function to convert Mel spectrogram to PNG image
# def mel_spectrogram_to_png(mel_spec, output_file):
#     mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)
#     plt.figure(figsize=(10, 4))
#     plt.imshow(mel_spec_db, cmap='viridis', origin='lower')
#     plt.axis('off')
#     plt.savefig(output_file, bbox_inches='tight', pad_inches=0)
#     plt.close()

source_dir = 'C:/Users/bisho/Vosyn/Datasets/CREMA-D_1'
output_dir = 'C:/Users/bisho/Vosyn/Datasets/CREMA-D_1_images'

# mel_spec = wav_to_mel_spectrogram(source_dir)
# mel_spectrogram_to_png(mel_spec, output_dir)

for folder in os.listdir(source_dir):
    filename = os.path.join(source_dir, folder)
    filename_1 = os.path.join(output_dir, folder)

    for file in os.listdir(filename):
        emotion_path = os.path.join(filename, file)
        emotion_path_1 =os.path.join(filename_1, file)
        for audio in os.listdir(emotion_path):
            if audio.endswith('.wav'):
                # Construct the full path to the source file
                source_path = os.path.join(emotion_path, audio)
                output_path = os.path.join(emotion_path_1, audio)

                # Create the destination directory if it doesn't exist
                create_pngs_from_wavs(emotion_path, emotion_path_1)

                print(f"Converted {filename} and saved to {output_path}")

print("Conversion complete.")