```dataviewjs
const pages = dv.pages("#workouts").where(p => (p.exercise ==" Incline Chest Press"))
const dates = pages.map(p => p.file.name)
const weight = pages.map(p => p.weight).values
const exercise = pages.map(p => p.exercise)
const chartData = {type: "line",data: {labels: dates,datasets: [{label: "Weight (kg)",data: weight,backgroundColor: ["rgba(53, 252, 167, 1)"],borderColor: ["rgba(138, 102, 204, 0.8)"],borderWidth: 1.5,spanGaps: true,}],},};
dv.span("**Incline Chest Press Tracker**")
window.renderChart(chartData, this.container)
```
# Incline Chest Press Workouts

```dataview 
TABLE date_of_workout AS "Date", sets AS "Number of Sets",reps AS "Number of Reps", weight AS "Weight in Kg" 
 SORT file.name DESC 
WHERE exercise =" Incline Chest Press"
```
### Date: 2024-08-19
- Sets: 4
- Reps: 7
- Weight: 30 kg
- Type: Circuit

