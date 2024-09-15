```dataviewjs
const pages = dv.pages("#workouts").where(p => (p.exercise ==" Pec Fly"))
const dates = pages.map(p => p.file.name)
const weight = pages.map(p => p.weight).values
const exercise = pages.map(p => p.exercise)
const chartData = {type: "line",data: {labels: dates,datasets: [{label: "Weight (kg)",data: weight,backgroundColor: ["rgba(53, 252, 167, 1)"],borderColor: ["rgba(138, 102, 204, 0.8)"],borderWidth: 1.5,spanGaps: true,}],},};
dv.span("**Pec Fly Tracker**")
window.renderChart(chartData, this.container)
```
# Pec Fly Workouts

```dataview 
TABLE date_of_workout AS "Date", sets AS "Number of Sets",reps AS "Number of Reps", weight AS "Weight in Kg" 
 SORT file.name DESC 
WHERE exercise =" Pec Fly"
```
### Date: 2024-09-03
- Sets: 1
- Reps: 8
- Weight: 20 kg
- Type: Warmup

### Date: 2024-09-03
- Sets: 1
- Reps: 8
- Weight: 29 kg
- Type: Circuit

### Date: 2024-09-03
- Sets: 2
- Reps: 7
- Weight: 29 kg
- Type: Circuit

### Date: 2024-09-03
- Sets: 1
- Reps: 7
- Weight: 39 kg
- Type: Circuit

