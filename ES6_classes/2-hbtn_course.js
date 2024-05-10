export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
    if (typeof (name) !== 'string') { throw new TypeError('Name must be a string'); }

    if (typeof (length) !== 'number') { throw new TypeError('Length must be a Number'); }

    if (!Array.isArray(students)) { throw new TypeError('Students must be an Array'); }
  }

  get name() { return this._name; }

  set name(namee) { this._name = namee; }

  get length() { return this._length; }

  set length(lengthh) { this._length = lengthh; }

  get students() { return this._students; }

  set students(studentss) { this._students = studentss; }
}
