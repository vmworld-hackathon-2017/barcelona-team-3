import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ListhostsComponent } from './listhosts.component';

describe('ListhostsComponent', () => {
  let component: ListhostsComponent;
  let fixture: ComponentFixture<ListhostsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListhostsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ListhostsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
