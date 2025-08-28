import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';

import { ApiService } from './api';

describe('ApiService', () => {
  let service: ApiService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      providers: [ApiService]
    });
    service = TestBed.inject(ApiService);
    httpMock = TestBed.inject(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify();
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should perform health check', () => {
    const mockResponse = { status: 'OK' };

    service.healthCheck().subscribe(response => {
      expect(response).toEqual(mockResponse);
    });

    const req = httpMock.expectOne('http://localhost:5000/api/../health');
    expect(req.request.method).toBe('GET');
    req.flush(mockResponse);
  });

  it('should create dengue notification', () => {
    const mockNotification = {
      tp_not: '2',
      dt_notific: '2025-01-01',
      sg_uf_not: 'SP',
      cs_sexo: 'M'
    };
    const mockResponse = { success: true, data: mockNotification };

    service.createDengueNotification(mockNotification).subscribe(response => {
      expect(response).toEqual(mockResponse);
    });

    const req = httpMock.expectOne('http://localhost:5000/api/dengue-notifications');
    expect(req.request.method).toBe('POST');
    expect(req.request.body).toEqual(mockNotification);
    req.flush(mockResponse);
  });
});
