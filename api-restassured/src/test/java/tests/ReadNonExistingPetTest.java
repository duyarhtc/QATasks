package tests;

import base.BaseTest;
import io.qameta.allure.Epic;
import io.qameta.allure.Feature;
import io.qameta.allure.Story;
import org.testng.annotations.Test;

import static base.RequestSpecs.defaultRequestSpec;
import static io.restassured.RestAssured.given;

public class ReadNonExistingPetTest extends BaseTest {
    @Epic("Pet API")
    @Feature("CRUD Operations - Negative")
    @Story("Read Non existing Pet - Negative")
    @Test
    public void getNonExistingPet_negative() {

        given()
                .spec(defaultRequestSpec())
                .pathParam("petId", InvalidPetId)
                .when()
                .get("/pet/{petId}")
                .then()
                .statusCode(404);
    }
}
