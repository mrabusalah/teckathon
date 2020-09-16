import {Component, OnInit} from '@angular/core';
import {Material} from "../model/Material";
import {ActivatedRoute, ParamMap, Router} from "@angular/router";
import {MaterialService} from "../services/material.service";
import {User} from "../model/User";
import {UserService} from "../services/user.service";

@Component({
  selector: 'app-material',
  templateUrl: './material.component.html',
  styleUrls: ['./material.component.css']
})
export class MaterialComponent implements OnInit {

  user: User;
  material: Material;
  id: number;

  constructor(private route: ActivatedRoute,
              private router: Router,
              private materialService: MaterialService,
              private userService: UserService) {
    this.route.paramMap.subscribe((param: ParamMap) => {
      this.id = +param.get('id');
      this.materialService.getMaterialById(this.id)
        .subscribe(data => {
          this.material = data;
          this.userService.gerUserById(this.material.creatorId).subscribe(res => {
            this.user = res;
          }, error => console.log(error));
        }, error => console.log(error));
    });
  }

  ngOnInit(): void {
    this.material = new Material();
  }
}
