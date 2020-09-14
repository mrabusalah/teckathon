package com.amazon.amazonproject.services;

import com.amazon.amazonproject.modle.User;
import com.amazon.amazonproject.repositories.UserRepository;
import org.springframework.stereotype.Repository;
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

    public boolean checkUserCredential(User user) {
        Optional<User> fetchedUser = userRepository.getUserByUsername(user.getUsername());
        if(isExist(fetchedUser.get())){
            String username = user.getUsername();
            String password = user.getPassword();
            return (username.equals(fetchedUser.get().getUsername()) &&
                    password.equals(fetchedUser.get().getPassword()));
        }
        return false;
    }

}
