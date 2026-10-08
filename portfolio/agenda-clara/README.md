# Agenda Clara — laboratório educacional

Este projeto fictício acompanha os módulos DTEM. Não usa dados de clientes nem representa experiência profissional contratada.

Executar `python agenda_clara.py` nesta pasta. São mostradas duas versões. A versão `AgendaComDefeito` aceita um nome composto somente por espaços; a versão de referência o rejeita. A comparação permite aprender teste negativo e reporte reproduzível. Reiniciar a classe entre testes independentes.

## Saída esperada para conferência

| Chamada | Referência | Com defeito |
|---|---|---|
| consultar inicial | H09, H10, H11 | H09, H10, H11 |
| reservar Ana/H09 | sucesso, id 1 | sucesso, id 1 |
| reservar Bruno/H09 | conflito | conflito |
| reservar espaços/H11 | nome_invalido | sucesso, id 2 |
| cancelar 1 | cancelado | cancelado |
| consultar final | H09, H10, H11 | H09, H10 |

A implementação guarda dados apenas em memória. Encerrar a execução perde o estado. O laboratório não demonstra API, interface web, autenticação, banco persistente ou concorrência distribuída.

## Estrutura que o aluno construirá

- `requisitos.md`: problema, regras e histórias.
- `testes.md`: plano, casos, execução e evidências.
- `bugs.md`: defeitos simulados e reteste.
- `sprint.md`: meta, capacidade, quadro e decisões.
- `release.md`: decisão de liberação simulada e rollback.
- `aprendizados.md`: contribuição pessoal e limitações.

Os arquivos de entrega são produzidos pelo aluno; os exemplos dos E-books servem como referência comentada.

