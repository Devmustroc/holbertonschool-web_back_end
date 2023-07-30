const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  it('should call calculateNumber', () => {
    const calculate = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    calculate.restore();
    sinon.assert.calledOnce(calculate);
    sinon.assert.calledWithExactly(calculate, 'SUM', 100, 20);
  });
});
