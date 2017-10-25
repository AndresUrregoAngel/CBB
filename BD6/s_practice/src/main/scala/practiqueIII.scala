


object practiqueIII extends App {

  def message(): String = {
    "Bienvenue"
  }

  val toto = message
  //println(toto)


  //imbriquees function

  def maxn(a: Int, b: Int, c: Int): Int = {
    def max(a: Int, b: Int): Int = {
      if (a > b) a else b
    }

    max(a, max(b, c))
  }


  //println(maxn(3,5,1))

  //VARARG Functions

  def sum(elem: Int*): Int = {
    var total = 0
    for (i <- elem) {
      total += i
    }
    total
  }

  //print(sum(2,4,5,1))


  //HIGH ORDER

  def double(x: Int): Int = {
    x * 2
  }

  val mondoublage = double(5)
  //print(mondoublage)


  val totodeux: (Int) => Int = double


  //plus de parametres


  def sum(a: Int, b: Int): Int = {
    a + b

  }

  val monsumme: (Int, Int) => Int = sum

  //println(sum(2, 2))
  //println(monsumme(2, 2))

  def traiterchaine(phrase: String): String = {
    if (phrase != null) {
      phrase.reverse
    } else {
      phrase
    }
  }

  def betterphrase (phrase: String , f:String => String) : String = {  //High-Order
    f(phrase)
  }

  val s1 = betterphrase("Bienvenue",traiterchaine)
  val s2 = betterphrase("Bienvenue",_.reverse)

  // Literal Function

  val multiplicateur  = (x:Int) =>  x * 2
  //println(multiplicateur(5))

  //*************Training***********///

  def stringwel = (phrase:String) => "Bienvenue "+phrase // literal
  def stringweld : (String => String) = x => "Bienvenue "+ x //  high-order



  print(stringwel("test"))


}
