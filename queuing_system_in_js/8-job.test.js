import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  const queue = kue.createQueue();
  before(() => queue.testMode.enter());
  afterEach(() => queue.testMode.clear());
  after(() => queue.testMode.exit());

  it('should throw error if not array', () => {
    expect(() => createPushNotificationsJobs(123, queue)).to.throw('Jobs is not an array');
  });

  it('should create jobs correctly', () => {
    const jobs = [
      { phoneNumber: '123', message: 'Hello' },
      { phoneNumber: '456', message: 'World' }
    ];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
  });
});