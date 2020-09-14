import {Component, OnInit} from '@angular/core';
import {UserService} from "../services/user.service";
import {ActivatedRoute, Router} from "@angular/router";
import Swal from "sweetalert2";
import {FormBuilder, FormControl, FormGroup, Validators} from "@angular/forms";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  loginForm: FormGroup;
  username: string;
  password: string;
  alertType = "alert-success";
  alertTitle = "INFO ! ";
  alertContent = "username : mrabusalah / password : root";

  constructor(private userService: UserService,
              private route: ActivatedRoute,
              private router: Router,
              private fb: FormBuilder
  ) {
  }

  ngOnInit(): void {
    this.loginForm = this.fb.group({
      username: new FormControl(null, Validators.required),
      password: new FormControl(null, Validators.required)
    });
  }

  onSubmit() {
    console.log("abusalah username" + this.loginForm.value.username);
    this.userService.userLogin(
      // this.loginForm.value.username,
      // this.loginForm.value.password
      "mrabusalah",
      "hi"
    ).subscribe(res => {

      localStorage.setItem('access_token', res.access_token);
      localStorage.setItem('refresh_token', res.refresh_token);
      localStorage.setItem('id', res.userId);
      localStorage.setItem('username', res.username);

      Swal.fire({
        position: 'center',
        icon: 'success',
        title: 'Your are login now ',
        footer: 'Welcome Back ' + this.username,
        showConfirmButton: false,
        timer: 2000
      });
      console.log("hello abusalah");
      this.router.navigate([``]);
    }, error => {
      this.alertType = "alert-danger";
      this.alertTitle = "WRONG ! ";
      this.alertContent = "enter the correct username and password please";
      console.log(error);
    })

  }

}
