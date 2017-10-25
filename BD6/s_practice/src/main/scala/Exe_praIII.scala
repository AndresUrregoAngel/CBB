object Exe_praIII extends App{

/*  val liste = List(15,39,22,98,37,19,5)

  def sumlist(x: List[Int]): Int = {
    var a :Int = 0
    for (item <- x){
      a += item
    }
    return a
  }

  print(sumlist(liste))

  var somme: Int  = 0
  liste.foreach (x => somme += x)
  print(somme)*/


  val inputh_list = List("Introduction à la Programmation",
    "Pratique de la Programmation",
    "Structure de données",
    "Principe de la Programmation",
    "Algorithmie",
    "Langages de Programmation")


//  if (inputh_list.forall( x => x.toLowerCase == "programmation" )) somme += 1
  var somme  = inputh_list.count( _.contains("Programmation") )
  println(somme)


  var sommen  = inputh_list.count( _.contains("Programmation") )
  println(sommen)






}
