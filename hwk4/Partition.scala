object Partition extends App {


  def moved(records: Int, startN: Int, endN: Int): Double = {
    var numR = 0
    for (a <- 0 to records) {
      val start = a % startN
      val end = a % endN
      if (start != end) {
        numR += 1
      }
    }

    numR/records.toDouble

  }

  println(moved(1000000, 100, 107))
}
