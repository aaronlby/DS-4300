object HW4 extends App {
  override def main(args: Array[String]) {

    println("Hello again")

    val g: Graph = new Graph()
    g.addNode("X")
    g.addNode("J")
    g.addNode("B")
    g.addNode("E")
    g.addNode("R")
    g.addNode("C")
    g.addNode("F")
    g.addNode("Y")

    g.addEdge("X", "J")
    g.addEdge("J", "F")
    g.addEdge("F", "E")
    g.addEdge("F", "B")
    g.addEdge("F", "J")
    g.addEdge("R", "Y")
    g.addEdge("R", "E")
    g.addEdge("R", "C")
    g.addEdge("R", "B")
    g.addEdge("R", "J")
    g.addEdge("B", "R")
    g.addEdge("B", "C")
    g.addEdge("B", "J")
    g.addEdge("C", "R")
    g.addEdge("C", "B")
    g.addEdge("E", "F")
    g.addEdge("E", "Y")
    g.addEdge("E", "R")
    g.addEdge("Y", "R")
    g.addEdge("Y", "E")
    g.addEdge("J", "R")
    g.addEdge("J", "B")
    g.addEdge("J", "X")

    val path = g.shortestPath("X", "Y")
    path.foreach(print)


  }
}