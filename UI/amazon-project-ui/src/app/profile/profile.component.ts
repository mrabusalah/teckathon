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
  // static hard-codded data because of credits issue from AWS
  chartData = [
    {data: [33, 40, 26, 55, 0, 10, 0, 80, 10, 96], label: 'التشتت'},
    {data: [67, 60, 74, 45, 100, 90, 100, 20, 95, 4], label: 'الانتباه'},
  ];
  chartLabels = ['01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00'];

}
