export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  const students = getListStudents;
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const studentGrade = newGrades.filter((grade) => grade.studentId === student.id)[0];
      return {
        ...student,
        grade: studentGrade ? studentGrade.grade : 'N/A',
      };
    });
}
