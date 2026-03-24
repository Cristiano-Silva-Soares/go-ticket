import { Routes } from '@angular/router';

import { HomeComponent } from './pages/home/home';
import { LoginComponent } from './pages/login/login';
import { RegisterComponent } from './pages/login-register/login-register';

import { Dashboard } from './pages/dashboard/dashboard';
import { TicketSale } from './pages/ticket-sale/ticket-sale';
import { Reports } from './pages/reports/reports';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'login', component: LoginComponent },
  { path: 'user-register', component: RegisterComponent },
  { path: 'dashboard', component: Dashboard },
  { path: 'sale', component: TicketSale },
  { path: 'reports', component: Reports }
];