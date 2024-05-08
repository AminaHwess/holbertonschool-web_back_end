export default function createEmployeesObject(departmentName, employees) {
  const dictionary = {};
  dictionary[departmentName] = employees;

  return dictionary;
}
