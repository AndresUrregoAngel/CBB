import scala.collection.immutable.List
import scala.collection.mutable
import scala.collection.mutable.ListBuffer
import scala.compat.Platform.currentTime
import scala.collection.mutable.MutableList
import scala.io.Source

object Employee extends App {

  class Employees(var name: String, var lastname: String, var age: Int) {


    override def toString(): String = {
      "Name: " + name + ", Lastname: " + lastname + ", age: " + age
    }
  }

  class EmployeeList() {

    //var listempl = List

    var listempl = new ListBuffer[Employees]()

    def newemployee(empl: Employees): ListBuffer[Employees] = {

      for (currempl <- listempl) {
        if (empl.name == currempl.name) {
          print("the employee: " + empl.name + " already exist")
        }
      }
      listempl += empl
    }

    def showupemployee(): Unit = {
      for (i <- listempl)
        println(i)
    }
  }

  val ObjE1 = new Employees("andres", "urrego", 31)
  val ObjE2 = new Employees("juan", "urrego", 32)
  val ObjE3 = new Employees("andres", "angel", 31)
  var container = new EmployeeList()
  //println(ObjE1)
  container.newemployee(ObjE1)
  container.newemployee(ObjE2)
  container.newemployee(ObjE3)
  container.showupemployee()


}
