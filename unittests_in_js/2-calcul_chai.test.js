const chai = require('chai');
const { expect } = chai;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function() {
  it('add two integer', function() {
    expect(calculateNumber('SUM', 1, 3)).to.equal(4);
  });
  it('add integer and float', function() {
    expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
  });
  it('add two float', function() {
    expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
  });
  it('add two float', function() {
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
  });
  it('add negative a,d float', function() {
    expect(calculateNumber('SUM', -3, 1.2)).to.equal(-2);
  });
  it('sub two integer', function() {
    expect(calculateNumber('SUBTRACT', 3, 1)).to.equal(2);
  });
  it('sub to float', function() {
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
  });
  it('sub two float', function() {
    expect(calculateNumber('SUBTRACT', 1.2, 3.7)).to.equal(-3);
  });
  it('sub two float', function() {
    expect(calculateNumber('SUBTRACT', 3.7, 1.5)).to.equal(2);
  });
  it('Checks 0.1 - 0.1', function() {
    expect(calculateNumber('SUBTRACT', 0.1, 0.1)).to.equal(0);
  });
  it('divide two integer', function() {
    expect(calculateNumber('DIVIDE', 3, 1)).to.equal(3);
  });
  it('divide two float', function() {
    expect(calculateNumber('DIVIDE', 3.5, 2.1)).to.equal(2);
  });
  it('divide two float', function() {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
  });
  it('divide integer with a zero', function() {
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
  });
  it('divide two rounded 0', function() {
    expect(calculateNumber('DIVIDE', 0.1, 0.1)).to.equal('Error');
  });
});
