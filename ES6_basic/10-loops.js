export default function appendToEachArrayValue(array, appendString) {
  let output = [];
  for (let value of array) {
    output.push(appendString + value);
  }
  return output;
}
