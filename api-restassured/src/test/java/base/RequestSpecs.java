package base;

import io.restassured.builder.RequestSpecBuilder;
import io.restassured.http.ContentType;
import io.restassured.specification.RequestSpecification;

public class RequestSpecs{

    public static RequestSpecification defaultRequestSpec() {
        return new RequestSpecBuilder()
                .setContentType(ContentType.JSON)
                .setAccept(ContentType.JSON)
                .log(io.restassured.filter.log.LogDetail.ALL)
                .build();
    }
 /*   public static RequestSpecification authRequestSpec() {
        return new RequestSpecBuilder()
                .setBaseUri("https://api.example.com")
                .setContentType(ContentType.JSON)
                .addHeader("Authorization", "Bearer " + "token") // burada direkt TokenManager.getToken()) yazılabılır. token degerı yazılmalı hata vermesın dıye " içine aldım
                .build();
    }
    // token değeri loginden nsra kullanıcı giriş yaptıktan snra API tarafından uretilir onu cekip daha snra chaining ile bu token daha sonra kullanılıyor
 */

}
