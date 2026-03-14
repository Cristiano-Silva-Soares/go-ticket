import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TicketSale } from './ticket-sale';

describe('TicketSale', () => {
  let component: TicketSale;
  let fixture: ComponentFixture<TicketSale>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TicketSale],
    }).compileComponents();

    fixture = TestBed.createComponent(TicketSale);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
