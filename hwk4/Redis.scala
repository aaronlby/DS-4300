import scala.collection.mutable.HashMap

class Redis {

  var keyValue = HashMap[String, List[String]]()

  def get(key: String): List[String] = {
    val value = keyValue get key
    value match {
      case Some(x) => x
      case None => Nil
    }
  }

  def set(key: String, value: String): Unit = {
    if (!(keyValue contains key))
      (keyValue += (key -> List(value)))
    else
      (keyValue += (key -> (value +: getValue(key))))
  }

  def lpush(key: String, value: String): Int = {
    (keyValue += (key -> (value +: getValue(key))))
    llen(key)
  }

  def rpush(key: String, value: String): Int = {
    (keyValue += (key -> (getValue(key) :+ value)))
    llen(key)
  }

  def lpop(key: String): String = {
    val losValue = getValue(key)
    (keyValue += (key -> losValue.drop(1)))
    losValue.head
  }

  def rpop(key: String): String = {
    val losValue = getValue(key)
    (keyValue += (key -> losValue.dropRight(1)))
    losValue.last
  }

  def lrange(key: String, start: Int, stop: Int): List[String] = {
    val losValue = getValue(key)
    var specifiedElements = List[String]()
    if ((start > stop) || (stop > (losValue length)))
      throw new Exception("The start index must be less than the end one.")
    else
      for(i <- start until stop) {
        specifiedElements = (specifiedElements :+ losValue(i))
      }
    return specifiedElements
  }

  def llen(key: String): Int = {
    getValue(key) length
  }

  def getValue(k:String): List[String] = keyValue getOrElse(k, List.empty)
}
