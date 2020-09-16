import {Component, OnInit} from '@angular/core';
import {MaterialService} from "../services/material.service";
import {Material} from "../model/Material";
import {UserService} from "../services/user.service";
import Swal from "sweetalert2";
import {Router} from "@angular/router";
import {User} from "../model/User";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  username: string;
  materials: Material[];
  user: User;

  constructor(private materialService: MaterialService,
              private userService: UserService,
              private router: Router) {
  }

  ngOnInit(): void {
    this.user = new User();
    this.username = localStorage.getItem("username");
    this.materialService.getAllMaterials().subscribe(res => {
      this.materials = res;
      this.userService.gerUserByUsername(this.username).subscribe(data => {
        this.user = data;
      });
    }, error => {
      console.log(error);
    });
  }

  logout() {
    Swal.fire({
      title: 'Are you sure?',
      text: "You won't be able to revert this!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#f6981c',
      confirmButtonText: 'Yes, logout!'
    }).then((result) => {
      if (result.isConfirmed) {
        this.userService.userLogout();
        Swal.fire(
          'DONE!',
          'LOGGED OUT SUCCESSFULLY.',
          'success'
        )
      }
    })
  }

  profile(username: string) {
    this.router.navigate(['profile', username]);
  }
}
