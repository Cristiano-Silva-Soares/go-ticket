import { Routes } from '@angular/router';

import { Home } from './pages/home/home';
import { Login } from './pages/login/login';
import { Dashboard } from './pages/dashboard/dashboard';
import { TicketSale } from './pages/ticket-sale/ticket-sale';
import { Reports } from './pages/reports/reports';

export const routes: Routes = [
  { path: '', component: Home },
  { path: 'login', component: Login },
  { path: 'dashboard', component: Dashboard },
  { path: 'sale', component: TicketSale },
  { path: 'reports', component: Reports }
];