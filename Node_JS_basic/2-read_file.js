const fs = require('fs');

function countStudents(path) {
  try {
    // Read the CSV file synchronously
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n').filter(line => line.trim() !== '');

    // Initialize an object to store the count of students in each field
    const studentsCountByField = {};

    // Process each line to count the students in each field
    for (const line of lines) {
      const [firstName, lastName, age, field] = line.split(',');
      if (field) {
        // Count the students in each field
        studentsCountByField[field] = (studentsCountByField[field] || 0) + 1;
      }
    }

    // Calculate the total number of students
    const totalStudents = Object.values(studentsCountByField).reduce((acc, count) => acc + count, 0);

    // Log the number of students in each field and the total number of students
    console.log(`Number of students: ${totalStudents}`);
    for (const field in studentsCountByField) {
      const count = studentsCountByField[field];
      console.log(`Number of students in ${field}: ${count}. List: ${getFieldList(lines, field)}`);
    }
  } catch (error) {
    // If an error occurs during reading or processing, throw the "Cannot load the database" error
    throw new Error('Cannot load the database');
  }
}

function getFieldList(lines, field) {
  // Extract the list of first names for a specific field
  const list = lines
    .filter(line => line.split(',')[3] === field)
    .map(line => line.split(',')[0])
    .join(', ');
  return list;
}

module.exports = countStudents;
