package tests;

import base.BaseTest;
import base.RequestSpecs;
import io.qameta.allure.Epic;
import io.qameta.allure.Feature;
import io.qameta.allure.Story;
import org.testng.annotations.Test;
import static org.hamcrest.Matchers.equalTo;

import static io.restassured.RestAssured.given;

public class UpdatePetTest extends BaseTest {

    @Epic("Pet API")
    @Feature("CRUD Operations")
    @Story("Update Pet - Positive")
    @Test(priority = 3,dependsOnMethods = "getPet_positive")
    public void updatePet_positive() {

        long petId = BaseTest.petId;
        String photoPath = "testdata/pet.jpg";
        String updatedBody = """
        {
          "id": %d,
          "category": {
            "id": 1,
            "name": "Dogs"
          },
          "name": "Minik",
          "photoUrls": ["%s"],
          "tags": [
            {
              "id": 1,
              "name": "friendly"
            }
          ],
          "status": "sold"
        }
        """.formatted(petId, photoPath);

        System.out.println("REQUEST -> PUT /pet");
        System.out.println(updatedBody);

        given()
                .spec(RequestSpecs.defaultRequestSpec())
                .body(updatedBody)
                .when()
                .put("/pet")
                .then()
                .statusCode(200)
                .body("name", equalTo("Minik"))
                .body("status", equalTo("sold"));
    }
}
