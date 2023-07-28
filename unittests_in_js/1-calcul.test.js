const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
  it('add two integer', function() {
    assert.equal(calculateNumber('SUM', 1, 3), 4);
  });
  it('add integer and float', function() {
    assert.equal(calculateNumber('SUM', 1, 3.7), 5);
  });
  it('add two float', function() {
    assert.equal(calculateNumber('SUM', 1.2, 3.7), 5);
  });
  it('add two float', function() {
    assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
  });
  it('add negative a,d float', function() {
    assert.equal(calculateNumber('SUM', -3, 1.2), -2);
  });
  it('sub two integer', function() {
    assert.equal(calculateNumber('SUBTRACT', 3, 1), 2);
  });
  it('sub to float', function() {
    assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
  });
  it('sub two float', function() {
    assert.equal(calculateNumber('SUBTRACT', 1.2, 3.7), -3);
  });
  it('sub two float', function() {
    assert.equal(calculateNumber('SUBTRACT', 3.7, 1.5), 2);
  });
  it('Checks 0.1 - 0.1', function() {
    assert.equal(calculateNumber('SUBTRACT', 0.1, 0.1), 0);
  });
  it('divide two integer', function() {
    assert.equal(calculateNumber('DIVIDE', 3, 1), 3);
  });
  it('divide two float', function() {
    assert.equal(calculateNumber('DIVIDE', 3.5, 2.1), 2);
  });
  it('divide two float', function() {
    assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
  });
  it('divide integer with a zero', function() {
    assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });
  it('divide two rounded 0', function() {
    assert.equal(calculateNumber('DIVIDE', 0.1, 0.1), 'Error');
  });
});
