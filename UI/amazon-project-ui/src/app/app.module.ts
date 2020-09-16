import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {LoginComponent} from './login/login.component';
import {NotFoundComponent} from './not-found/not-found.component';
import {SweetAlert2Module} from "@sweetalert2/ngx-sweetalert2";
import {HTTP_INTERCEPTORS, HttpClient, HttpClientModule} from "@angular/common/http";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {TokenInterceptorService} from "./services/token-interceptor.service";
import {HomeComponent} from './home/home.component';
import {RouterModule} from "@angular/router";
import {MaterialComponent} from './material/material.component';
import { ProfileComponent } from './profile/profile.component';
import { ChartsModule } from 'ng2-charts';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    NotFoundComponent,
    HomeComponent,
    MaterialComponent,
    ProfileComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    SweetAlert2Module,
    HttpClientModule,
    ReactiveFormsModule,
    RouterModule,
    FormsModule,
    ChartsModule
  ],
  providers: [HttpClient,
    {provide: HTTP_INTERCEPTORS, useClass: TokenInterceptorService, multi: true}],
  bootstrap: [AppComponent]
})
export class AppModule {
}
