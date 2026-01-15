package utils;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonUtil {

    private static final ObjectMapper mapper = new ObjectMapper();

    public static String getValue(String json, String key) {
        try {
            JsonNode node = mapper.readTree(json);
            return node.get(key).asText();
        } catch (Exception e) {
            return null;
        }
    }
}
