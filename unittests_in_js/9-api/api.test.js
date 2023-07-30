const chai = require('chai');
const request = require('request');
const { expect } = chai;

describe('Index page', () => {
it('correct status code', (done) => {
    request('http://localhost:7865', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('correct content', (done) => {
    request('http://localhost:7865', (error, response, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});
describe('Cart page', () => {
  const url = 'http://localhost:7865/cart/12';
  const invalidUrl = 'http://localhost:7865/cart/hello';

  it('correct status code for valid url', (done) => {
    request(url, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('correct status code for invalid url', (done) => {
    request(invalidUrl, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });

  it('correct content for valid url', (done) => {
    request(url, (error, response, body) => {
      expect(body).to.equal('Payment methods for cart 12');
      done();
    });
  });

  it('Checks the body when :id is not a number', (done) => {
    request(invalidUrl, (error, response, body) => {
      expect(body).to.equal('Cart not found');
      done();
    });
  });
});
