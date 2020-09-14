package com.amazon.amazonproject.repositories;

import com.amazon.amazonproject.modle.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> getUserByUsername(String username);

    boolean existsByUsername(String username);
}
