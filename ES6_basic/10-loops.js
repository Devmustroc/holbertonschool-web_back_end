export default function appendToEachArrayValue(array, appendString) {
  const output = [];
  for (const val of array) {
    output.push(appendString + val);
  }
  return output;
}
