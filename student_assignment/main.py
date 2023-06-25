import numpy as np
import matplotlib.pyplot as plt

# Q1: Load the dataset "student_data.csv" into a NumPy array, using np.genfromtxt.
# Load the data from a CSV file
student_data = np.array(np.genfromtxt('./data/student_data.csv', delimiter=',', names=True, dtype=None, encoding='utf-8'))

# Q2: Calculate the following statistics for the student data:
# Q2.1: Average test score.
avg_test_score = np.mean(student_data['TestScore'])

print(f'1. The average test score of all students is {avg_test_score}')

# Q2.2: Minimum and maximum test scores.
# Get the minimum and maximum test scores
min_test_score = np.min(student_data['TestScore'])
max_test_score = np.max(student_data['TestScore'])

print(f'2. The minimum test score achieved is {min_test_score} and the maximum is {max_test_score}')

# Q2.3: Standard deviation of study hours.
# Get the standard deviation of study hours
std_study_hours = np.std(student_data['StudyHours'])

print(f'3. The standard deviation of study hours is {std_study_hours}')

# Q3: Find the students who achieved the highest test scores.
# Find the student ids of the students with the highest test scores
highest_students = np.array(np.argwhere(student_data['TestScore'] == np.max(student_data['TestScore'])))

# Extract the IDs of the highest-scoring students
student_ids = student_data['StudentID'][highest_students]

# Extract the individual indices of the highest-scoring students
students_who_achieved_hts =  [int(idx[0]) for idx in student_ids]

print(f'4. The students who achieved the highest test scores are: {students_who_achieved_hts}')

# Q4: Find the age and test score of the youngest student.
# Find the index of the youngest student
youngest_std_idx = np.argmin(student_data['Age'])

# Get the age and test score of the youngest student
youngest_std_age = student_data['Age'][youngest_std_idx] 
youngest_std_test_score = student_data['TestScore'][youngest_std_idx] 

print(f'5. The test score of the youngest student, aged {youngest_std_age}, is: {youngest_std_test_score}')

# Q5: Filter the dataset to include only female students and save it as a new file named "female_students.csv".
# Create a boolean mask for female students
female_mask = student_data['Gender'] == 'Female'

# Filter the student data to include only female students
female_data = student_data[female_mask]

# Create the filtered data to a new CSV file
np.savetxt('female_students.csv', female_data, delimiter=',', fmt='%s', header=','.join(female_data.dtype.names))

print(f'6. The dataset for female students has been saved as female_students.csv.')

# Q6: Calculate the average study hours for male students.
# Create a boolean mask for male students
male_mask = student_data['Gender'] == 'Male'

# Filter the student data to include only male students
male_data = student_data[male_mask]

avg_study_hours_for_male = np.mean(male_data['StudyHours'])

# Print the average study hours for male students to the console with formatting
print(f'7. On average, male students study for {avg_study_hours_for_male} hours.')

# Q7: Calculate the percentage of students who passed the test (grade >= 60). See if you can draw any conclusions from this information.
# Calculate the percentage of students who passed the test (grade >= 60)
passing_percentage = 100 * np.sum(student_data['TestScore'] >= 60) / len(student_data['TestScore'])

# Get the total of students who passed the test (grade >= 60)
total_passing_students= np.argwhere(student_data['TestScore'] >= 60)

# Print the percentage of students who passed the test (grade >= 60) to the console with formatting
print(f'8. {np.size(total_passing_students)} of students passed the test, indicating {passing_percentage}%.')

# Q8: Visualize the distribution of test scores using a histogram.
scores = np.array(student_data['TestScore'])

plt.hist(scores, bins=10, width=5)

plt.xlabel('Test Scores')
plt.ylabel('Frequency')
plt.title('Distribution of Test Scores')

plt.show()