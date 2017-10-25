
import scala.collection.mutable.ListBuffer

object EmployeeCase extends App {

  case class Employee(var name: String, var lastname: String, var age: Int)

  class EmployeeList() {

    var listempl = new ListBuffer[Employee]()

    def addnewemployee(empl: Employee): ListBuffer[Employee] = {
      var sortie = false
      for (currempl <- listempl) {
        if (empl == currempl) {
          println("the employee is duplicated verify the record: ", empl)
          sortie = true
        }
      }
      if (!sortie) listempl += empl
      listempl

    }

    def printlist(): Unit = {
      for (empl <- listempl) {
        println(empl)
      }
    }
  }


  val ObjE1 = Employee("andres", "urrego", 31)
  val ObjE2 = Employee("juan", "urrego", 32)
  val ObjE3 = ObjE1.copy()

  var container = new EmployeeList()
  //println(ObjE1)
  container.addnewemployee(ObjE1)
  container.addnewemployee(ObjE2)
  container.addnewemployee(ObjE3)
  container.printlist()


}
