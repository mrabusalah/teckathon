import {Component, OnInit} from '@angular/core';
import {User} from "../model/User";
import {ActivatedRoute, ParamMap, Router} from "@angular/router";
import {UserService} from "../services/user.service";

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {

  user: User;
  username: string;

  constructor(private route: ActivatedRoute,
              private router: Router,
              private userService: UserService) {
    this.route.paramMap.subscribe((param: ParamMap) => {
      this.username = param.get('username');
      this.userService.gerUserByUsername(this.username)
        .subscribe(data => {
          this.user = data;
        }, error => console.log(error));
    });
  }

  ngOnInit(): void {
    this.user = new User();
  }

  goHome() {
    this.router.navigate(['/home']);
  }

  chartOptions = {
    responsive: true
  };
  // static hard-codded data becuase of credits issue from AWS
  chartData = [
    {data: [33, 60, 26, 70], label: 'التشتت'},
    {data: [12, 45, 100, 34], label: 'الانتباه'},
  ];
  chartLabels = ['January', 'February', 'Mars', 'April'];

}
