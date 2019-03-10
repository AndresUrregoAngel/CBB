import scala.collection.mutable.ListBuffer
import scala.compat.Platform.currentTime
import scala.collection.mutable.MutableList
import scala.io.Source


object practiqueII extends App {

  class student(ido: String, val nom: String, val finalscore: Double) {
    private var _id: String = ido

    def id = _id

    def id_= (valeur:String): Unit ={
      _id= valeur
    }

    def maketask(message: String): Unit = {
      println(message)
    }

    override def toString(): String = {
      "ID:" + id + " Nom: " + nom + " -" + "Note finale:" + finalscore
    }

  }

  var obj1: student = new student("10", "carlos", 5)

  println(obj1)
  println(obj1.nom)
  println(obj1.finalscore)
  obj1.maketask("doing doing")
  obj1.id_=("20")
  println(obj1)


}

