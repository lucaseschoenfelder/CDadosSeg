# CI1030_ERE2_2021
Projeto criado como requisito parcial à conclusão da matéria CI1030, ministrada no ERE2 em 2021 pelo professor Drº André Grégio.

## Dataset escolhido
[Malicious and Benign Webpages](https://data.mendeley.com/datasets/gdx3pkwp47/2), dataset de classificação de webpages como maliciosas ou benignas. 

## Campos do dataset
O dataset possui 361.934 instâncias caracterizadas por **12 atributos**, sendo estes:
* **url**: a url da página.
* **url\_len**: o comprimento da url.
* **ip\_add**: local geográfico em que a página é hospedada.
* **geo\_loc**: país de origem da página.
* **tld**: top level domain da página.
* **who_is**: se a informação WHO IS do domínio está completa ou não.
* **htps**: se o site usa https ou não.
* **js\_len**: comprimento de código javascript na página.
* **js\_obf\_len**: comprimento de código javascript ofuscado na página.
* **content**: o conteúdo bruto da página com código javascript incluso.
* **label**: o rótulo da classe em benigna ou maligna.
