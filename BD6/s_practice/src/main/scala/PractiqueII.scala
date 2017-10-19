import scala.collection.mutable.ListBuffer
import scala.compat.Platform.currentTime
import scala.collection.mutable.MutableList
import scala.io.Source


object practiqueII extends App {

  class student(ido: String, val nom: String, val finalscore: Double) {
    var id: String = ido



    def maketask(message: String): Unit = {
      println(message)
    }

    override def toString(): String = {
      "ID:"+ ido + " Nom: " + nom + " -" + "Note finale:" + finalscore
    }

  }

  var obj1: student = new student("10","carlos", 5)

  println(obj1)
  println(obj1.nom)
  println(obj1.finalscore)
  obj1.maketask("doing doing")

}

