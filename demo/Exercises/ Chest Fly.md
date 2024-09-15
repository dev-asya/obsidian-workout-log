```dataviewjs
const pages = dv.pages("#workouts").where(p => (p.exercise ==" Chest Fly"))
const dates = pages.map(p => p.file.name)
const weight = pages.map(p => p.weight).values
const exercise = pages.map(p => p.exercise)
const chartData = {type: "line",data: {labels: dates,datasets: [{label: "Weight (kg)",data: weight,backgroundColor: ["rgba(53, 252, 167, 1)"],borderColor: ["rgba(138, 102, 204, 0.8)"],borderWidth: 1.5,spanGaps: true,}],},};
dv.span("**Chest Fly Tracker**")
window.renderChart(chartData, this.container)
```
# Chest Fly Workouts

```dataview 
TABLE date_of_workout AS "Date", sets AS "Number of Sets",reps AS "Number of Reps", weight AS "Weight in Kg" 
 SORT file.name DESC 
WHERE exercise =" Chest Fly"
```
### Date: 2024-08-20
- Sets: 2
- Reps: 8
- Weight: 29 kg
- Type: Circuit

### Date: 2024-08-20
- Sets: 2
- Reps: 8
- Weight: 20 kg
- Type: Warmup

### Date: 2024-09-13
- Sets: 1
- Reps: 11
- Weight: 13.5 kg
- Type:Warmup

### Date: 2024-09-13
- Sets: 1
- Reps: 11
- Weight: 13.5 kg
- Type:Circuit

### Date: 2024-09-13
- Sets: 1
- Reps: 12
- Weight: 40 lbs kg
- Type:Circuit

### Date: 2024-09-13
- Sets: 1
- Reps: 10
- Weight: 55 lbs kg
- Type:Circuit

### Date: 2024-09-13
- Sets: 1
- Reps: 6
- Weight: 65 lbs kg
- Type:Failure

