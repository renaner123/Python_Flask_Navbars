## Exemplo de utilização de Navbars, Sidebars com uso de Bootstrap, Python e Flask


## Como executar

  - Windows: 

    Para executar na plataforma windows é necessário apenas executar o script [executar.sh](executar.sh) ou se preferir fazer manualmente, pode usar os seguintes comandos estando na pasta raíz.

    ```bash
        cd venv/scripts        
        # ativando o ambiente virtual python
        activate
        cd ../../
        # instalando as dependências
        pip install -r requirements.txt        
        # executando a aplicação.
        python app.py
    ```

- Linux:

    Para compilar em plataforma linux, será necessário criar um novo ambiente virtual para o python com:

    ```bash
    # Criar ambiente virtual python
    python3 -m venv venv

    # ativar o amboente virtual
    source venv/bin/activate

    # para instalar as dependências
    pip install -r requirements.txt

    # para executar a aplicação
    python3 app.py
    ```

## Adicionando novos menus no Sidebar

No arquivo [app.py](app.py) é necessário criar uma nova rota para para adicionar um novo menu no Sidebar, no caso, uma nova página de um produto por exemplo. Rota a ser criada deverá ficar como essa abaixo. Ela será utilizada para receber o endereço da imagem que será exibida e retornar para a página de destino.

```python
@app.route('/route', methods=['GET', 'POST'])
def imgRoute3():
    imgSrc = ((request.values.get('path')))
    return render_template('page.html', title='Page 3', form=imgSrc), 200
```

Após ter a rota criada, é necessário criar a página HTML dentro da pasta [templates](/templates) que exibirá as imagens do produto em questão, pode usar como modelo as já criadas. Elas foram criadas usando o extends do Flask. 

Após isso é necessário adicionar uma nova linha no navbar do arquivo [base_test.html](templates/base_test.html)

```html
    <div id="conteudo-1" class="navbar navbar-dark bg-dark container">
        <nav>
            <ul class="nav flex-column">
                <li class="nav-item">
                    <a class="btn btn-dark btn-lg" href="/route1?path=work-in-progress.png">Product 1</a>
                </li>
            </ul>
        </nav>
    </div>
```


## Informações

Para os menus do dropdown funcionar, foi necessário inserir nas páginas na parte de scrips os seguintes scripts. Podem ser alterados conforme a necessiade.

```js
    $('ul.dropdown-menu [data-toggle=dropdown]').on('click', function(event) {
    // Avoid following the href location when clicking
    event.preventDefault();
    // Avoid having the menu to close when clicking
    event.stopPropagation();
    // If a menu is already open we close it
    $('ul.dropdown-menu [data-toggle=dropdown]').parent().removeClass('open');
    // opening the one you clicked on
    $(this).parent().addClass('open');

    var menu = $(this).parent().find("ul");
    var menupos = menu.offset();

    if ((menupos.left + menu.width()) + 30 > $(window).width()) {
        var newpos = - menu.width();
    } else {
        var newpos = $(this).parent().width();
    }
    menu.css({ left:newpos });
```

e no arquivo de estilo.css

```css
    .dropdown-submenu{position:relative;}
    .dropdown-submenu>.dropdown-menu{top:0;left:100%;margin-top:-6px;margin-left:-1px;-webkit-border-radius:0 6px 6px 6px;-moz-border-radius:0 6px 6px 6px;border-radius:0 6px 6px 6px;}
    /*.dropdown-submenu:hover>.dropdown-menu{display:block;}*/
    .dropdown-submenu>a:after{display:block;content:" ";float:right;width:0;height:0;border-color:transparent;border-style:solid;border-width:5px 0 5px 5px;border-left-color:#cccccc;margin-top:5px;margin-right:-10px;}
    .dropdown-submenu:hover>a:after{border-left-color:#ffffff;}
    .dropdown-submenu.pull-left{float:none;}.dropdown-submenu.pull-left>.dropdown-menu{left:-100%;margin-left:10px;-webkit-border-radius:6px 0 6px 6px;-moz-border-radius:6px 0 6px 6px;border-radius:6px 0 6px 6px;}
```