package tests;

import base.BaseTest;
import base.RequestSpecs;
import io.qameta.allure.Epic;
import io.qameta.allure.Feature;
import io.qameta.allure.Story;
import org.testng.annotations.Test;
import static org.hamcrest.Matchers.equalTo;

import static io.restassured.RestAssured.given;

public class CreatePetTest  extends BaseTest {
    @Epic("Pet API")
    @Feature("CRUD Operations")
    @Story("Create Pet - Positive")
    @Test(priority = 1)
    public void createPet_positive() {

        BaseTest.petId = System.currentTimeMillis();

        String photoPath = "testdata/pet.jpg"; // resource path string

        String body = """
    {
      "id": %d,
      "category": {
        "id": 1,
        "name": "Dogs"
      },
      "name": "Tekir",
      "photoUrls": ["%s"],
      "tags": [
        {
          "id": 1,
          "name": "friendly"
        }
      ],
      "status": "available"
    }
    """.formatted(petId, photoPath);

        given()
                .spec(RequestSpecs.defaultRequestSpec())
                .body(body)
                .when()
                .post("/pet")
                .then()
                .statusCode(200)
                .body("name", equalTo("Tekir"))
                .body("status", equalTo("available"));
}
}