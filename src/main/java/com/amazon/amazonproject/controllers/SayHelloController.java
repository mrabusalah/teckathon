package com.amazon.amazonproject.controllers;

import com.amazon.amazonproject.HelloPage;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")
public class SayHelloController {
    @GetMapping("hello")
    public String firstHello() {
        String name = "Fox";
        HelloPage helloPage = new HelloPage();
        return helloPage.sayHello(name);
    }
}
