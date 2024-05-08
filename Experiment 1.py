import os 
import matplotlib.pyplot as plt 
from keras.models import load_model
from voice_match import base_model, classify_gender, classify_emotion, audio_to_mel_to_png

gender_classifier = load_model('best_model_1.h5')
male_emotion_classifier = load_model('male_model.h5')
female_emotion_classifier = load_model('female_model_3.h5')

english_voice_samples_path = 'C:/Users/bisho/Vosyn/Datasets/RAVDESS_test_1'
num_samples = 154
correct_gender_count = 0
correct_male_emotion_count = 0
correct_female_emotion_count = 0 
correct_combined_count = 0 
male_sample_count = 0
female_sample_count = 0

for i, filename in enumerate(os.listdir(english_voice_samples_path)):
    if filename.endswith(".wav") and i < num_samples:
        actual_gender, actual_emotion, _ = filename.rstrip('.wav').split('_')
        wav_file_path = os.path.join(english_voice_samples_path, filename)
        
        mel_image_file = audio_to_mel_to_png(wav_file_path, 'temp_mel_spec.png')

        predicted_gender = classify_gender(mel_image_file, gender_classifier, base_model)

        if predicted_gender == 'Male':
            predicted_emotion = classify_emotion(mel_image_file, male_emotion_classifier, base_model)
            male_sample_count += 1 
            if predicted_emotion == actual_emotion:
                correct_male_emotion_count += 1
        else: 
            predicted_emotion = classify_emotion(mel_image_file, female_emotion_classifier, base_model)
            female_sample_count += 1 
            if predicted_emotion == actual_emotion: 
                correct_female_emotion_count += 1 

        
        if predicted_gender == actual_gender and predicted_emotion == actual_emotion:
            correct_combined_count += 1 

        if predicted_gender == actual_gender: 
            correct_gender_count += 1 

        os.remove('temp_mel_spec.png')

gender_accuracy = correct_gender_count / num_samples
male_emotion_accuracy = correct_male_emotion_count / male_sample_count
female_emotion_accuracy = correct_female_emotion_count / female_sample_count
combined_accuracy = correct_combined_count / num_samples

categories = ['Gender Accuracy', 'Male Emotion Accuracy', 'Female Emotion Accuracy', 'Combined Accuracy']
accuracies = [gender_accuracy, male_emotion_accuracy, female_emotion_accuracy, combined_accuracy]

plt.bar(categories, accuracies, color=['blue', 'green', 'red', 'purple'])
plt.xlabel('Category')
plt.ylabel('Accuracy')
plt.title('Voice Match Classification Accuracies')
plt.ylim(0, 1.0)

for i, acc in enumerate(accuracies):
    plt.text(i, acc, f'{acc:.2f}', ha='center', va='bottom')

plt.show()