<p align="center">
  <img src="img/logo.png" alt="Logo HydroAlert" width="250"/>
</p>

# Scripts de Segurança e Acessibilidade

Este repositório contém scripts Python desenvolvidos para fornecer funcionalidades essenciais ao aplicativo **HydroAlerta+**, voltado para alertas de enchentes, acessibilidade e rotas seguras em situações de risco.

##  Estrutura dos Scripts

### 1. `broadcast_alerts.py`
Realiza a simulação de envio de alertas para diferentes locais públicos.

- **Função principal**: `broadcast_alerts(locais, mensagens)`
- **Descrição**: Exibe combinações de mensagens de alerta e locais (como metrôs ou terminais) simulando a divulgação pública da emergência.

---

### 2. `alert_translation.py`
Oferece suporte multilíngue para alertas, permitindo que usuários escolham entre português, inglês e espanhol.

- **Função principal**: `exibir_frases(idioma)`
- **Descrição**: Exibe frases importantes em três idiomas diferentes com base na escolha do usuário (1, 2 ou 3).

---

### 3. `safe_routes.py`
Ajuda na recomendação de rotas mais seguras com base no risco identificado nas regiões.

- **Função principal**: `recomendar_rota(ruas)`
- **Descrição**: Analisa uma lista de ruas e indica as mais seguras, filtrando aquelas que possuem nível de risco baixo.

---

### 4. `check_risk_zones.py`
Permite verificar o nível de risco de determinadas regiões.

- **Função principal**: `verificar_zonas_de_risco(zonas)`
- **Descrição**: Recebe uma lista de zonas e seus níveis de risco, informando o status de segurança de cada uma.

---

###  5. `region_tips.py`
Fornece dicas de prevenção baseadas em regiões específicas.

- **Função principal**: `mostrar_dicas(regiao)`
- **Descrição**: Exibe uma ou mais dicas de prevenção conforme a região selecionada pelo usuário (por exemplo, Zona Norte ou Zona Sul).

---

### 6. `alert_history.py`
Mantém e exibe o histórico de alertas recebidos.

- **Função principal**: `exibir_historico(alertas)`
- **Descrição**: Lista todos os alertas registrados, permitindo ao usuário consultar ocorrências passadas.

---

### 7. `location_alerts.py`
Exibe alertas por localização.

- **Função principal**: `mostrar_alertas_por_local(locais_alertas)`
- **Descrição**: Recebe um dicionário de locais com seus respectivos alertas e os exibe de forma organizada.

---

### 8. `accessibility.py`
Garante acessibilidade a pessoas com deficiência visual.

- **Função principal**: `ler_alerta_em_voz(texto)`
- **Descrição**: Simula a leitura em voz alta de alertas, garantindo inclusão de usuários com deficiência visual.

---

## Como usar

Cada script pode ser executado individualmente com `python nome_do_script.py`

### Exemplo de execução:
```bash
python broadcast_alerts.py
```

---


## Executando os Testes com Pytest

Certifique-se de que o `pytest` está instalado:

```bash
pip install pytest
```

Para rodar todos os testes do projeto:

```bash
pytest
```

Para rodar um teste específico:
```bash
pytest tests/test_broadcast_alerts.py
```

---

## 📜 Licença
Este projeto é licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

[![Licença MIT](https://img.shields.io/badge/Licença-MIT-green)](LICENSE)

---


## 👥 Integrantes
- **Gabriel Augusto - RM564126**
- **Beatriz Cortez - RM561431**
- **Bruno Alves - RM563986**

---


💡 _Este projeto visa fortalecer a segurança da população por meio da tecnologia, promovendo acesso rápido a alertas e rotas seguras durante enchentes. _🌧️📲