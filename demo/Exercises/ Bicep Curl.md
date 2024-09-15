```dataviewjs
const pages = dv.pages("#workouts").where(p => (p.exercise ==" Bicep Curl"))
const dates = pages.map(p => p.file.name)
const weight = pages.map(p => p.weight).values
const exercise = pages.map(p => p.exercise)
const chartData = {type: "line",data: {labels: dates,datasets: [{label: "Weight (kg)",data: weight,backgroundColor: ["rgba(53, 252, 167, 1)"],borderColor: ["rgba(138, 102, 204, 0.8)"],borderWidth: 1.5,spanGaps: true,}],},};
dv.span("**Bicep Curl Tracker**")
window.renderChart(chartData, this.container)
```
# Bicep Curl Workouts

```dataview 
TABLE date_of_workout AS "Date", sets AS "Number of Sets",reps AS "Number of Reps", weight AS "Weight in Kg" 
 SORT file.name DESC 
WHERE exercise =" Bicep Curl"
```
### Date: 2024-09-03
- Sets: 1
- Reps: 8
- Weight: 0 kg
- Type: Warmup

### Date: 2024-09-03
- Sets: 2
- Reps: 8
- Weight: 5 kg
- Type: Circuit

### Date: 2024-09-03
- Sets: 1
- Reps: 6
- Weight: 10 kg
- Type: Circuit

