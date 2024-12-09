param ( [int]$day)

$python_file = "day_$day/challenge_1.py"

New-Item "day_$day" -ItemType Directory
New-Item "day_$day/challenge_1.py" -ItemType File
New-Item "day_$day/trial.in" -ItemType File
New-Item "day_$day/input.in" -ItemType File

"import sys`n`n" | Add-Content $python_file
"with open('day_$day/' + sys.argv[1]) as file:" | Add-Content $python_file
"    data = file.read().strip()`n`n" | Add-Content $python_file
"print(data)" | Add-Content $python_file

