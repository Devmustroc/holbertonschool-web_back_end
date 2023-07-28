const calculateNumber = require("./1-calcul.js");
const assert = require("assert");

describe("calculateNumber", function () {
  it ("checks the output of SUM", function () {
    assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
    assert.equal(calculateNumber('SUM', 1.2, 3.7), 5);
    assert.equal(calculateNumber('SUM', 1.5, 3.7), 6);
    assert.equal(calculateNumber('SUM', -3, 1.2), -2);
  });
  it ("checks the output of SUBTRACT", function () {
    assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    assert.equal(calculateNumber('SUBTRACT', 1.2, 3.7), -3);
    assert.equal(calculateNumber('SUBTRACT', 1.5, 3.7), -2);
    assert.equal(calculateNumber('SUBTRACT', -3, 1.2), -4);
  });
  it ("checks the output of DIVIDE", function () {
    assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    assert.equal(calculateNumber('DIVIDE', 1.2, 3.7), 0.25);
    assert.equal(calculateNumber('DIVIDE', 1.5, 3.7), 0.4);
    assert.equal(calculateNumber('DIVIDE', -3, 1.2), -2.5);
  });
  it ("checks the output of DIVIDE when dividing by 0", function () {
    assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    assert.equal(calculateNumber('DIVIDE', 1.2, 0), 'Error');
    assert.equal(calculateNumber('DIVIDE', 1.5, 0), 'Error');
    assert.equal(calculateNumber('DIVIDE', -3, 0), 'Error');
  });
});
