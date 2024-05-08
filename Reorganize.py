import shutil
from pathlib import Path

files_path = Path("C:/Users/bisho/Downloads/archive")

for actor_dir in files_path.iterdir():
    if actor_dir.is_dir() and actor_dir.name.startswith('Actor_'):
        old_name = actor_dir.stem
        actor, number = old_name.split('_')
        new_number = int(number) + 10
        name_1 = "00" + str(new_number)

        if int(name_1) % 2 != 0:
                    new_name = name_1 + " - Male"
        else: 
                    new_name = name_1 + " - Female"
        new_actor_dir = actor_dir.with_name(new_name)
        actor_dir.rename(new_actor_dir)

    for file in actor_dir.iterdir():
        if file.name.startswith('03'):
            inner_name = file.stem 
            modality, channel, emotion, emotional_intensity, statement, repetition, actor = inner_name.split('-')

            emotions_mapping = {
                "01": "Neutral",
                "02": "Calm",
                "03": "Happy",
                "04": "Sad",
                "05": "Angry",
                "06": "Fearful",
                "07": "Disgust",
                "08": "Surprised"
            }
            
            emotion_type = emotions_mapping.get(emotion, "Unknown")

            new_folder_path = file.with_name(f"{emotion_type}")
            if not new_folder_path.exists():
                new_folder_path.mkdir(parents=True, exist_ok=True)

            new_file_path = new_folder_path / file.name
            shutil.move(file, new_file_path)

        elif file.is_dir() and file.name.startswith(('Angry', 'Calm', 'Disgust', 'Fearful', 'Happy', 'Sad', 'Surprised')):
            for file_dir in file.iterdir():
                inner_name = file_dir.stem
                modality, channel, emotion, emotional_intensity, statement, repetition, actor = inner_name.split('-')
                if emotional_intensity == "01":
                    if file_dir.is_file() and file_dir.suffix == ".wav":
                        file_dir.unlink()
        
         

                  

            

    