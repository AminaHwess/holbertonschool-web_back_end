const sinon = require("sinon");
const { expect } = require("chai");
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./3-payment");

describe("sendPaymentRequestToApi", function () {
  let spy;

  beforeEach(() => {
    spy = sinon.spy(Utils, "calculateNumber");
  });

  afterEach(() => {
    spy.restore();
  });

  it("should call Utils.calculateNumber with SUM, 100, 20", function () {
    sendPaymentRequestToApi(100, 20);

    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith("SUM", 100, 20)).to.be.true;
  });
});
