```dataview
table date_of_workout AS Date, sets AS Sets, reps AS Reps, weight AS "Weight (kg)"
from "Log/workouts"
where exercise = " Overhead Press"
sort date_of_workout asc
