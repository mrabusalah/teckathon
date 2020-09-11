package com.amazon.amazonproject.modle;

import lombok.Data;

@Data
public class Address {
    private String countryName;
    private String sate;
    private String streetName;
    private String buildingNumber;
    private int streetNumber;
}
