```dataviewjs
const pages = dv.pages("#workouts").where(p => (p.exercise ==" Abdominal Curl"))
const dates = pages.map(p => p.file.name)
const weight = pages.map(p => p.weight).values
const exercise = pages.map(p => p.exercise)
const chartData = {type: "line",data: {labels: dates,datasets: [{label: "Weight (kg)",data: weight,backgroundColor: ["rgba(53, 252, 167, 1)"],borderColor: ["rgba(138, 102, 204, 0.8)"],borderWidth: 1.5,spanGaps: true,}],},};
dv.span("**Abdominal Curl Tracker**")
window.renderChart(chartData, this.container)
```
# Abdominal Curl Workouts

```dataview 
TABLE date_of_workout AS "Date", sets AS "Number of Sets",reps AS "Number of Reps", weight AS "Weight in Kg" 
 SORT file.name DESC 
WHERE exercise =" Abdominal Curl"
```
### Date: 2024-08-21
- Sets: 2
- Reps: 8
- Weight: 31.5 kg
- Type: Circuit

### Date: 2024-08-21
- Sets: 1
- Reps: 6
- Weight: 5 kg
- Type: Circuit

### Date: 2024-08-21
- Sets: 1
- Reps: 8
- Weight: 18 kg
- Type: Warmup

### Date: 2024-09-10
- Sets: 1
- Reps: 8
- Weight: 18 kg
- Type: Warmup

### Date: 2024-09-10
- Sets: 1
- Reps: 10
- Weight: 25 kg
- Type: Circuit

### Date: 2024-09-10
- Sets: 1
- Reps: 10
- Weight: 31.5 kg
- Type: Circuit

### Date: 2024-09-10
- Sets: 1
- Reps: 8
- Weight: 38 kg
- Type: Circuit

### Date: 2024-09-13
- Sets: 1
- Reps: 1
- Weight: 10 kg
- Type:Circuit

### Date: 2024-09-13
- Sets: 1
- Reps: 10
- Weight: 31.5 kg
- Type:Warmup

### Date: 2024-09-13
- Sets: 1
- Reps: 8
- Weight: 38.5 kg
- Type:Circuit

### Date: 2024-09-13
- Sets: 1
- Reps: 6
- Weight: 45 kg
- Type:Failure

