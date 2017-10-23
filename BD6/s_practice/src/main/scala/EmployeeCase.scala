
import scala.collection.mutable.ListBuffer

object EmployeeCase extends App {

  case class Employee(var name: String, var lastname: String, var age: Int)

  case class EmployeeList() {

    var listempl = new ListBuffer[Employee]()

    def addnewemployee(empl: Employee): ListBuffer[Employee] = {

      for (currempl <- listempl) {
        if (empl == currempl) {
          println("the employee is duplicated verify the recod: ", empl)
        }
      }
       listempl += empl
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

  var container = EmployeeList()
  //println(ObjE1)
  container.addnewemployee(ObjE1)
  container.addnewemployee(ObjE2)
  container.addnewemployee(ObjE3)
  container.printlist()


}
