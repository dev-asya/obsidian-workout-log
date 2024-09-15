import os
import re
from collections import defaultdict

# Folder containing markdown files
input_folder_path = 'demo\Log\workouts'
output_folder_path = 'demo\Exercises'
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
                    'type': properties.get('type')[3:-1],                       
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


        Graph1 = '```dataviewjs\nconst pages = dv.pages("#workouts").where(p => (p.exercise =='
        Graph2 = '))\nconst dates = pages.map(p => p.file.name)\nconst weight = pages.map(p => p.weight).values\nconst exercise = pages.map(p => p.exercise)\nconst chartData = {type: "line",data: {labels: dates,datasets: [{label: "Weight (kg)",data: weight,backgroundColor: ["rgba(53, 252, 167, 1)"],borderColor: ["rgba(138, 102, 204, 0.8)"],borderWidth: 1.5,spanGaps: true,}],},};\ndv.span("**'
        Graph3 = ' Tracker**")\nwindow.renderChart(chartData, this.container)\n```\n'
        Graph = Graph1 + exercise + Graph2 + exercise[2:-1] + Graph3

        output_file.write(f"{Graph}")



        output_file.write(f"#{exercise[1:-1]} Workouts\n\n")
        Table1 = '```dataview \nTABLE date_of_workout AS "Date", sets AS "Number of Sets",reps AS "Number of Reps", weight AS "Weight in Kg" \nWHERE exercise =' 
        Table2 = "\n```\n"
        Table = Table1 + exercise + Table2   
        output_file.write(f"{Table}")
        
        for workout in workouts:
            output_file.write(f"### Date: {workout['date_of_workout'][1:-1]}\n")
            output_file.write(f"- Sets: {workout['sets']}\n")
            output_file.write(f"- Reps: {workout['reps']}\n")

            output_file.write(f"- Weight: {workout['weight'][1:-1]} kg\n")

            output_file.write(f"- Type:{workout['type']}\n\n")
    print(f"File written: {output_file_path}")