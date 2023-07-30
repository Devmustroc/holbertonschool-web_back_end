const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', () => {
  let log;
  beforeEach(() => {
    log = sinon.spy(console, 'log');
  });
  afterEach(() => {
    log.restore();
  });
  it('call sendPaymentRequestToApi with 100, and 20', () => {
    const totalAmount = 100;
    const totalShipping = 20;

    sendPaymentRequestToApi(totalAmount, totalShipping);

    sinon.assert.calledOnce(log);
    sinon.assert.calledWith(log, 'The total is: 120');
  });
  it('call sendPaymentRequestToApi with 10, and 10', () => {
    const totalAmount = 10;
    const totalShipping = 10;

    sendPaymentRequestToApi(totalAmount, totalShipping);

    sinon.assert.calledOnce(log);
    sinon.assert.calledWith(log, 'The total is: 20');
  });
});
