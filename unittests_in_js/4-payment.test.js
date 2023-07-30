const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', () => {
  it('should call calculateNumber', () => {
    const calculate = sinon.stub(Utils, 'calculateNumber').returns(10);
    const log = sinon.spy(console, 'log');
    const totalAmount = 100;
    const totalShipping = 20;

    sendPaymentRequestToApi(totalAmount, totalShipping);

    calculate.restore();
    log.restore();
    sinon.assert.calledOnce(calculate);
    sinon.assert.calledWith(calculate, 'SUM', totalAmount, totalShipping);
    sinon.assert.calledOnce(log);
    sinon.assert.calledWith(log, `The total is: 10`);
  });
});
