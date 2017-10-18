object practiqueI extends App{
//exercise 1
/*  val liste = List(15,39,22,98,37,19,5)
  var z : Int = 0

  for (i <- liste){

    z = z + i
  }

  println("the total is:",z)*/

//exercise 2
  val list_etxt = List("Introduction à la programation ",
    "Practique de la programmation",
    "Structure de données",
    "principe de la programmation",
    "Algorithme","Langages de progrmmation")

  val word_cle: String = "programation"
  var  counter_word:Int = 0

  for(i<-list_etxt){
    var test: String = i.toLowerCase
    if(test == word_cle){
      counter_word += 1
    }

  }

  println(counter_word)
}


