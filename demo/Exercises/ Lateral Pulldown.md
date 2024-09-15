```dataviewjs
const pages = dv.pages("#workouts").where(p => (p.exercise ==" Lateral Pulldown"))
const dates = pages.map(p => p.file.name)
const weight = pages.map(p => p.weight).values
const exercise = pages.map(p => p.exercise)
const chartData = {type: "line",data: {labels: dates,datasets: [{label: "Weight (kg)",data: weight,backgroundColor: ["rgba(53, 252, 167, 1)"],borderColor: ["rgba(138, 102, 204, 0.8)"],borderWidth: 1.5,spanGaps: true,}],},};
dv.span("**Lateral Pulldown Tracker**")
window.renderChart(chartData, this.container)
```
# Lateral Pulldown Workouts

```dataview 
TABLE date_of_workout AS "Date", sets AS "Number of Sets",reps AS "Number of Reps", weight AS "Weight in Kg" 
 SORT file.name DESC 
WHERE exercise =" Lateral Pulldown"
```
### Date: 2024-08-21
- Sets: 1
- Reps: 7
- Weight: 30 kg
- Type: Circuit

### Date: 2024-08-21
- Sets: 1
- Reps: 7
- Weight: 22.5 kg
- Type: Warmup

### Date: 2024-08-20
- Sets: 4
- Reps: 7
- Weight: 20 kg
- Type: Circuit

### Date: 2024-08-21
- Sets: 3
- Reps: 7
- Weight: 27.5 kg
- Type: Circuit

### Date: 2024-08-19
- Sets: 4
- Reps: 7
- Weight: 27 kg
- Type: Circuit

### Date: 2024-09-03
- Sets: 1
- Reps: 9
- Weight: 20 kg
- Type: Warmup

### Date: 2024-09-03
- Sets: 1
- Reps: 9
- Weight: 30 kg
- Type: Circuit

### Date: 2024-09-03
- Sets: 1
- Reps: 6
- Weight: 30 kg
- Type: Circuit

### Date: 2024-09-13
- Sets: 2
- Reps: 9
- Weight: 20 kg
- Type:Circuit

### Date: 2024-09-13
- Sets: 1
- Reps: 8
- Weight: 25 kg
- Type:Circuit

