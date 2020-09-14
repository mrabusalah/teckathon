package com.amazon.amazonproject.controllers;

import com.amazon.amazonproject.modle.Material;
import com.amazon.amazonproject.services.MaterialService;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/api/materials")
public class MaterialController {
    private final MaterialService materialService;

    public MaterialController(MaterialService materialService) {
        this.materialService = materialService;
    }

    @GetMapping
    public List<Material> getAllMaterial(){
        return materialService.getAllMaterial();
    }

    @GetMapping("/{id}")
    public Optional<Material> getMaterialById(@PathVariable Long id){
        return materialService.getMaterialById(id);
    }

    @PostMapping
    public Material addNewMaterial(@RequestBody @Valid Material material){
        return materialService.addNewMaterial(material);
    }

    @PutMapping
    public Material updateExistMaterial(@RequestBody @Valid Material material){
        return materialService.updateExistMaterial(material);
    }
}
