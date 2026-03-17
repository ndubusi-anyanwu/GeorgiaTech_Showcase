package edu.gatech.battle.configuration;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")  // Applies to all endpoints
                .allowedOrigins("http://localhost:3001")  // Replace with your frontend domain
                .allowedMethods("GET", "POST", "PUT", "DELETE")  // Add methods as needed
                .allowedHeaders("*")
                .allowCredentials(true);
    }
}

