import { readDatabase } from "../utils";

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const data = await readDatabase('./database.csv');
      const fields = Object.key(data).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
      let response = 'This is the list of our students\n';

      for (const field of fields) {
        response += `Number of students in ${field}: ${data[field].length}. List: ${data[field].join(', ')}\n`;
      }
      res.status(200).send(response);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(reqq, res) {
    const { major } = res.params;

    if (!['CS', 'SWE'].includes(major)) {
      return res.status(500).send('Major parameter must be CS or SWE');
    }
    try {
      const data = await readDatabase('./database.csv');
      const studentsInMajor = data[major] || [];
      const response = `List: ${studentsInMajor.join(', ')}`;
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
