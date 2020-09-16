package com.amazon.amazonproject.modle;

import lombok.Data;

import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Data
public class Material {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    private String materialLink;
    private Long creatorId;
    private String materialTitle;
    private String materialDescription;
    private String materialThumbnail;
    private LocalDateTime creatingDate;

    @PrePersist
    public void prePersist() {
        this.creatingDate = LocalDateTime.now();
    }
}
