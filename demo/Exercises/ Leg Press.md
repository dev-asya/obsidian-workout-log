```dataviewjs
const pages = dv.pages("#workouts").where(p => (p.exercise ==" Leg Press"))
const dates = pages.map(p => p.file.name)
const weight = pages.map(p => p.weight).values
const exercise = pages.map(p => p.exercise)
const chartData = {type: "line",data: {labels: dates,datasets: [{label: "Weight (kg)",data: weight,backgroundColor: ["rgba(53, 252, 167, 1)"],borderColor: ["rgba(138, 102, 204, 0.8)"],borderWidth: 1.5,spanGaps: true,}],},};
dv.span("**Leg Press Tracker**")
window.renderChart(chartData, this.container)
```
# Leg Press Workouts

```dataview 
TABLE date_of_workout AS "Date", sets AS "Number of Sets",reps AS "Number of Reps", weight AS "Weight in Kg" 
 SORT file.name DESC 
WHERE exercise =" Leg Press"
```
### Date: 2024-09-10
- Sets: 1
- Reps: 8
- Weight: 40.5 kg
- Type: Warmup

### Date: 2024-09-10
- Sets: 1
- Reps: 10
- Weight: 58.5 kg
- Type: Circuit

### Date: 2024-09-10
- Sets: 1
- Reps: 10
- Weight: 67.5 kg
- Type: Circuit

### Date: 2024-09-10
- Sets: 1
- Reps: 10
- Weight: 155 lbs kg
- Type: Circuit

### Date: 2024-09-10
- Sets: 1
- Reps: 10
- Weight: 160 lbs kg
- Type: Circuit

### Date: 2024-09-10
- Sets: 1
- Reps: 10
- Weight: 76.5 kg
- Type: Circuit

### Date: 2024-09-10
- Sets: 1
- Reps: 8
- Weight: 175 lbs kg
- Type: Circuit

