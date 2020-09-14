package com.amazon.amazonproject.services;

import com.amazon.amazonproject.modle.User;
import com.amazon.amazonproject.repositories.UserRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class UserService {

    private final UserRepository userRepository;

    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public List<User> getAllUsers() {
        return userRepository.findAll();
    }

    public Optional<User> getUserById(Long id) {
        return userRepository.findById(id);
    }

    public User addNewUser(User user) {
        return userRepository.save(user);
    }

    public User updateExistUser(User user) {
        if (isExist(user)) {
            return userRepository.save(user);
        }
        return addNewUser(user);
    }

    private boolean isExist(User user) {
        return userRepository.existsById(user.getId());
    }

    public User loginCheck(String username, String password) {
        if (isUsernameExist(username)) {
            User user = userRepository.findUserByUsername(username);
            return isOk(user, password) ? user : null;
        }
        throw new NullPointerException("username not found");
    }

    private boolean isOk(User user, String password) {
        return password.equals(user.getPassword());
    }

    private boolean isUsernameExist(String username) {
        return userRepository.existsByUsername(username);
    }
}
