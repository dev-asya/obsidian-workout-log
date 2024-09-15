```dataviewjs
const pages = dv.pages("#workouts").where(p => (p.exercise ==" Row"))
const dates = pages.map(p => p.file.name)
const weight = pages.map(p => p.weight).values
const exercise = pages.map(p => p.exercise)
const chartData = {type: "line",data: {labels: dates,datasets: [{label: "Weight (kg)",data: weight,backgroundColor: ["rgba(53, 252, 167, 1)"],borderColor: ["rgba(138, 102, 204, 0.8)"],borderWidth: 1.5,spanGaps: true,}],},};
dv.span("**Row Tracker**")
window.renderChart(chartData, this.container)
```
# Row Workouts

```dataview 
TABLE date_of_workout AS "Date", sets AS "Number of Sets",reps AS "Number of Reps", weight AS "Weight in Kg" 
 SORT file.name DESC 
WHERE exercise =" Row"
```
### Date: 2024-08-19
- Sets: 4
- Reps: 6
- Weight: 32 kg
- Type: Circuit

### Date: 2024-09-03
- Sets: 1
- Reps: 7
- Weight: 9 kg
- Type: Warmup

### Date: 2024-09-03
- Sets: 1
- Reps: 9
- Weight: 22.5 kg
- Type: Circuit

### Date: 2024-09-03
- Sets: 1
- Reps: 8
- Weight: 27 kg
- Type: Circuit

### Date: 2024-09-03
- Sets: 1
- Reps: 8
- Weight: 27 kg
- Type: Circuit

### Date: 2024-09-03
- Sets: 1
- Reps: 10
- Weight: 34 kg
- Type: Circuit

### Date: 2024-09-05
- Sets: 1
- Reps: 10
- Weight: 18 kg
- Type: Warmup

### Date: 2024-09-05
- Sets: 1
- Reps: 12
- Weight: 27 kg
- Type: Circuit

### Date: 2024-09-05
- Sets: 1
- Reps: 10
- Weight: 34 kg
- Type: Circuit

### Date: 2024-09-05
- Sets: 1
- Reps: 10
- Weight: 34 kg
- Type: Circuit

### Date: 2024-09-05
- Sets: 1
- Reps: 10
- Weight: 37 kg
- Type: Circuit

