import {Injectable, Injector} from '@angular/core';
import {HttpEvent, HttpHandler, HttpHeaders, HttpInterceptor, HttpRequest} from "@angular/common/http";
import {Observable} from "rxjs";
import {UserService} from "./user.service";

@Injectable({
  providedIn: 'root'
})
export class TokenInterceptorService implements HttpInterceptor {

  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    if (this.userService.loggedIn()) {
      const authReq = req.clone({
        headers: new HttpHeaders({
          Authorization: `Basic ` + btoa('app' + ':' + 'passApp')
        })
      });
      return next.handle(authReq);
    } else {
      return next.handle(req);
    }
  }

  constructor(private injector: Injector, private userService: UserService) {
  }
}
