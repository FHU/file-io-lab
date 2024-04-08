# file-io-lab
This is an independent lab.  

In this lab you will read in a csv of simulated student grades, create student objects, and then calculate the class average for certain scores.  

<ins>**student.py**</ins>  
In the student.py file, create a Student class with the following attributes (don't require these as parameters in the constructor):  
1. name (default as empty string)
2. lab (default to 0): This represents the individual student's average lab grade.
3. test (default to 0):  This represents the individual student's average test grade.
4. final_exam (default to 0): This represents the individual student's final exam score.
5. overall (default to 0): This represents the individual student's overall grade in the class. 
6. letter_grade (default to empty string): This represents the overall letter grade for the class (A,B, C, D, F)
7. Write a method called calc_overall_grade(): that will calculate the student's overall grade as the unweighted average of their lab, test, and final exam scores. This will set the value of the overall attribute. (not return)
8. Write a method called calc_letter_grade(): that will determine the student's letter grade based on their overall grade. This method will set the value of the letter grade attribute. (not return)

<ins>**main.py**</ins>  
1. Read in the "file_io_lab_data.csv" that is included in the repo.
2. Each row in the file represents a single student with their lab, test, and final exam scores.
3. For each row (student) in the file, create a student object from the provided data.
4. You must then call the calc_overall_grade() and calc_letter_grade() methods for the methods.
5. Add each student to a list called students.
6. After all students have been added to the list, calculate the class average for lab, test, final exam, and overall score. Store in variables lab_avg, test_avg, final_exam_avg, and overall_avg.  

<ins>**Important Notes**</ins>. 
The data provided has bad data that you must clean up.  
1. Missing data is represetned by a #. Those must be changed to 0 score.  
2. If the score is greater than 100, change it to 100.  
3. If the score is less than 0, change it to 0.  
4. Remember to deal with the header row when processing the data.   
