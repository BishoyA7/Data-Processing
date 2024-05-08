import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
import shutil 
import wave

def is_numeric_ending(file_name):
    # Check if the file name ends with a number
    return file_name[-1].isdigit()

def combine_wav_files(input_files, output_file):
    # Open the first WAV file to get parameters
    with wave.open(input_files[0], 'rb') as first_file:
        num_channels = first_file.getnchannels()
        sample_width = first_file.getsampwidth()
        frame_rate = first_file.getframerate()

    # Create a new WAV file for writing
    with wave.open(output_file, 'wb') as output_wave:
        output_wave.setnchannels(num_channels)
        output_wave.setsampwidth(sample_width)
        output_wave.setframerate(frame_rate)

        for input_file in input_files:
            try:
                # Open each input file
                with wave.open(input_file, 'rb') as input_wave:
                    # Read audio data from the input file
                    audio_data = input_wave.readframes(input_wave.getnframes())

                    # Write audio data to the output file
                    output_wave.writeframes(audio_data)
            except wave.Error as e:
                print(f"Skipping {input_file} due to the following error: {e}")

    print(f'WAV files combined successfully: {output_file}')


def combine_wav_files_in_directory(input_directory, output_directory):
    # List all files in the input directory
    all_files = os.listdir(input_directory)

    # Filter out only WAV files
    wav_files = [file for file in all_files if file.lower().endswith('.wav')]

    # Sort the files for consistent processing order
    wav_files.sort()

    for foldername in os.listdir(input_directory):
        base_name, extension = os.path.splitext(foldername)
        actor, word, emotion = base_name.split('_')

    # Process files in groups of 10
    for i in range(0, len(wav_files), 10):
        # Extract the current group of 10 files
        current_files = wav_files[i:i+10]

        # Create the output file name
        output_file = f'{output_directory}/{actor}_{emotion}_{i//10 + 1:04d}.wav'

        # Combine the current group of 10 files into one
        combine_wav_files([os.path.join(input_directory, file) for file in current_files], output_file)

def delete_non_combined_wav_files(directory, combined_files):
    # List all files in the directory
    all_files = os.listdir(directory)

    # Filter out only WAV files without numeric endings and not in the list of combined files
    non_combined_wav_files = [file for file in all_files if file.lower().endswith('.wav') and not is_numeric_ending(file) and file not in combined_files]

    # Delete each non-combined WAV file
    for file_to_delete in non_combined_wav_files:
        file_path = os.path.join(directory, file_to_delete)
        os.remove(file_path)
        print(f'Deleted: {file_path}')

source_dir = 'C:/Users/bisho/Vosyn/TESS Toronto emotional speech set data_1'

for foldername in os.listdir(source_dir):
    source_path = os.path.join(source_dir, foldername)

     # Check if the path is a directory
    if os.path.isdir(source_path):
        combined_files = []  # List to store the names of combined files
        # Combine WAV files in the emotion folder
        combine_wav_files_in_directory(source_path, source_path)
        # # Store the names of combined files
        # for i in range(0, len(os.listdir(source_path)), 10):
        #     combined_files.append(f'{foldername}_{i//10 + 1:04d}.wav')
        # # Delete non-combined WAV files in the emotion folder
        # delete_non_combined_wav_files(source_path, combined_files)
        
        