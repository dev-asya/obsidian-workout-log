```dataviewjs
const pages = dv.pages("#workouts").where(p => (p.exercise ==" Overhead Press"))
const dates = pages.map(p => p.file.name)
const weight = pages.map(p => p.weight).values
const exercise = pages.map(p => p.exercise)
const chartData = {type: "line",data: {labels: dates,datasets: [{label: "Weight (kg)",data: weight,backgroundColor: ["rgba(53, 252, 167, 1)"],borderColor: ["rgba(138, 102, 204, 0.8)"],borderWidth: 1.5,spanGaps: true,}],},};
dv.span("**Overhead Press Tracker**")
window.renderChart(chartData, this.container)
```
# Overhead Press Workouts

```dataview 
TABLE date_of_workout AS "Date", sets AS "Number of Sets",reps AS "Number of Reps", weight AS "Weight in Kg" 
 SORT file.name DESC 
WHERE exercise =" Overhead Press"
```
### Date: 2024-08-21
- Sets: 1
- Reps: 4
- Weight: 30 kg
- Type: Circuit

### Date: 2024-08-21
- Sets: 3
- Reps: 6
- Weight: 20 kg
- Type: Circuit

### Date: 2024-08-19
- Sets: 4
- Reps: 6
- Weight: 20 kg
- Type: Circuit

### Date: 2024-08-23
- Sets: 1
- Reps: 7
- Weight: 13.5 kg
- Type: Warmup

### Date: 2024-08-23
- Sets: 1
- Reps: 7
- Weight: 16 kg
- Type: Circuit

### Date: 2024-08-23
- Sets: 1
- Reps: 5
- Weight: 22.5 kg
- Type: Circuit

### Date: 2024-08-23
- Sets: 1
- Reps: 7
- Weight: 16 kg
- Type: Circuit

### Date: 2024-09-05
- Sets: 1
- Reps: 10
- Weight: 13.5 kg
- Type: Warmup

### Date: 2024-09-05
- Sets: 1
- Reps: 8
- Weight: 16 kg
- Type: Circuit

### Date: 2024-09-05
- Sets: 1
- Reps: 8
- Weight: 16 kg
- Type: Circuit

### Date: 2024-09-05
- Sets: 1
- Reps: 10
- Weight: 16 kg
- Type: Circuit

### Date: 2024-09-05
- Sets: 1
- Reps: 7
- Weight: 20 kg
- Type: Circuit

