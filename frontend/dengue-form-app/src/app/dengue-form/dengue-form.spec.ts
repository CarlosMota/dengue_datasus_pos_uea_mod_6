import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ReactiveFormsModule } from '@angular/forms';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { HttpClientTestingModule } from '@angular/common/http/testing';

import { DengueFormComponent } from './dengue-form';

describe('DengueFormComponent', () => {
  let component: DengueFormComponent;
  let fixture: ComponentFixture<DengueFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [
        DengueFormComponent,
        ReactiveFormsModule,
        NoopAnimationsModule,
        MatSnackBarModule,
        HttpClientTestingModule
      ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DengueFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should initialize form with required fields', () => {
    expect(component.dengueForm).toBeDefined();
    expect(component.dengueForm.get('tp_not')).toBeTruthy();
    expect(component.dengueForm.get('dt_notific')).toBeTruthy();
    expect(component.dengueForm.get('sg_uf_not')).toBeTruthy();
    expect(component.dengueForm.get('cs_sexo')).toBeTruthy();
  });

  it('should mark form as invalid when required fields are empty', () => {
    expect(component.dengueForm.valid).toBeFalsy();
  });

  it('should mark form as valid when required fields are filled', () => {
    component.dengueForm.patchValue({
      tp_not: '2',
      dt_notific: new Date(),
      sg_uf_not: 'SP',
      cs_sexo: 'M'
    });
    expect(component.dengueForm.valid).toBeTruthy();
  });
});
