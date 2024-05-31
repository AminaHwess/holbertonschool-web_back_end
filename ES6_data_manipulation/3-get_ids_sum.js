export default function getStudentIdsSum(listarr) {
  return listarr.reduce((total, student) => total + student.id, 0);
}
