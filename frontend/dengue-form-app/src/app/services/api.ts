import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, map } from 'rxjs/operators';

export interface DengueNotification {
  id?: number;
  // Identificação da Notificação
  tp_not: string;
  id_agravo?: string;
  dt_notific: string;
  sem_not?: string;
  nu_ano?: string;
  sg_uf_not: string;
  id_municip?: string;
  id_regiona?: string;
  id_unidade?: string;

  // Dados do Paciente
  dt_sin_pri?: string;
  sem_pri?: string;
  ano_nasc?: string;
  nu_idade_n?: string;
  cs_sexo: string;
  cs_gestant?: string;
  cs_raca?: string;
  cs_escol_n?: string;

  // Dados de Residência e Procedência
  sg_uf?: string;
  id_mn_resi?: string;
  id_rg_resi?: string;
  id_pais?: string;
  dt_invest?: string;
  id_ocupa_n?: string;

  // Sinais e Sintomas Clínicos
  febre?: string;
  mialgia?: string;
  cefaleia?: string;
  exantema?: string;
  vomito?: string;
  nausea?: string;
  dor_costas?: string;
  conjuntvit?: string;
  artrite?: string;
  artralgia?: string;
  petequia_n?: string;
  leucopenia?: string;
  laco?: string;
  dor_retro?: string;

  // Doenças Pré-existentes
  diabetes?: string;
  hematolog?: string;
  hepatopat?: string;
  renal?: string;
  hipertensa?: string;
  acido_pept?: string;
  auto_imune?: string;

  // Exames Laboratoriais
  dt_coleta?: string;
  resul_soro?: string;
  dt_ns1?: string;
  resul_ns1?: string;
  dt_viral?: string;
  resul_vi_n?: string;
  dt_pcr?: string;
  resul_pcr?: string;
  sorotipo?: string;
  histopa_n?: string;
  imunoh_n?: string;

  // Hospitalização e Local da Infecção
  hospitaliz?: string;
  dt_interna?: string;
  coufinf?: string;
  municipio?: string;
  tpautocto?: string;

  // Encerramento do Caso
  classi_fin?: string;
  criterio?: string;
  dt_encerra?: string;
  evolucao?: string;
  dt_obito?: string;
}

export interface ApiResponse<T> {
  success: boolean;
  data?: T;
  message?: string;
  error?: string;
}

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:5000/api';

  constructor(private http: HttpClient) {}

  private getHttpOptions() {
    return {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      })
    };
  }

  // Métodos para notificações de dengue
  createDengueNotification(notification: DengueNotification): Observable<ApiResponse<DengueNotification>> {
    return this.http.post<ApiResponse<DengueNotification>>(
      `${this.apiUrl}/dengue-notifications`,
      notification,
      this.getHttpOptions()
    ).pipe(
      catchError(this.handleError)
    );
  }

  getDengueNotifications(): Observable<ApiResponse<DengueNotification[]>> {
    return this.http.get<ApiResponse<DengueNotification[]>>(
      `${this.apiUrl}/dengue-notifications`,
      this.getHttpOptions()
    ).pipe(
      catchError(this.handleError)
    );
  }

  getDengueNotificationById(id: number): Observable<ApiResponse<DengueNotification>> {
    return this.http.get<ApiResponse<DengueNotification>>(
      `${this.apiUrl}/dengue-notifications/${id}`,
      this.getHttpOptions()
    ).pipe(
      catchError(this.handleError)
    );
  }

  updateDengueNotification(id: number, notification: DengueNotification): Observable<ApiResponse<DengueNotification>> {
    return this.http.put<ApiResponse<DengueNotification>>(
      `${this.apiUrl}/dengue-notifications/${id}`,
      notification,
      this.getHttpOptions()
    ).pipe(
      catchError(this.handleError)
    );
  }

  deleteDengueNotification(id: number): Observable<ApiResponse<any>> {
    return this.http.delete<ApiResponse<any>>(
      `${this.apiUrl}/dengue-notifications/${id}`,
      this.getHttpOptions()
    ).pipe(
      catchError(this.handleError)
    );
  }

  // Métodos para usuários (compatibilidade com a API existente)
  createUser(user: any): Observable<ApiResponse<any>> {
    return this.http.post<ApiResponse<any>>(
      `${this.apiUrl}/users`,
      user,
      this.getHttpOptions()
    ).pipe(
      catchError(this.handleError)
    );
  }

  getUsers(): Observable<ApiResponse<any[]>> {
    return this.http.get<ApiResponse<any[]>>(
      `${this.apiUrl}/users`,
      this.getHttpOptions()
    ).pipe(
      catchError(this.handleError)
    );
  }

  getUserById(id: number): Observable<ApiResponse<any>> {
    return this.http.get<ApiResponse<any>>(
      `${this.apiUrl}/users/${id}`,
      this.getHttpOptions()
    ).pipe(
      catchError(this.handleError)
    );
  }

  updateUser(id: number, user: any): Observable<ApiResponse<any>> {
    return this.http.put<ApiResponse<any>>(
      `${this.apiUrl}/users/${id}`,
      user,
      this.getHttpOptions()
    ).pipe(
      catchError(this.handleError)
    );
  }

  deleteUser(id: number): Observable<ApiResponse<any>> {
    return this.http.delete<ApiResponse<any>>(
      `${this.apiUrl}/users/${id}`,
      this.getHttpOptions()
    ).pipe(
      catchError(this.handleError)
    );
  }

  // Health check
  healthCheck(): Observable<any> {
    return this.http.get(`${this.apiUrl}/../health`).pipe(
      catchError(this.handleError)
    );
  }

  private handleError(error: any): Observable<never> {
    console.error('Erro na API:', error);
    
    let errorMessage = 'Erro desconhecido';
    
    if (error.error instanceof ErrorEvent) {
      // Erro do lado do cliente
      errorMessage = `Erro: ${error.error.message}`;
    } else {
      // Erro do lado do servidor
      errorMessage = `Código do erro: ${error.status}\nMensagem: ${error.message}`;
      
      if (error.error && error.error.message) {
        errorMessage = error.error.message;
      }
    }
    
    return throwError(() => new Error(errorMessage));
  }
}
