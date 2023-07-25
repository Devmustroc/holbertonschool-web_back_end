import readDatabase from "../utils";

export default class StudentsController {
  static getAllStudents(req, res, path) {
    readDatabase(path).then((result) => {
      const students = [];
      students.push('This is the list of our students');
      Object.keys(result).sort().forEach((key) => {
        students.push(`Number of students in ${key}: ${result[key].length}. List: ${result[key].join(', ')}`);
      });
      response.status(200);
      response.send(students.join('\n'));
    }).catch((error) => {
      response.status(500);
      response.send(error.message);
    });
  }

  static getAllStudentsByMajor(req, res, path) {
    const { major } = req.params;
    if (major !== 'CS' && major !== 'SWE') {
      response.status(500);
      response.send('Major parameter must be CS or SWE');
    } else {
      readDatabase(path).then((result) => {
        response.status(200);
        response.send(`List: ${result[major].join(', ')}`);
      }).catch((error) => {
        response.status(500);
        response.send(error.message);
      });
    }
  }
}
