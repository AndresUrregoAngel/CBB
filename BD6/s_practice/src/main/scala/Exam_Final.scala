import scala.collection.mutable.ListBuffer

object Exam_Final extends App{

  var NonbananesList = new ListBuffer[String]()
  val inputh = List( "Salade de bananes et pommes",
                     "bananes et pommes du midi",
                      "Fruterie général",
                      "bananes",
                      "Banania",
                      "pommes de l'automne"
  )

  for (i <- inputh)
    if (!(i.toLowerCase.contains("bananes"))){
        NonbananesList += i
    }

  var non_bananes = NonbananesList.count(_.nonEmpty)
  var contain_pommes = inputh.count(_.toLowerCase.contains("pommes"))

  def UpperList(x:List[String]): ListBuffer[String] = {
    var new_list = new ListBuffer[String]()
    for (i <- x)
      new_list += i.toUpperCase

    return new_list
  }
  //first point
  println("the number of elements that dont contain the word 'bananes' is: "+non_bananes)
  //second point
  println("the number of elements in the list that contain the word 'pommes' is:"+contain_pommes)
  //third point
  println("the list in upper case is: "+UpperList(inputh))
}
