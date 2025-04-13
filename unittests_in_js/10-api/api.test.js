const request = require("request");
const { expect } = require("chai");

describe("Index page", () => {
  const url = "http://localhost:7865/";

  it("should return status 200", (done) => {
    request(url, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return "Welcome to the payment system"', (done) => {
    request(url, (error, response, body) => {
      expect(body).to.equal("Welcome to the payment system");
      done();
    });
  });
});

describe("Cart page", () => {
  it("should return status 200 when id is a number", (done) => {
    request("http://localhost:7865/cart/12", (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal("Payment methods for cart 12");
      done();
    });
  });

  it("should return status 404 when id is NOT a number", (done) => {
    request("http://localhost:7865/cart/hello", (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});

describe("Available Payments endpoint", () => {
  const url = "http://localhost:7865/available_payments";

  it("should return status 200", (done) => {
    request(url, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it("should return the correct payment methods object", (done) => {
    request(url, { json: true }, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false,
        },
      });
      done();
    });
  });
});

describe("Login endpoint", () => {
  const url = "http://localhost:7865/login";

  it("should return welcome message when userName is provided", (done) => {
    const options = {
      url: url,
      method: 'POST',
      json: true,
      body: { userName: 'Betty' }
    };
    request(options, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal("Welcome Betty");
      done();
    });
  });

  it("should return status 400 when userName is missing", (done) => {
    const options = {
      url: url,
      method: 'POST',
      json: true,
      body: {} // Missing userName
    };
    request(options, (error, response, body) => {
      // Based on api.js, it should return 400 if userName is missing
      expect(response.statusCode).to.equal(400);
      // Optionally check the body message
      // expect(body).to.equal("Bad Request: userName is required");
      done();
    });
  });

   it("should return status 400 when userName is empty", (done) => {
    const options = {
      url: url,
      method: 'POST',
      json: true,
      body: { userName: '' } // Empty userName
    };
    request(options, (error, response, body) => {
      // Based on api.js, it should return 400 if userName is empty
      expect(response.statusCode).to.equal(400);
      done();
    });
  });
});
