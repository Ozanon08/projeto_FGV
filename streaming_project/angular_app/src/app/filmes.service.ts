import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class FilmeService {

  private baseUrl = 'http://localhost:8000/api/';  // Substitua pela URL da sua API Django

  constructor(private http: HttpClient) { }

  getFilmes(): Observable<any> {
    return this.http.get(this.baseUrl + 'filmes/')
        .pipe(
            catchError(error => {
                console.error('Erro ao buscar filmes:', error);
                throw error;
            })
        );
  }

}
