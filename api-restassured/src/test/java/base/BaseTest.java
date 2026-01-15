package base;
import config.ConfigReader;
import io.qameta.allure.testng.AllureTestNg;
import io.restassured.RestAssured;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Listeners;

@Listeners({AllureTestNg.class})
// alure testi eklemek için komut :  allure serve allure-results
public class BaseTest {
    @BeforeClass
    public void setup() {
        RestAssured.baseURI = ConfigReader.get("base.url"); // config properties içerisinden geliyor
    }
    public static long petId;
    public static long InvalidPetId=Long.parseLong(ConfigReader.get("InvalidPetId"));
}
