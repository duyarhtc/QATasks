package tests;

import base.BaseTest;
import io.qameta.allure.Epic;
import io.qameta.allure.Feature;
import io.qameta.allure.Story;
import io.restassured.response.Response;
import org.testng.annotations.Test;
import static org.hamcrest.Matchers.equalTo;


import static base.RequestSpecs.defaultRequestSpec;
import static io.restassured.RestAssured.given;

public class ReadPetTest extends BaseTest {
    @Epic("Pet API")
    @Feature("CRUD Operations")
    @Story("Read Pet - Positive")
    @Test(priority = 2,dependsOnMethods = "createPet_positive")
    public void getPet_positive()  {
        long petId = BaseTest.petId;

        Response response =
                given()
                        .spec(defaultRequestSpec())
                        .pathParam("petId", petId)
                        .when()
                        .get("/pet/{petId}");

        response.then().statusCode(200)
                .body("name", equalTo("Tekir"))
                .body("status", equalTo("available"));
    }
}
