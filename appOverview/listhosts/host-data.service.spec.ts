import { TestBed, inject } from '@angular/core/testing';

import { HostDataService } from './host-data.service';

describe('HostDataService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [HostDataService]
    });
  });

  it('should be created', inject([HostDataService], (service: HostDataService) => {
    expect(service).toBeTruthy();
  }));
});
