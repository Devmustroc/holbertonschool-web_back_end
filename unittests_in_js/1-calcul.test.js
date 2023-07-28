const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
  it('add two integers', function() {
    assert.equal(calculateNumber('SUM', 1, 3), 4);
  });
  it('add integer and one floats', function() {
    assert.equal(calculateNumber('SUM', 1, 3.7), 5);
  });
  it('add two floats', function() {
    assert.equal(calculateNumber('SUM', 1.2, 3.7), 5);
  });
  it('add negative digit and floats', function() {
    assert.equal(calculateNumber('SUM', -1, 3.7), 3);
  });
  it('add two negative floats', function() {
    assert.equal(calculateNumber('SUM', -1.2, -3.7), -5);
  });
  it('subtract two integers', function() {
    assert.equal(calculateNumber('SUBTRACT', 1, 3), -2);
  });
  it('subtract integer and one floats', function() {
    assert.equal(calculateNumber('SUBTRACT', 1, 3.7), -3);
  });
  it('subtract two floats', function() {
    assert.equal(calculateNumber('SUBTRACT', 1.2, 3.7), -3);
  });
  it('subtract negative digit and floats', function() {
    assert.equal(calculateNumber('SUBTRACT', -1, 3.7), -5);
  });
  it('subtract two negative floats', function() {
    assert.equal(calculateNumber('SUBTRACT', -1.2, -3.7), 3);
  });
  it('divide two integers', function() {
    assert.equal(calculateNumber('DIVIDE', 1, 3), 0.3333333333333333);
  });
  it('divide integer and one floats', function() {
    assert.equal(calculateNumber('DIVIDE', 1, 3.7), 0.25);
  });
  it('divide two floats', function() {
    assert.equal(calculateNumber('DIVIDE', 1.2, 3.7), 0.25);
  });
  it('divide negative digit and floats', function() {
    assert.equal(calculateNumber('DIVIDE', -1, 3.7), -0.25);
  });
  it('divide two negative floats', function() {
    assert.equal(calculateNumber('DIVIDE', -1.2, -3.7), 0.25);
  });
  it('divide by zero', function() {
    assert.equal(calculateNumber('DIVIDE', 1.2, 0), 'Error');
  });
});
