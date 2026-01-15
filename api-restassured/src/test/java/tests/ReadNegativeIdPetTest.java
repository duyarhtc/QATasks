package tests;

import base.BaseTest;
import io.qameta.allure.Epic;
import io.qameta.allure.Feature;
import io.qameta.allure.Story;
import org.testng.annotations.Test;

import static base.RequestSpecs.defaultRequestSpec;
import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;

public class ReadNegativeIdPetTest extends BaseTest {
    @Epic("Pet API")
    @Feature("CRUD Operations - Negative")
    @Story("Read Negative ID Pet  - Negative")
    @Test
    public void getNegativeIdPet_negative() {

        given()
                .spec(defaultRequestSpec())
                .pathParam("petId", -1)
                .when()
                .get("/pet/{petId}")
                .then()
                .statusCode(404)
                .body("message", equalTo("Pet not found"));
    }

}
