# Projeto Django - Sisgef

## Descrição
Sisgef é um projeto Django para gerenciamento de sistemas. Este README fornece instruções sobre como configurar e executar o projeto localmente.

## Requisitos
- Python 3.x
- Django 3.x
- Virtualenv

## Instalação

### Clonar o repositório
```bash
git clone https://github.com/seu-usuario/sisgef.git
cd sisgef
```

### Criar e ativar o ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

### Instalar dependências
```bash
pip install -r requirements.txt
```

### Configurar o banco de dados
Edite o arquivo `settings.py` para configurar o banco de dados conforme necessário.

### Aplicar migrações
```bash
python manage.py migrate
```

### Criar superusuário
```bash
python manage.py createsuperuser
```

### Executar o servidor de desenvolvimento
```bash
python manage.py runserver
```

## Testes
Para rodar os testes, use o comando:
```bash
python manage.py test
```

## Contribuição
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Faça o push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato
Para mais informações, entre em contato com [raphael.muniz@ifrn.edu.br](mailto:raphael.muniz@ifrn.edu.br).
