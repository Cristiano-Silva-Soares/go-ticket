import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { TicketsService } from './services/tickets';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class App {

  protected readonly title = signal('go-ticket');

  constructor(private ticketsService: TicketsService) {
  }

}