import {Component, OnInit} from '@angular/core';
import {MaterialService} from "../services/material.service";
import {Material} from "../model/Material";
import {Router} from "@angular/router";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  username: string;
  materials: Material[];

  constructor(private materialService: MaterialService, private router: Router) {
  }

  ngOnInit(): void {
    this.username = localStorage.getItem("username");
    this.materialService.getAllMaterials().subscribe(res => {
      this.materials = res;
      console.log(this.materials);
    }, error => {
      console.log(error);
    });
  }

}
