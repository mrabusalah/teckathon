package com.amazon.amazonproject.services;

import org.springframework.stereotype.Service;

@Service
public class MaterialService {
    private final MaterialService materialService;

    public MaterialService(MaterialService materialService) {
        this.materialService = materialService;
    }
}
