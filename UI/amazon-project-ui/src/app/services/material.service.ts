import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Router} from "@angular/router";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class MaterialService {

  private baseUrl = 'http://localhost:8080/api/materials';

  constructor(private http: HttpClient, private router: Router) {
  }

  getAllMaterials(): Observable<any> {
    return this.http.get(this.baseUrl);
  }
}
