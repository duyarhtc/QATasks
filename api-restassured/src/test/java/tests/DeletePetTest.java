package tests;

import base.BaseTest;
import base.RequestSpecs;
import io.qameta.allure.Epic;
import io.qameta.allure.Feature;
import io.qameta.allure.Story;
import org.testng.annotations.Test;
import static org.hamcrest.Matchers.equalTo;

import static io.restassured.RestAssured.given;

public class DeletePetTest extends BaseTest {

    @Epic("Pet API")
    @Feature("CRUD Operations")
    @Story("Delete Pet - Positive")
    @Test(priority = 4,dependsOnMethods = "getPet_positive")
    public void deletePet_positive() {

        given()
                .spec(RequestSpecs.defaultRequestSpec())
                .when()
                .delete("/pet/" + petId)
                .then()
                .statusCode(200) // Swagger docs'a göre başarılı DELETE 200 dönüyor
                .body("message", equalTo(String.valueOf(petId))); // geri dönen mesaj genelde silinen petId olur
    }
}
