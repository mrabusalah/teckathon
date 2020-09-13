package com.amazon.amazonproject.modle;

import com.amazon.amazonproject.enums.Role;
import lombok.Data;

import javax.persistence.*;

@Data
@Entity
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    private String firstName;
    private String middleName;
    private String lastName;
    private String email;
    private String phone;
    private String country;
    @Enumerated(EnumType.STRING)
    private Role role;
}
