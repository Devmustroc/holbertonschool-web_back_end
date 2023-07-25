const fs = require('fs');

export default function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
      } else {
        const [headerLine, ...body] = data.split('\n').filter((line) => line.length > 0);
        const headers = headerLine.split(',');
        const students = body.map((line) => line.split(',').reduce((student, field, index) => Object.assign(student, { [headers[index]]: field }), {}));
        const fieldsGroup = students.reduce((res, student) => {
          res[student.field] = res[student.field] || [];
          res[student.field].push(student.firstname);
          return res;
        }, {});
        resolve(fieldsGroup);
      }
    });
  });
}
