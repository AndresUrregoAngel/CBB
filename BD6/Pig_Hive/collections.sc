import java.util
import scala.io.StdIn.{readInt,readLine}

object Hello extends App {
  val liste = List("a","b","c")
  for (i <- liste){
    println(i)
    }
  val listing = new java.util.ArrayList[String] ()
  listing.add("a")
  listing.add("d")
  listing.add("f")
  listing.add("q")
  
  println(listing)
  
  println(liste.renverse)
 }
 
 
object Hello extends App {
  //tuple
  var a = (45,"a",12)
  println(a._1)
  
  var (x,y,z,python,java) = (1,2,4,"python",false)
  println(x,y,z,python,java)
  
 def calcul_carre (x:Int): Int = {
  x*x
  }
  
  
 }
 
 
