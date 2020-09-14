package com.amazon.amazonproject.services;

import com.amazon.amazonproject.modle.Material;
import com.amazon.amazonproject.repositories.MaterialRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class MaterialService {

    private final MaterialRepository materialRepository;

    public MaterialService(MaterialRepository materialRepository) {
        this.materialRepository = materialRepository;
    }

    public List<Material> getAllMaterial() {
        return materialRepository.findAll();
    }

    public Optional<Material> getMaterialById(Long id) {
        return materialRepository.findById(id);
    }

    public Material addNewMaterial(Material material) {
        return materialRepository.save(material);
    }

    public Material updateExistMaterial(Material material) {
        if (isExist(material)) {
            return materialRepository.save(material);
        }
        return addNewMaterial(material);
    }

    private boolean isExist(Material material) {
        return materialRepository.existsById(material.getId());
    }
}
