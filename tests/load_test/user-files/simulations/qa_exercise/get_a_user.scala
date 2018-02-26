
package qa_exercise

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._
import io.gatling.core.session.Session

class GetAUsers extends Simulation {
  val sentHeaders = Map("Content-Type" -> "application/json")
  val scn = scenario("QA Exercise Load Test").repeat(100) {
            exec(http("Load Test 2")
              .get("http://localhost:5000/users/1")
              .headers(sentHeaders)
              .check(status.is(200)))}

  setUp(scn.inject(atOnceUsers(100)))

}
