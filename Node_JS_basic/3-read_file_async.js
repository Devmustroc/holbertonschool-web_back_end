const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    console.log("After!");
    fs.promises.readFile(path, 'utf8')
      .then((data) => {
        const lines = data.trim().split('\n');

        if (lines.length === 0) {
          reject(new Error('Cannot load the database'));
        }

        const counts = {};

        for (const line of lines) {
          const [firstname, lastname, age, field] = line.split(',');
          if (field) {
            if (!counts[field]) {
              counts[field] = {
                count: 0,
                list: []
              };
            }
            counts[field].count++;
            counts[field].list.push(firstname);
          }
        }

        console.log(`Number of students: ${lines.length}`);

        for (const field in counts) {
          console.log(`Number of students in ${field}: ${counts[field].count}. List: ${counts[field].list.join(', ')}`);
        }

        resolve();
      })
      .catch((error) => {
        reject(new Error('Cannot load the database'));
      })
      .finally(() => {
        console.log("Done!");
      });
  });
}

module.exports = countStudents;
