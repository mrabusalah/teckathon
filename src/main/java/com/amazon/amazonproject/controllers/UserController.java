package com.amazon.amazonproject.controllers;

import com.amazon.amazonproject.modle.User;
import com.amazon.amazonproject.services.UserService;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/users")
public class UserController {


    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }


    @GetMapping
    public List<User> getAllUsers() {
        return userService.getAllUsers();
    }

    @GetMapping("/{id}")
    public Optional<User> getUserWithId(@PathVariable Long id) {
        return userService.getUserById(id);
    }

    @GetMapping("/settings/{username}")
    public User getUserWithId(@PathVariable String username) {
        return userService.getUserByUsername(username);
    }

    @PostMapping
    public User addNewUser(@Valid @RequestBody User user) {
        return userService.addNewUser(user);
    }

    @PutMapping
    public User updateExistUser(@RequestBody User user) {
        return userService.updateExistUser(user);
    }

}
