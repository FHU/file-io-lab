# file-io-lab
In this lab you will read in a csv of simulated student grades, create student objects, and then calculate the class average for certain scores.  
## Set Up
<ol>
	<li>Create new anaconda environment using these commands</li>
	<ul>
		<li>conda create --name fileio_lab python=3.13.1</li>
		<li>conda activate fileio_lab</li>
	</ul>
	<li>Pull starter code from GitHub Classroom</li>
	<li>Open in VS code and switch to the fileio_lab anaconda environment</li>
	<li>When the lab is complete, push code to GitHub Classroom</li>
</ol>

## Instructions
<ol>
  <li><strong>student.py</strong></li>
  In the student.py file, create a Student class with the following attributes:  
  <ol>
    <li>name (required)</li>
    <li>tests (required)</li>
    <li>final_exam (required)</li>
    <li>overall: This represents the student's overall grade and will get its value from the calc_overall_grade() method</li>
    <li>letter_grade: This represents a student's letter grade for the class (A,B,C,D,F) and will get its value from the calc_letter_grade() method</li>
  </ol>
  <br>
  Create the following methods:
  <ol>
    <li>calc_overall_grade(): This will return the student's overall grade as the unweighted average of their lab, test, and final exam scores rounded to the nearest whole number. </li>
    <li>calc_letter_grade(): This will return the student's letter grade based on their overall grade. This uses a 10-point grading scale.</li>
  </ol>
  <br>
  <li><strong>main.py</strong></li>
  <ol>
    <li>Import any files and read in the "file_io_lab_data.csv" that is included in the repo.</li>
    <li>Each row in the file represents a single student with their lab, test, and final exam scores.</li>
    <li>For each row (student) in the file, create a student object from the provided data.</li>
    <li>Add each student to a list called students.</li>
    <li>After all students have been added to the list, calculate the class average for lab, test, final exam, and overall score. Store in variables lab_avg, test_avg, final_exam_avg, and overall_avg. </li>
  </ol>
</ol>

## Important Notes
The data provided has bad data that you must clean up.
<ol>
  <li>Missing data is represetned by a '#'. Those must be changed to 0 score. </li>
  <li>If any score is greater than 100, change it to 100.</li>
  <li>If any score is less than 0, change it to 0.</li>
  <li>Remember to deal with the header row when processing the file. </li>
</ol>  
