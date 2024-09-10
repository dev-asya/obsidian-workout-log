import os
import re
from collections import defaultdict

# Folder containing markdown files
input_folder_path = 'Log\workouts'
output_folder_path = 'Exercises'
# Dictionary to store data by exercise
workouts_by_exercise = defaultdict(list)

# Function to extract properties from markdown file
def extract_properties(file_content):
    properties = {}
    # Regular expression to extract properties
    regex = r"(\w+):\s*(.*)"
    matches = re.findall(regex, file_content)
    for match in matches:
        key, value = match
        properties[key] = value
    return properties

# Read each markdown file in the folder
for filename in os.listdir(input_folder_path):
    if filename.endswith('.md'):  # Ensure we're only reading markdown files
        file_path = os.path.join(input_folder_path, filename)
        
        with open(file_path, 'r') as file:
            content = file.read()
            properties = extract_properties(content)
            
            # Ensure the exercise property is in the file
            if 'exercise' in properties:
                exercise = properties['exercise']
                
                # Append the workout data to the dictionary
                workouts_by_exercise[exercise].append({
                    'date_of_workout': properties.get('date_of_workout'),
                    'sets': properties.get('sets')[1:-1],
                    'reps': properties.get('reps')[1:-1],
                    'weight': properties.get('weight'), # "[1:-1]" is not present here, because some of the workout files have weight written in imperial pounds in the form ' "X lbs" '. Instead, [1:-1] is present when writing the value.
                    'type': properties.get('type')[1:-1],                       
                    'time': properties.get('time')
                })

# Write the organized data into separate markdown files
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)  # Create the output folder if it doesn't exist

for exercise, workouts in workouts_by_exercise.items():
    # Create a markdown file for each exercise
    exercise_to_string = str({exercise})
    file_name = exercise_to_string[3:-3] + ".md"
    output_file_path = os.path.join(output_folder_path, file_name)
    
    with open(output_file_path, 'w') as output_file:
        output_file.write(f"#{exercise[1:-1]} Workouts\n\n")
    


        for workout in workouts:
            output_file.write(f"### Date: {workout['date_of_workout'][1:-1]}\n")
            output_file.write(f"- Sets: {workout['sets']}\n")
            output_file.write(f"- Reps: {workout['reps']}\n")

            output_file.write(f"- Weight: {workout['weight'][1:-1]}\n")

            output_file.write(f"- Type: {workout['type']}\n\n")
    print(f"File written: {output_file_path}")