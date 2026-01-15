package tests;

import base.BaseTest;
import io.qameta.allure.Epic;
import io.qameta.allure.Feature;
import io.qameta.allure.Story;
import org.testng.annotations.Test;

import static base.RequestSpecs.defaultRequestSpec;
import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.anyOf;
import static org.hamcrest.Matchers.is;

public class CreatePetWithoutBodyTest extends BaseTest {
    @Epic("Pet API")
    @Feature("CRUD Operations - Negative")
    @Story("Create Pet Without Body - Negative")
    @Test
    public void createPet_withoutBody_negative() {

        given()
                .spec(defaultRequestSpec())
                .when()
                .post("/pet")
                .then()
                .statusCode(anyOf(is(400), is(405)));
    }
}
