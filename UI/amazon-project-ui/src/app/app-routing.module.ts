import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {LoginComponent} from "./login/login.component";
import {NotFoundComponent} from "./not-found/not-found.component";
import {HomeComponent} from "./home/home.component";
import {MaterialComponent} from "./material/material.component";
import {UserAuthGuard} from "./guards/user-auth.guard";

const routes: Routes = [
  {path: '', redirectTo: '/home', pathMatch: 'full'},
  {path: 'login', component: LoginComponent},
  {path: 'home', component: HomeComponent, canActivate: [UserAuthGuard]},
  {path: 'material/:id', component: MaterialComponent, canActivate: [UserAuthGuard]},
  {path: '**', pathMatch: 'full', redirectTo: '/404'},
  {path: '404', component: NotFoundComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
