package com.amazon.amazonproject.controllers;

import com.amazon.amazonproject.modle.User;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/users")
public class UserController {
    @GetMapping("")
    public List<User> getAllUsers() {
        return null;
    }

    @GetMapping("/{id}")
    public User getUserWithId(@PathVariable Long id) {
        return null;
    }

    @PostMapping("")
    public User addNewUser(@RequestBody User user) {
        return null;
    }
}
