import scala.collection.mutable
import scala.collection.mutable.ListBuffer
import scala.compat.Platform.currentTime
import scala.collection.mutable.MutableList
import scala.io.Source


object practiqueI extends App{
//exercise 1
/*  val liste = List(15,39,22,98,37,19,5)
  var z : Int = 0

  for (i <- liste){

    z = z + i
  }

  println("the total is:",z)*/

//exercise 2
  /*
  val list_txt = List("Introduction à la programmation ",
    "Practique de la programmation",
    "Structure de données",
    "principe de la programmation",
    "Algorithme","Langages de programmation")


  def wordrepeted(some:List[String]) : Int =  {
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
    return counter_nword
  }

  wordrepeted(list_txt)

*/

//exercise 3
  /*val inputh_list = List("Introduction à la Programmation",
  "Pratique de la Programmation",
  "Structure de données",
  "Principe de la Programmation",
  "Algorithmie",
  "Langages de Programmation")

   val output_list = inputh_list.filter(_.contains(" "))
   for (i <- output_list) {
    print(i)
   }

  val output_nospace = inputh_list.filterNot(_.contains(" "))
  println(output_nospace)*/
// exercise 4

  var word_count : Int = 0
  var word_count_issis : Int =0
  var word_lengh18 : Int = 0
  var word_issis = new ListBuffer[String]()
  var word_notvowels = new ListBuffer[String]()
  val F = Source.fromFile("C:\\Users\\axu30\\Documents\\GitHub\\CBB\\BD6\\s_practice\\src\\test\\english_words.txt")
  for (line <- F.getLines) {
    word_count += 1
    if (line.contains("issis")){
      word_issis += line
    }
    if (line.length == 18 ){
      word_lengh18 += 1
    }
    if ( !(line.contains("a") || line.contains("e") || line.contains("i") ||
           line.contains("o") || line.contains("u") )){
      word_notvowels += line
    }
  }

  for (word <- word_issis){
      word_count_issis += 1
  }
  println("the file has "+ word_count +" words, and words with the string issis are:"+ word_count_issis)
  for (word <- word_notvowels){
    println(word.split(",").foreach(print))
  }


}