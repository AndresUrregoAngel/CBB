import scala.collection.mutable.ListBuffer


object practiqueI extends App{
//exercise 1
/*  val liste = List(15,39,22,98,37,19,5)
  var z : Int = 0

  for (i <- liste){

    z = z + i
  }

  println("the total is:",z)*/

//exercise 2
  val list_txt = List("Introduction à la programmation ",
    "Practique de la programmation",
    "Structure de données",
    "principe de la programmation",
    "Algorithme","Langages de programmation")


  def wordrepeted(some: _*)   {
    var  counter_word:Int = 0
    var counter_nword: Int =0
    val word_cle: String = "programmation"
    var exist_word: Boolean = false

    for (i <- some) {
      var test: String = i.toLowerCase
      if (test.contains(word_cle)) {
        counter_word +=  1
        exist_word = true
       } else {
         counter_nword += 1
      }
    }
    print(counter_word,counter_nword,exist_word)
  }

 wordrepeted(list_txt)

}


