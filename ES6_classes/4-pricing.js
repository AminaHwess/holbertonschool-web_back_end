export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  get amount() { return this._amount; }

  set amount(amount) {
    this._amount = amount;
  }

  get currency() { return this._currency; }

  set currency(currency) {
    this._currency = currency;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.code} (${this._currency.name})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}