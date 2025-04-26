const login = document.getElementById("login")
const diva = document.getElementById("diva")
const opções = [
  `<form id="formulario">
  <label> Nome: <br> <input class="texto" type="text" name="nome" required></label><br>
  <label> 
  <input type="radio" name = "sexo" value="masculino" required> masculino
  <input type="radio" name = "sexo" value="feminino" required> feminino
  <input type="radio" name = "sexo" value="prefiro não dizer" required> prefiro não dizer
  </label><br><br>
  <label> idade <br> <input type="text" name="idade" required></label><br>
  <label> Telefone <br> <input type="text" name="telefone" placeholder="DD xxxxx-xxxx" required></label><br>
  <label> Email <br> <input type="email" name="email" required></label> <br> <br>
  <select name="EstadoCivil" name="estadocivil" required>
  <option value="selecione">selecione</option>
  <option value="Casada(o)">Casada(o)</option>
  <option value="Solteira(o)">Solteira(o)</option>
  <option value="Viuva(o)">Viuva(o)</option>
  <option value="Divorcida(o)">Divorcida(o)</option>
  </select> 
  </form>
  <button id="voltar"> anterior </button>
  <button id="proximo"> proximo</button>
  `,
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
  `,
  `
  <form id="formulario">
  <label> idiomas:
  <input type="radio" name="idioma" value="ingles" required> Inglês
  <input type="radio" name="idioma" value="espanhol" required> Espanhol
  <input type="radio" name="idioma" value="frances" required> Francês
  <input type="radio" name="idioma" value="italiano" required> Italiano
  <input type="radio" name="idioma" value="alemao" required> Ilemão
  </label>
  </form>
  <button id="voltar"> anterior </button>
  <button id="finalizar"> finalizar </button>
  `,
  `
  <form id="formulario">
  <label> Login: <br> <input class="texto" type ="text" name="login" value="login placeholder="SeuNome" required> <br><br>
  <label> Senha: <br> <input class="texto" type ="text" name="senha" value="senha placeholder="SeuNome" required> <br><br>
  <label> Confirmar Senha: <br> input class="texto" type ="text" name="senha2" value="senha2 placeholder="SeuNome" required> <br><br>
  </form>
  <button id="voltar"> anterior </button>
  <button id="finalizar"> finalizar </button>
  `,
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
]
let DadosGerais = []

let finalizado = false
let escondido = false
let proximos = 0
let escolha = 0

function esconder(){
  diva.classList.remove('entra')
  diva.classList.add('sair')
}
function PushData(){
  const form = document.getElementById("formulario")
  const formdata = new FormData(form);
  dados = Object.fromEntries(formdata.entries());
  
  DadosGerais.push(dados)
  diva.innerHTML = opções[escolha]

}
login.addEventListener('click', () =>{
    escolha = 0
    diva.innerHTML = opções[escolha]
  
  if (escondido){
    diva.classList.remove('sair');
    escondido = false
    }
    diva.classList.add('entra');
  }
  
);

diva.addEventListener('click', (e) =>{
id = e.target.id;

if (id === "proximo"){
  PushData()
  escolha += 1
  console.log(escolha)
}

if (id == "voltar"){
  if (escolha != 0){
    console.log('NãO DA MLK')
  }
  else{
    escolha -= 1
    diva.innerHTML = opções[escolha]
  }

  }
  if (id === "deslog"){
    esconder()
  }

  if (id === "finalizar"){
    PushData()
    esconder()
  }
}
)