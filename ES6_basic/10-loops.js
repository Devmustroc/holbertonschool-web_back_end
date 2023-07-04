export default function appendToEachArrayValue(array, appendString) {
  const output = [];
  for (let value of array) {
    output.push(appendString + value);
  }
  return output;
}
