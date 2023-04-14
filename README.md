### Sistema de Credenciamento de Filmes e Avaliações 🎬

O projeto utiliza FastAPI para a construção de um backend que possibilita o cadastro de filmes e avaliações desses filmes.

#### Configurações 

Crie um ambiente virtual e instale as bibliotecas necesssárias:

```bash
pip install -r requirements.txt
```

É necessário também a criação de um arquivo `.env` com os caminhos globais para os arquivos `db_filmes.json` e `db_avaliacao.json`. 
O conteúdo mínimo desses dois arquivos deve ser a variável responsável pelo autoincremento dos ids. Conteúdo mínimo, demonstrado abaixo:
```python
{
  "count_id": 0
}
```

### Vídeo demonstração do funcionamento
Link : https://youtu.be/Nv5XD2XsCIU
