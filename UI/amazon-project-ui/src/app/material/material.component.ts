import {Component, OnInit} from '@angular/core';
import {Material} from "../model/Material";
import {ActivatedRoute, ParamMap, Router} from "@angular/router";
import {MaterialService} from "../services/material.service";

@Component({
  selector: 'app-material',
  templateUrl: './material.component.html',
  styleUrls: ['./material.component.css']
})
export class MaterialComponent implements OnInit {

  material: Material;
  id: number;

  constructor(private route: ActivatedRoute,
              private router: Router,
              private materialService: MaterialService) {
    this.route.paramMap.subscribe((param: ParamMap) => {
      this.id = +param.get('id');

      this.materialService.getMaterialById(this.id)
        .subscribe(data => {
          this.material = data;
        }, error => console.log(error));
    });
  }

  ngOnInit(): void {
    this.material = new Material();
  }

}
