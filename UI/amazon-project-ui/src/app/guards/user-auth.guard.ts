import {Injectable} from '@angular/core';
import {ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot} from '@angular/router';
import {UserService} from "../services/user.service";

@Injectable({
  providedIn: 'root'
})
export class UserAuthGuard implements CanActivate {
  constructor(private authService: UserService, private router: Router) {
  }

  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): boolean {
    if (this.authService.loggedIn()) {
      return true;
    } else {
      this.router.navigate(['/login'], {
        queryParams: {returnUrl: state.url}
      });
      return false;
    }
  }
}
