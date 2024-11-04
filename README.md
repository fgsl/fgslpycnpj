# fgslpycnpj

Componente Python para validar CNPJ e calcular o dígito verificador para o novo padrão Alfanumérico definido pela [ Instrução Normativa nº 2.229](http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=141102).

Este componente está documentado em português porque CNPJ é um identificador que só faz sentido no Brasil.

Are you not understanding this documentation? Learn portuguese or use a translator.

## Como instalar

```shell
pip install fgslpycnpj
```

## Usando o componente

### Validando o CNPJ

```shell
$ python
>>> from fgslpycnpj.cnpj.CNPJ import CNPJ
>>> numero = "12.ABC.345/01DE-35"
>>> cnpj = CNPJ(numero)
>>> print(cnpj.valida())
```

### Calculando o dígito verificador

```shell
$ python
>>> from fgslpycnpj.cnpj.DigitoVerificador import DigitoVerificador
>>> base = "12.ABC.345"
>>> dv = CNPJ(base)
>>> print(dv.gera_dv())
```

## Para desenvolvedores

* **PKG-INFO** descreve o pacote de uma forma resumida.
* **MANIFEST.in** define quais arquivos serão incluídos dentro do pacote.
* **pyproject.toml** define a informação de empacotamento geral.

## Execute os testes

```shell
python -m unittest tests/cnpjtest.py 
```

### Construa o pacote

```shell
python -m build --sdist .
```

Requer o módulo `build`. Você pode instalá-lo usando `pip install build`.

### Atualize o pacote para o to PyPI

```shell
twine upload dist/*
```
