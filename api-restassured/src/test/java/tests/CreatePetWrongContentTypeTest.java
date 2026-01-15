package tests;

import base.BaseTest;
import io.qameta.allure.Epic;
import io.qameta.allure.Feature;
import io.qameta.allure.Story;
import org.testng.annotations.Test;
import static org.hamcrest.Matchers.anyOf;
import static org.hamcrest.Matchers.is;

import static base.RequestSpecs.defaultRequestSpec;
import static io.restassured.RestAssured.given;

public class CreatePetWrongContentTypeTest extends BaseTest {
    @Epic("Pet API")
    @Feature("CRUD Operations - Negative")
    @Story("Create Pet With Wrong ContentType  - Negative")
    @Test
    public void createPet_WrongContentType_negative() {

        given()
                .spec(defaultRequestSpec())
                .contentType("text/plain")
                .when()
                .post("/pet")
                .then()
                .statusCode(anyOf(is(400), is(415)));
    }
}
