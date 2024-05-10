export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    if (!Array.isArray(students)) {
      throw new TypeError('Students must be an array');
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(name2) {
    if (typeof name2 !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = name2;
  }

  get length() {
    return this._length;
  }

  set length(length2) {
    if (typeof length2 !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = length2;
  }

  get students() {
    return this._students;
  }

  set students(students2) {
    if (!Array.isArray(students2)) {
      throw new TypeError('Students must be an array');
    }
    this._students = students2;
  }
}
