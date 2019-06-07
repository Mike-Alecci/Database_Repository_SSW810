# Complete the latestStudent function below.
"""def latestStudent(attendanceData):
    stud_rel_lateness = dict()                             #Keeps track of students and their lateness times, keys = stud_name, values = rel_lateness, lateness
    avg_date_lateness = dict()                             #Keeps track of lateness on a day and number of studs, key = date, value = total lateness, num studs
    answer = ""
    new_date = False
    count = 0
    if len(attendanceData) == 0:
        return answer
    for student_data in sorted(attendanceData):                     #We need to check in date order hence the sorted attendance data
        date, student, class_start, time_arrived = student_data
        temp_date = date
        if count != 0:
            new_date = (temp_date != prev_date)
        time_diff = int(time_arrived) - int(class_start)
        if time_diff <= 0:
            time_diff = 0
        if student not in stud_rel_lateness.keys():                 #populates the dictionary with people once they are first encountered
            stud_rel_lateness[student] = [0, 0]                     #here the first val is rel_lateness, and then temp date lateness
        if date not in avg_date_lateness.keys():                    #populates the dictionary with dates once they are first encountered
            avg_date_lateness[date] = [0,0, []]                     #Student was late
        avg_date_lateness[date][0] += time_diff                     #add to total late time
        avg_date_lateness[date][1] += 1                             #add to num studs
        avg_date_lateness[date][2].append(student)                  #use to check later on if the student has a record for this date
        if new_date != True:
            stud_rel_lateness[student][1] = time_diff               #Since only one data entry per stud per date we can make the second val in list temp
        if count != 0 and temp_date != prev_date:                   #not the first iteration, prevents error from prev_date, and we just hit a new date
            for stud in stud_rel_lateness:
                stud_temp_late_time = stud_rel_lateness[stud][1]
                if stud not in avg_date_lateness[prev_date][2]:     #This accounts for a student who has no data for this date, adds no time
                    stud_temp_late_time = 0
                avg_latetime = (avg_date_lateness[prev_date][0])/(avg_date_lateness[prev_date][1])
                rel_late = stud_temp_late_time - avg_latetime
                if rel_late <= 0:
                    rel_late = 0
                stud_rel_lateness[stud][0] += rel_late
        if new_date == True:
            stud_rel_lateness[student][1] = time_diff
        prev_date = date
        count += 1
    late_val = 0
    count = 0
    for stud in sorted(stud_rel_lateness.keys()):                          #sorting it helps us to account for ties
        if count == 0:
            answer = stud
            late_val = stud_rel_lateness[stud][0]
            count += 1
        elif stud_rel_lateness[stud][0] > late_val:
            answer = stud
            late_val = stud_rel_lateness[stud][0]
    return answer
"""     
"""
def solution(s):
    answer = ""
    for poss_num in s:
        if poss_num != " " and poss_num != "-":
            answer += poss_num
    if len(answer) <= 3:
        return answer
    elif len(answer) % 3 == 0:
        for i in range(len(answer), 3):
            answer = answer[0,i] + "-" + answer[i]
    print(answer)
s = "00-44  48 5555 83615"        
solution(s)
"""
print(int(5/2))