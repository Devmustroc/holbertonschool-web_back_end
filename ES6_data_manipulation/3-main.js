import getListStudents from './0-get_list_students';
import getStudentIdsSum from './3-get_ids_sum';

const students = getListStudents();
const newVal = getStudentIdsSum(students);

console.log(newVal);
