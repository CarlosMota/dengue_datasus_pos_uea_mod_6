import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatRadioModule } from '@angular/material/radio';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatStepperModule } from '@angular/material/stepper';
import { MatSnackBarModule, MatSnackBar } from '@angular/material/snack-bar';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { ApiService, DengueNotification } from '../services/api';

@Component({
  selector: 'app-dengue-form',
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    MatDatepickerModule,
    MatNativeDateModule,
    MatButtonModule,
    MatCardModule,
    MatRadioModule,
    MatCheckboxModule,
    MatStepperModule,
    MatSnackBarModule,
    MatProgressSpinnerModule
  ],
  templateUrl: './dengue-form.html',
  styleUrls: ['./dengue-form.scss']
})
export class DengueFormComponent implements OnInit {
  dengueForm!: FormGroup;
  isLoading = false;
  
  // Opções para campos de seleção
  tipoNotificacao = [
    { value: '1', label: 'Negativa' },
    { value: '2', label: 'Individual' },
    { value: '3', label: 'Surto' },
    { value: '4', label: 'Agregado' }
  ];

  sexoOptions = [
    { value: 'M', label: 'Masculino' },
    { value: 'F', label: 'Feminino' },
    { value: 'I', label: 'Ignorado' }
  ];

  gestanteOptions = [
    { value: '1', label: '1º Trimestre' },
    { value: '2', label: '2º Trimestre' },
    { value: '3', label: '3º Trimestre' },
    { value: '4', label: 'Gestação ignorada' },
    { value: '5', label: 'Não' },
    { value: '6', label: 'Não se aplica' },
    { value: '9', label: 'Ignorado' }
  ];

  racaOptions = [
    { value: '1', label: 'Branca' },
    { value: '2', label: 'Preta' },
    { value: '3', label: 'Amarela' },
    { value: '4', label: 'Parda' },
    { value: '5', label: 'Indígena' },
    { value: '9', label: 'Ignorado' }
  ];

  escolaridadeOptions = [
    { value: '0', label: 'Analfabeto' },
    { value: '1', label: '1ª-4ª incompleto' },
    { value: '2', label: '4ª completo' },
    { value: '3', label: '5ª-8ª incompleto' },
    { value: '4', label: 'Fundamental completo' },
    { value: '5', label: 'Médio incompleto' },
    { value: '6', label: 'Médio completo' },
    { value: '7', label: 'Superior incompleto' },
    { value: '8', label: 'Superior completo' },
    { value: '9', label: 'Ignorado' },
    { value: '10', label: 'Não se aplica' }
  ];

  simNaoOptions = [
    { value: '1', label: 'Sim' },
    { value: '2', label: 'Não' }
  ];

  resultadoExameOptions = [
    { value: '1', label: 'Reagente' },
    { value: '2', label: 'Não reagente' },
    { value: '3', label: 'Inconclusivo' },
    { value: '4', label: 'Não realizado' }
  ];

  constructor(
    private fb: FormBuilder,
    private apiService: ApiService,
    private snackBar: MatSnackBar
  ) {}

  ngOnInit() {
    this.createForm();
    this.checkApiConnection();
  }

  createForm() {
    this.dengueForm = this.fb.group({
      // Campos de Identificação da Notificação
      tp_not: ['', Validators.required],
      id_agravo: [''],
      dt_notific: ['', Validators.required],
      sem_not: [''],
      nu_ano: [''],
      sg_uf_not: ['', Validators.required],
      id_municip: [''],
      id_regiona: [''],
      id_unidade: [''],

      // Dados do Paciente
      dt_sin_pri: [''],
      sem_pri: [''],
      ano_nasc: [''],
      nu_idade_n: [''],
      cs_sexo: ['', Validators.required],
      cs_gestant: [''],
      cs_raca: [''],
      cs_escol_n: [''],

      // Dados de Residência e Procedência
      sg_uf: [''],
      id_mn_resi: [''],
      id_rg_resi: [''],
      id_pais: [''],
      dt_invest: [''],
      id_ocupa_n: [''],

      // Sinais e Sintomas Clínicos
      febre: [''],
      mialgia: [''],
      cefaleia: [''],
      exantema: [''],
      vomito: [''],
      nausea: [''],
      dor_costas: [''],
      conjuntvit: [''],
      artrite: [''],
      artralgia: [''],
      petequia_n: [''],
      leucopenia: [''],
      laco: [''],
      dor_retro: [''],

      // Doenças Pré-existentes
      diabetes: [''],
      hematolog: [''],
      hepatopat: [''],
      renal: [''],
      hipertensa: [''],
      acido_pept: [''],
      auto_imune: [''],

      // Exames Laboratoriais
      dt_coleta: [''],
      resul_soro: [''],
      dt_ns1: [''],
      resul_ns1: [''],
      dt_viral: [''],
      resul_vi_n: [''],
      dt_pcr: [''],
      resul_pcr: [''],
      sorotipo: [''],
      histopa_n: [''],
      imunoh_n: [''],

      // Hospitalização e Local da Infecção
      hospitaliz: [''],
      dt_interna: [''],
      coufinf: [''],
      municipio: [''],
      tpautocto: [''],

      // Encerramento do Caso
      classi_fin: [''],
      criterio: [''],
      dt_encerra: [''],
      evolucao: [''],
      dt_obito: ['']
    });
  }

  checkApiConnection() {
    this.apiService.healthCheck().subscribe({
      next: (response) => {
        console.log('Conexão com API estabelecida:', response);
        this.showMessage('Conectado à API com sucesso!', 'success');
      },
      error: (error) => {
        console.error('Erro ao conectar com a API:', error);
        this.showMessage('Erro ao conectar com a API. Verifique se o servidor está rodando.', 'error');
      }
    });
  }

  onSubmit() {
    if (this.dengueForm.valid) {
      this.isLoading = true;
      
      const formData = this.prepareFormData();
      
      this.apiService.createDengueNotification(formData).subscribe({
        next: (response) => {
          this.isLoading = false;
          console.log('Notificação criada com sucesso:', response);
          this.showMessage('Notificação de dengue enviada com sucesso!', 'success');
          this.dengueForm.reset();
        },
        error: (error) => {
          this.isLoading = false;
          console.error('Erro ao enviar notificação:', error);
          this.showMessage('Erro ao enviar notificação. Tente novamente.', 'error');
        }
      });
    } else {
      console.log('Formulário inválido');
      this.markFormGroupTouched();
      this.showMessage('Por favor, preencha todos os campos obrigatórios.', 'warning');
    }
  }

  private prepareFormData(): DengueNotification {
    const formValue = this.dengueForm.value;
    
    // Converter datas para formato ISO string se necessário
    const dateFields = ['dt_notific', 'dt_sin_pri', 'dt_invest', 'dt_coleta', 'dt_ns1', 'dt_pcr', 'dt_interna', 'dt_encerra', 'dt_obito'];
    
    dateFields.forEach(field => {
      if (formValue[field] && formValue[field] instanceof Date) {
        formValue[field] = formValue[field].toISOString().split('T')[0];
      }
    });

    return formValue as DengueNotification;
  }

  private markFormGroupTouched() {
    Object.keys(this.dengueForm.controls).forEach(key => {
      const control = this.dengueForm.get(key);
      control?.markAsTouched();
    });
  }

  private showMessage(message: string, type: 'success' | 'error' | 'warning') {
    const config = {
      duration: 5000,
      panelClass: [`snackbar-${type}`]
    };
    
    this.snackBar.open(message, 'Fechar', config);
  }

  // Método para testar a conexão com a API
  testApiConnection() {
    this.checkApiConnection();
  }

  // Método para limpar o formulário
  clearForm() {
    this.dengueForm.reset();
    this.showMessage('Formulário limpo com sucesso!', 'success');
  }
}
