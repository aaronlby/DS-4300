import breeze.plot._

// Integer to n-bit binary string
object Binary extends App {
  def toBinary(x:Int, bits: Int): String = {
    if (x == 1) "0"*(bits-1)+"1"
    else if (x == 0) "0"*bits
    else toBinary(x/2, bits - 1) + (x % 2).toString
  }
  println(toBinary(1234567890, 32))
  println(toBinary(57,8))

  // count the weight
  def weight(b: String): Int = b.count(_ == '1')
  println(weight("87654321"))

  // Draw the graph
  val xs = Range(0, 1025)
  val ys = xs.map(x=>weight(toBinary(x, 8)))
  val fig = Figure()
  val plt = fig.subplot(0)
  plt += plot(xs,ys)
  fig.refresh()
}
