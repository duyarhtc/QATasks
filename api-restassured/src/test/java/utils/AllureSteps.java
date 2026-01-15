package utils;

import io.qameta.allure.Step;

public class AllureSteps {

    @Step("Request body oluşturuluyor: name={name}, job={job}")
    public static String createUserBody(String name, String job) {
        return """
               {
                 "name": "%s",
                 "job": "%s"
               }
               """.formatted(name, job);
    }
}
