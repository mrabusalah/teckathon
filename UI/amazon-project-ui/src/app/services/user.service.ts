import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Router} from "@angular/router";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class UserService {

  private baseUrl = 'http://localhost:8080/api/users';

  constructor(private http: HttpClient, private router: Router) {
  }

  userLogin(username: string, password: string): Observable<any> {
    const headers = {
      headers: new HttpHeaders({
        Authorization: 'Basic ' + btoa('app:passApp')
      })
    };
    return this.http.post(`http://localhost:8080/oauth/token?grant_type=password&username=${username}&password=${password}`,
      {},
      headers);
  }

  userLogout() {
    this.router.navigate(['/login']);
    return localStorage.clear();
  }

  loggedIn() {
    return !!localStorage.getItem('access_token');
  }

}
