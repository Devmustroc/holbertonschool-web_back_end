export default function updateUniqueItems(groceries) {
  const error = 'Cannot process';
  if (groceries instanceof Map) {
    for (const [key, value] of groceries) {
      if (value === 1) {
        groceries.set(key, 100);
      }
    }
    return groceries;
  }
  return error;
}
