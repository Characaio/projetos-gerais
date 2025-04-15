const login = document.getElementById("login")
    const diva = document.getElementById("diva")
    const primeiro = 
    `<form id="formulario">
    <div>
    <label> Nome: <br> <input class="texto" type="text" name="nome" required></label><br>
    <label> 
        <input type="radio" name = "sexo" value="masculino" required> masculino
        <input type="radio" name = "sexo" value="feminino" required> feminino
    </label><br>
    <label> idade <br> <input type="text" name="idade" required></label><br>
    <label> Telefone <br> <input type="text" name="telefone" placeholder="DD xxxxx-xxxx" required></label><br>
    <label> Email <br> <input type="email" name="email" required></label>
    </div>
    </form>
    <div>
      <button id="deslog">sair</button>
      <button id="proximo"> proximo</button>
    </div>
    `
    const segundo = 
    `
    <form id="formulario">
    <legend>Endereço</legend>
    <label>rua <br> <input type="text" name="rua" required></label> <br>
    <label>Número da casa<br> <input type="text" name="numero" required></label> <br>
    <label>Cidade <br> <input type="text" name="cidade" required></label> <br>
    <label> UF:
      <select name="estados" name="estado" required>
      <option value="selecione">selecione</option>
      <option value="AC">Acre</option>
      <option value="SP">São Paulo</option>
      <option value="CE">Ceara</option>
      </select> 
    </label>
    </form>
    <button id="voltar"> anterior </button>
    <button id="proximo"> proximo</button>
    `
    const terceiro = 
    `
    <form id="formulario">
    <label> Periodo: 
    <input type="radio" name="periodo" value="manhã" required> manhã  
    <input type="radio" name="periodo" value="tarde" required> tarde 
    <input type="radio" name="periodo" value="noite" required> noite
    </label><br><br>
    <label> Deixe-nos uma mensagem <br> <textarea name="mensagem" cols="70"  rows="10">  </textarea></label><br><br>
    <label> Senha: <input type="password" name="senha" required></label>
    </form>
    <button id="voltar"> anterior </button>
    <button id="finalizar"> finalizar </button>
    `
    let finalizado = false
    let escondido = false
    let proximos = 0
    
    login.addEventListener('click', () =>{
      if (proximos != 0){
        diva.innerHTML = primeiro
      }
      if (escondido){
        diva.classList.remove('sair');
        escondido = false
        }
        diva.classList.add('entra');
    });

    diva.addEventListener('click', (e) =>{
      id = e.target.id;
      
      if (id === "proximo"){
        if (proximos === 0){
          const form = document.getElementById("formulario")
          const formdata1 = new FormData(form);
          dados1 = Object.fromEntries(formdata1.entries());
          proximos = 1
          console.log('indo pro segundo log',proximos)
          diva.innerHTML = segundo
          } 
          else if (proximos === 1){
            const form = document.getElementById("formulario")
            const formdata2 = new FormData(form);
            dados2 = Object.fromEntries(formdata2.entries());
            console.log("indo pro terceiro log", proximos)
            proximos = 2
            diva.innerHTML = terceiro
          }
      }

    if (id == "voltar"){
      if (proximos === 1){
        console.log("voltando pro primeiro log", proximos)
        proximos = 0;
        diva.innerHTML = primeiro
        }

      if (proximos === 2){
        console.log("voltando pro segundo log", proximos)
        proximos = 1 
        diva.innerHTML = segundo
        }

      }
      if (id === "deslog"){
        esconder()
      }

      if (id === "finalizar"){
        const form = document.getElementById("formulario")
        console.log('finalizado')
        const formdata3 = new FormData(form);
        dados3 = Object.fromEntries(formdata3.entries());
        console.log(dados1,dados2,dados3)
        esconder()
      }
    }
  )