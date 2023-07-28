const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function () {
  it('should return the rounded sum of two integers', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it('should return the rounded sum of an integer and a float', function () {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it('should return the rounded sum of two floats', function () {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it('should return the rounded sum of two floats with a decimal .5', function () {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
});
