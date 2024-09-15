```dataviewjs
const pages = dv.pages("#workouts").where(p => (p.exercise ==" Calf Raises"))
const dates = pages.map(p => p.file.name)
const weight = pages.map(p => p.weight).values
const exercise = pages.map(p => p.exercise)
const chartData = {type: "line",data: {labels: dates,datasets: [{label: "Weight (kg)",data: weight,backgroundColor: ["rgba(53, 252, 167, 1)"],borderColor: ["rgba(138, 102, 204, 0.8)"],borderWidth: 1.5,spanGaps: true,}],},};
dv.span("**Calf Raises Tracker**")
window.renderChart(chartData, this.container)
```
# Calf Raises Workouts

```dataview 
TABLE date_of_workout AS "Date", sets AS "Number of Sets",reps AS "Number of Reps", weight AS "Weight in Kg" 
 SORT file.name DESC 
WHERE exercise =" Calf Raises"
```
### Date: 2024-09-10
- Sets: 1
- Reps: 10
- Weight: 0 kg
- Type: Warmup

### Date: 2024-09-10
- Sets: 1
- Reps: 9
- Weight: 13.5 kg
- Type: Circuit

### Date: 2024-09-10
- Sets: 1
- Reps: 9
- Weight: 35 lbs kg
- Type: Circuit

