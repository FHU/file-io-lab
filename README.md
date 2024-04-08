# file-io-lab
This is an independent lab.  

In this lab you will read in a csv of simulated student grades, create student objects, and then calculate the class average for certain scores.  

Student.py  
1. Create a Student class with the following attributes (don't require these as parameters in the constructor):
2. name (default as empty string)
3. lab (default to 0): This represents the individual student's average lab grade.
5. test (default to 0):  This represents the individual student's average test grade.
6. final_exam (default to 0): This represents the individual student's final exam score.
7. overall (default to 0): This represents the individual student's overall grade in the class. 
8. letter_grade (default to empty string): This represents the overall letter grade for the class (A,B, C, D, F)
9. Write a method called calc_overall_grade(): that will calculate the student's overall grade as the unweighted average of their lab, test, and final exam scores. This will set the value of the overall attribute. (not return)
10. Write a method called calc_letter_grade(): that will determine the student's letter grade based on their overall grade. This method will set the value of the letter grade attribute. (not return)

Main   
1. Read in the "file_io_lab_data.csv" that is included in the repo.
2. Each row in the file represents a single student with their lab, test, and final exam scores.
3. For each row (student) in the file, create a student object from the provided data.
4. Add each student to a list called students.
5. After all students have been added to the list, calculate the class average for lab, test, final exam, and overall score. Store in variables lab_avg, test_avg, final_exam_avg, and overall_avg.
